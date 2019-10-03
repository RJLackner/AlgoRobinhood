import robinhood_api.stocks as stocks
import logging
import numpy
import robinhood_api.account as account
from recommendation_system.data_pipeline.stock_price_data_pipeline import *
from sklearn.pipeline import Pipeline
from recommendation_system.estimation_models import tensorflow_lstm, random_forest_classifer
import pandas as pd
from sklearn.metrics import accuracy_score


def stock_rating(login, symbol, ml_model='LSTM', perf_window=5, label_pct_cutoff=0.05, historic_window=30, seed=7):
    """
    :param symbol: a string of symbol name
    :param ml_model: a string of selected machine learning model in the recommendation system
    :param perf_window: an integer of performance window that is used to define target label
    :param label_pct_cutoff: a double to define the threshold to label 1 when price go up by certain percentage
    :param historic_window: an integer of look back window which is used to define lagged features as predictors
    :param seed: random number seed
    :return: dictionary of {symbol: [model_forecast_prob, model_accuracy]}
    """
    logger = logging.getLogger(__name__)

    # fix random seed for reproducibility
    numpy.random.seed(seed)

    # get data from Robinhood API
    price = stocks.get_historicals(login, [symbol], span="year", interval="day", bounds='regular')
    price_data = pd.DataFrame.from_dict(price)
    price_data[['close_price', 'high_price', 'low_price', 'open_price', 'volume']] = price_data[
        ['close_price', 'high_price', 'low_price', 'open_price', 'volume']].apply(pd.to_numeric)

    # data pipeline
    data_pipeline = Pipeline([
        ('DeriveVariable',
         DeriveVariable(perf_window=perf_window, label_pct_cutoff=label_pct_cutoff, historic_window=historic_window)),
        ('CreateTrainTestForecastData', CreateTrainTestForecastData(test_size=0.33, seed=seed))
    ])

    X_train, X_test, y_train, y_test, X_forecast = data_pipeline.fit_transform(price_data)

    # model building
    if ml_model.upper() == 'LSTM':
        estimation_model = tensorflow_lstm.TensorFlowEstimator(X_train, y_train)
        model = estimation_model.fit()

        # model performance
        score = model.model.evaluate(X_test, y_test, verbose=0)
        accuracy = score[1]

        # forecast prediction
        y_forecast_pred = model.model.predict(X_forecast)[0][0]

    elif ml_model.upper() == 'RF':
        estimation_model = random_forest_classifer.RandomForestEstimator(X_train, y_train)
        model = estimation_model.fit()

        # model performance
        y_pred_test = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred_test)

        # forecast prediction
        y_forecast_pred = 1 - model.predict_proba(X_forecast)[0][0]

    else:
        # default / None is using LSTM
        estimation_model = tensorflow_lstm.TensorFlowEstimator(X_train, y_train)
        model = estimation_model.fit()

        # model performance
        score = model.model.evaluate(X_test, y_test, verbose=0)
        accuracy = score[1]

        # forecast prediction
        y_forecast_pred = model.model.predict(X_forecast)[0][0]

    logger.info(
        "Symbol {symbol} model accuracy is {accuracy}%, with prob of {forecast_prob}%"
        " to go up by {pct}% over the next {days} days ".format(
            symbol=symbol, accuracy=round(accuracy * 100, 2), pct=round(label_pct_cutoff * 100, 2), days=perf_window,
            forecast_prob=round(y_forecast_pred * 100, 2)))

    return {symbol: [y_forecast_pred, accuracy]}


def buy_stock_recommend_rating(login, ml_model='LSTM', top=5, perf_threshold=0.8):
    """
    :param login: login instance
    :param ml_model: a string of selected machine learning model in the recommendation system
    :param top: integer of showing top recommended stock in the log, ranked from high to low prob of price going up
    :param perf_threshold: double of only looking at models with performance >= the value
    :return: a list of top recommended {symbol: [model_forecast_prob, model_accuracy]}
    """
    # get watch list

    logger = logging.getLogger(__name__)

    watchlist_symbols = account.get_symbols_from_watchlist(login=login)

    ml_model_dict = {'LSTM': 'Long Short Term Memory networks - LSTM', 'RF': 'Random Forest - RF'}
    logger.info("Using {ml_model} to train and validate each stock price...".format(ml_model=ml_model_dict[ml_model]))
    rating = {}
    for symbol in watchlist_symbols:
        rating.update(stock_rating(login=login, symbol=symbol, ml_model=ml_model))

    rating_filter = {k: v for k, v in rating.items() if v[1] >= perf_threshold}
    rating_sorted = sorted(rating_filter.items(), key=lambda x: x[1][0], reverse=True)

    logger.info("Today's top {top} recommended stocks are: ".format(top=top))
    for i in rating_sorted[:top]:
        logger.info(
            "Symbol {symbol}: Rating {prob}% - Model Accuracy {accuracy}%".format(symbol=i[0],
                                                                                  prob=round(i[1][0] * 100, 2),
                                                                                  accuracy=round(i[1][1] * 100, 2)))

    return rating_sorted
