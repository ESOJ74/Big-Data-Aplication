from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from assets.common_css import *

id_page = "logistic_regresion"


def split_df(df, value_x, value_y, test_size, random_state):    
    return train_test_split(
        df[value_x].values, df[value_y].values, test_size=test_size,
        random_state=random_state)


def fit_model(X, y, fit_intercept, copy_X, n_jobs, positive):    
         
    fit_intercept = False if fit_intercept == "False"  else True
    copy_X = False if copy_X == "False"  else True
    positive = False if positive == "False"  else True    
    if n_jobs is not None: n_jobs = int(n_jobs)

    # Creamos el objeto de Regresión Linear
    regr = LinearRegression(fit_intercept=fit_intercept, copy_X=copy_X,
                              n_jobs=n_jobs, positive=positive)
    regr.fit(X, y)
    return regr