from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from assets.common_css import *

id_page = "logistic_regresion"



def split_df(df, value_x, value_y, test_size, random_state):    
    return train_test_split(
        df[value_x].values, df[value_y].values, test_size=test_size, random_state=random_state)


def fit_model(X, y, penalty, dual, tol, c,
                 fit_intercept, intercept_scaling, random_state, solver, max_iter,
                 multi_class, verbose, warm_start, n_jobs, l1_ratio):
    
    dual = False    
    fit_intercept = True
    warm_start = False

    if dual == "True": dual = True   
    if fit_intercept == "False": fit_intercept = False
    if warm_start == "True": warm_start = True
    if tol is not None: tol = float(tol)
    if c is not None: c = float(c)
    if intercept_scaling is not None: intercept_scaling = int(intercept_scaling) 
    if random_state is not None: random_state = int(random_state)
    if max_iter is not None: max_iter = int(max_iter)
    if verbose is not None: verbose = int(verbose)
    if n_jobs is not None: n_jobs = int(n_jobs)    
    if l1_ratio is not None: l1_ratio = int(l1_ratio) 

    # Creamos el objeto de Regresión Linear
    regr = LogisticRegression(penalty=penalty, dual=dual, tol=tol, C=c, 
                              fit_intercept=fit_intercept, intercept_scaling=intercept_scaling,
                              random_state=random_state, solver=solver, max_iter=max_iter,
                              multi_class=multi_class, verbose=verbose, warm_start=warm_start,
                              n_jobs=n_jobs, l1_ratio=l1_ratio)
    regr.fit(X, y)
    return regr