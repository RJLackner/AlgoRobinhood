from sklearn.ensemble import RandomForestClassifier


class RandomForestEstimator():

    def __init__(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def fit(self):
        rf = RandomForestClassifier(n_estimators=100, max_features=5, min_samples_leaf=0.01)
        rf_model = rf.fit(self.X_train, self.y_train)

        return rf_model
