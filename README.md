# AlgoRobinhood

Algorithmic Trading System with Machine Learning

- An <strong>Algorithmic Trading System</strong> connecting to Robinhood to execute various algo trading strategies
- Stocks <strong>Recommendation System</strong> based on <strong>Machine Learning</strong> Models


## Getting Started

These instructions will enable you to run an algo trading system on your local machine

### Prerequisites

You need a [robinhood](https://robinhood.com/) account with a two factor code setup using your phone number. At the point of executing AlgoRobinhood, you will put the account id, password and the two-factor codes in terminal to login

```
$ python AutoTrade.py

Enter your account id: abc@somemail.com
Do you want to run recommendation code (y/n): y
What recommendation model you want to use (LSTM/RF): LSTM
Enter your password: *****
Please Enter SMS Code: ******
2019-09-30 23:22:16,785 __main__ Successfully logged in account
2019-09-30 23:22:16,785 __main__ Running stocks recommendation for today...
...
2019-09-30 23:28:54,145 __main__ The code is outside execution period.
2019-09-30 23:28:54,202 __main__ Successfully logged out account.
```

### Installing

Make sure you have below python packages installed:

- tensorflow
- xgboost


Git clone the AlgoRobinhood codebase and you should be ready to go:

```
git clone https://github.com/ChrisZheng1985/AlgoRobinhood.git
```

## Running the AlgoRobinhood

Simply <em>git clone</em> this codebase and execute the below command. After successfully login in, a log file will be generated under <em>/log</em>, with detailed information like recommendations made from a tensorflow model predction, as well as buy/sell operations being executed if any<br>

 <em><strong>python AutoTrade.py</strong></em>

```
Example of a log file

2019-10-02 22:35:17,385 __main__ Auto trading start at 2019-10-02 22:35:17
2019-10-02 22:35:17,385 __main__ The code is outside execution period.
2019-10-02 22:35:31,913 __main__ Successfully logged in account
2019-10-02 22:35:31,914 __main__ Running stocks recommendation for today...
2019-10-02 22:35:38,262 recommendation_system.recommendation Using Random Forest - RF to train and validate each stock price...
2019-10-02 22:35:39,102 recommendation_system.recommendation Symbol SNAP model accuracy is 79.73%, with prob of 7.5% to go up by 5.0% over the next 5 days 
2019-10-02 22:35:39,412 recommendation_system.recommendation Symbol AAPL model accuracy is 89.19%, with prob of 5.99% to go up by 5.0% over the next 5 days 
...
2019-10-02 22:35:51,735 recommendation_system.recommendation Symbol UBER model accuracy is 93.24%, with prob of 16.7% to go up by 5.0% over the next 5 days 
2019-10-02 22:35:51,977 recommendation_system.recommendation Symbol COF model accuracy is 91.89%, with prob of 3.0% to go up by 5.0% over the next 5 days 

2019-10-02 22:35:51,977 recommendation_system.recommendation Today's top 5 recommended stocks are: 
2019-10-02 22:35:51,977 recommendation_system.recommendation Symbol FB: Rating 24.13% - Model Accuracy 94.59%
2019-10-02 22:35:51,977 recommendation_system.recommendation Symbol UBER: Rating 16.7% - Model Accuracy 93.24%
2019-10-02 22:35:51,977 recommendation_system.recommendation Symbol NFLX: Rating 15.93% - Model Accuracy 94.59%
2019-10-02 22:35:51,978 recommendation_system.recommendation Symbol SNE: Rating 13.67% - Model Accuracy 86.49%
2019-10-02 22:35:51,978 recommendation_system.recommendation Symbol TWTR: Rating 12.24% - Model Accuracy 82.43%
2019-10-02 22:35:51,978 __main__ The code is outside execution period.
2019-10-02 22:35:52,025 __main__ Successfully logged out account.

```

## Web-based Deployment

Example will be added about how to deploy this on a user-friendly web based system

```
Example to be added
```

## Built With

* [Python 3.6](https://www.anaconda.com/distribution/) - Codebase development and execution
* [Django](https://www.djangoproject.com/) - The web framework development

## Versioning

- Version 1.0

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Working in progress:

- Build Github page with more information in README.md - done on 20190929; <br>
- Optimize the data pipeline for modeling, and do codebase refactoring; - done on 20190930<br>
- add modeling class, which can be extented to RF and XGBoost; - done on 20190930<br>
- Extend machine leaning models by adding Random Forest to do forecast; - done on 20191001<br>
- Extend machine leaning models by adding XGboost to do forecast; - <strong>in progress</strong><br>
- Create Python package; <br>
- Build Web-based UI; <br>
- Build NLP on financial news, take it as additional features in ML models to enhance model performance; <br>



