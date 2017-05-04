# -*- coding: utf-8 -*-
import numpy as np
import seaborn as sns
from math import sqrt
from sklearn import feature_selection, linear_model, metrics

def log_transform(df, cols):
    """
    This function log transforms and return the data
    """

    log_df = df.copy()
    log_df[cols] = log_df[cols].apply(np.log10)
    log_df = log_df.dropna()

    return log_df

def get_linear_model_metrics(X, y, algo):
    pvals = feature_selection.f_regression(X, y)[1]
    algo.fit(X,y)
    residuals = (y-algo.predict(X)).values

    # print the basic metrics
    print 'P Values:', pvals
    print 'Coefficients:', algo.coef_
    print 'y-intercept:', algo.intercept_
    print 'R-2:', algo.score(X,y)

    # print model fit metrics
    mse = metrics.mean_squared_error(y, algo.predict(X))
    rmse = sqrt(metrics.mean_squared_error(y, algo.predict(X)))
    #rsq = metrics.r2_score(y, lm.predict(X))
    print 'MSE:', mse
    print 'RMSE:', rmse
    #print 'R-Squared:', rsq

    # graph the result
    sns.distplot(residuals)

    # return model
    return algo
