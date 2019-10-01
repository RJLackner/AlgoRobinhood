# AlgoRobinhood

Algorithmic Trading System with Machine Learning

- An <strong>Algorithmic Trading System</strong> connecting to Robinhood to execute various algo trading strategies;
- Stocks <strong>Recommendation System</strong> based on <strong>Machine Learning</strong> Models


## Getting Started

These instructions will enable you to run an algo trading system on your local machine.

### Prerequisites

You need a [robinhood](https://robinhood.com/) account with a two factor code setup using your phone number. At the point of executing AlgoRobinhood, you will put the account id, password and the two-factor codes in terminal to login.

```
$ python AutoTrade.py

Enter your account id: abc@somemail.com
Do you want to run recommendation code (y/n): y
Enter your password: *****
Please Enter SMS Code: ******
2019-09-30 23:22:16,785 __main__ Successfully logged in account
2019-09-30 23:22:16,785 __main__ Running stocks recommendation for today...
2019-09-30 23:28:54,145 __main__ The code is outside execution period.
2019-09-30 23:28:54,202 __main__ Successfully logged out account.
```

### Installing

A step by step series of examples will be added

```
Example to be added
```

## Running the tests

Simply <em>git clone</em> this codebase and execute the below command. After successfully login in, a log file will be generated under <em>/log</em>, with detailed information like recommendations made from a tensorflow model predction, as well as buy/sell operations being executed if any.<br>

 <em><strong>python AutoTrade.py</strong></em>

```
Example of a log file

2019-09-30 23:22:04,500 __main__ Auto trading start at 2019-09-30 23:22:04
2019-09-30 23:22:04,500 __main__ The code is outside execution period.
2019-09-30 23:22:16,785 __main__ Successfully logged in account
2019-09-30 23:22:16,785 __main__ Running stocks recommendation for today...
2019-09-30 23:22:23,236 recommendation_system.recommendation Symbol SNAP is using LSTM training model and doing forecast...
2019-09-30 23:22:27,877 recommendation_system.recommendation Symbol SNAP is trained and validated with accuracy 60.27%, forecasted to price up by 5.0% over the 5 days with predicted probability of 24.43%
...
2019-09-30 23:28:40,817 recommendation_system.recommendation Symbol COF is using LSTM training model and doing forecast...
2019-09-30 23:28:54,144 recommendation_system.recommendation Symbol COF is trained and validated with accuracy 90.41%, forecasted to price up by 5.0% over the 5 days with predicted probability of 4.17%

2019-09-30 23:28:54,145 recommendation_system.recommendation Today's top 5 recommended stocks are: 
2019-09-30 23:28:54,145 recommendation_system.recommendation Symbol GE: Rating 53.47% - Model Accuracy 87.67%
2019-09-30 23:28:54,145 recommendation_system.recommendation Symbol NFLX: Rating 49.46% - Model Accuracy 86.3%
2019-09-30 23:28:54,145 recommendation_system.recommendation Symbol FIT: Rating 38.27% - Model Accuracy 82.19%
2019-09-30 23:28:54,145 recommendation_system.recommendation Symbol AMZN: Rating 29.51% - Model Accuracy 91.78%
2019-09-30 23:28:54,145 recommendation_system.recommendation Symbol PVTL: Rating 27.16% - Model Accuracy 80.82%
2019-09-30 23:28:54,145 __main__ The code is outside execution period.
2019-09-30 23:28:54,202 __main__ Successfully logged out account.

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

## Working in progress:

- Build Github page with more information in README.md - done on 20190929; <br>
- Optimize the data pipeline for modeling, and do codebase refactoring; - done on 20190930<br>
- add modeling class, which can be extented to RF and XGBoost; - done on 20190930<br>
- Extend machine leaning models by adding Xgboost and Random Forests to do forecast; - <strong>in progress</strong><br>
- Create Python package; <br>
- Build Web-based UI; <br>



