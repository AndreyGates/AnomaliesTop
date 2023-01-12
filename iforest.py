from sklearn.ensemble import IsolationForest
from sklearn.model_selection import GridSearchCV

import numpy as np
from joblib import dump


def scorer_f(estimator, X):   #your own scorer
    return np.mean(estimator.score_samples(X))

def isolation_forest(X):
    '''Fitting Isolation Forest GridSearchCV to find top anomalies'''

    param_grid = {'n_estimators': [100, 500], 
                  'max_samples': [500, 1000, 1500], 
                  'max_features': [15, 30], 
                  'bootstrap': [True, False], 
                  'n_jobs': [-1]}

    grid = GridSearchCV(IsolationForest(), param_grid, scoring=scorer_f, refit=True, verbose=5)
    grid.fit(X)

    estimator = grid.best_estimator_
    dump(estimator, "iforest.joblib") # saving the best estimator
    return estimator
