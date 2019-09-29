# AlgoRobinhood

Algorithmic Trading System with Machine Learning

- An <strong>Algorithmic Trading System</strong> connecting to Robinhood to execute various algo trading strategies;
- Stocks <strong>Recommendation System</strong> based on <strong>Machine Learning</strong> Models


## Getting Started

These instructions will enable you to run an algo trading system on your local machine.

### Prerequisites

You need a [robinhood](https://robinhood.com/) account with a two factor code setup using your phone number. At the point of executing AlgoRobinhood, you will put the user_id, password and the two-factor codes in terminal to login.

```
$ python AutoTrade.py

Enter your account id: abc@somemail.com
Enter your password: *****
No 2FA Given
SMS Code:
123456
2019-09-29 18:09:45,131 __main__ Successfully logged in account
```

### Installing

A step by step series of examples will be added

```
Example to be added
```

## Running the tests

Simply <em>git clone</em> this codebase and execute the below command. After sucessfully login in, a log file will be generated under <em>/log</em>, with detailed information like recommendations made from a tensorflow model predction, as well as buy/sell operations being executed if any.<br>

 <em>python <strong>AutoTrade.py</strong></em>

```
Example of a log file

2019-09-29 18:09:33,282 __main__ Auto trading start at 2019-09-29 18:09:33
2019-09-29 18:09:33,283 __main__ The code is outside execution period.
2019-09-29 18:09:45,131 __main__ Successfully logged in account
2019-09-29 18:09:45,131 __main__ Running stocks recommendation for today...
2019-09-29 18:09:51,004 strategy.buy_stock_recommendation_rating Symbol SNAP is using LSTM training model and doing forecast...
2019-09-29 18:09:57,406 strategy.buy_stock_recommendation_rating Symbol SNAP is trained and validated with accuracy 61.11%, forecasted to price up by 5.0% over the 5 days with predicted probability of 39.66%
2019-09-29 18:09:57,406 strategy.buy_stock_recommendation_rating Symbol AAPL is using LSTM training model and doing forecast...
...
2019-09-29 18:16:08,795 strategy.buy_stock_recommendation_rating Symbol UBER is trained and validated with accuracy 94.44%, forecasted to price up by 5.0% over the 5 days with predicted probability of 1.69%
2019-09-29 18:16:08,797 strategy.buy_stock_recommendation_rating Symbol COF is using LSTM training model and doing forecast...
2019-09-29 18:16:20,070 strategy.buy_stock_recommendation_rating Symbol COF is trained and validated with accuracy 87.5%, forecasted to price up by 5.0% over the 5 days with predicted probability of 5.6%
2019-09-29 18:16:20,071 strategy.buy_stock_recommendation_rating Today's top 5 recommended stocks are: 
2019-09-29 18:16:20,072 strategy.buy_stock_recommendation_rating Symbol GE: Rating 54.03% - Model Accuracy 81.94%
2019-09-29 18:16:20,072 strategy.buy_stock_recommendation_rating Symbol NFLX: Rating 51.26% - Model Accuracy 90.28%
2019-09-29 18:16:20,072 strategy.buy_stock_recommendation_rating Symbol AMZN: Rating 44.12% - Model Accuracy 90.28%
2019-09-29 18:16:20,072 strategy.buy_stock_recommendation_rating Symbol DBX: Rating 36.58% - Model Accuracy 91.67%
2019-09-29 18:16:20,072 strategy.buy_stock_recommendation_rating Symbol PVTL: Rating 33.95% - Model Accuracy 80.56%
2019-09-29 18:16:20,072 __main__ The code is outside execution period.
2019-09-29 18:16:20,131 __main__ Successfully logged out account.


```

## Web-based Deployment

Example will be added about how to deploy this on a user-friendly web based system

```
Example to be added
```

## Built With

* [Python 3.7](https://www.anaconda.com/distribution/) - Codebase development and execution
* [Django](https://www.djangoproject.com/) - The web framework development

## Versioning

- Version 1.0

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

### Working in progress:

- Update Github page with more information in README.md - <strong>in progress</strong>; <br>
- Refactor code base, especially optimizing the data pipeline for modeling; <br>
- Extend machine leaning models by adding Xgboost and Random Forests to do forecast; <br>
- Create Python package; <br>
- Build Web-based UI; <br>



