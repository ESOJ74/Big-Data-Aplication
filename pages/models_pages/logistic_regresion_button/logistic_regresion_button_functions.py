import numpy as np
from dash import dcc, html
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from my_dash.my_dbc.my_button import my_button
from my_dash.my_dcc.my_dropdown import my_dropdown
from my_dash.my_html.my_div import my_div
from pages.models_pages.logistic_regresion_button.logistic_regresion_button_css import *

id_page = "logistic_regresion"


def create_content_up(columns):
    return my_div({"width": "100%", "height": "100%"}, "",
                 [my_div({"position": "relative", "top": "2%", "width": "100%", "height": "7%"}, "",
                         [
                          my_div({"float": "left", "margin-left": "1%", "width": "22.5%", "height": "100%"}, "", html.H6("X")),
                          my_div({"float": "left", "width": "30%", "height": "100%"}, "", html.H6("Y")),
                         ]
                  ),
                  my_div(s_selector, "",
                         my_dropdown(f"{id_page}_dropdown_x",
                              {"color": "black"},
                              columns,
                              placeholder="Seleccione columna",
                              multi=True,
                         ),
                  ),
                  my_div(s_selector2, "",
                         my_dropdown(f"{id_page}_dropdown_y",
                              {"color": "black"},
                              placeholder="Seleccione columna"
                         ),
                  ),
                 ]
          )


def create_param_drop(id_param, options, value):
    return my_div({"width": "100%"}, "", 
                  [my_div({"float": "left", "width": "45%"}, "", id_param),
                   my_div({"float": "left", "width": "55%"}, "",
                          my_dropdown(f"{id_page}_{id_param}",
                                      {"width": "80%", "color": "black"},
                                      options=options,
                                      value=value,
                          ),
                   )                                           
                  ]
           )


def create_utils(id_page):
    return my_div(s_utils, "",
                 [
                   my_div(style_div_input, "", 
                          [html.H5("train_test_split", style={"margin-left": "2%", "color": "black"}),
                           my_div({"margin-left": "5%"}, "",
                                  [my_div({}, "", 
                                          ["test_size",
                                           dcc.Input(id=f"{id_page}_test_size",
                                                     style=style_dcc_input,
                                                     value=20,
                                           ),
                                          ]
                                  ),
                                  my_div({}, "", 
                                          ["random_state",
                                           dcc.Input(id=f"{id_page}_random_state",
                                                     style=style_dcc_input,
                                                     value=42,
                                           ),
                                          ]
                                  ),
                                  ]
                           ),  
                           html.H5("Model", style={"margin-top": "10%", "margin-left": "2%", "color": "black"}),  
                           my_div({"margin-left": "5%"}, "",
                                  [create_param_drop("penalty", ["l1", "l2", "elasticnet"], "l2"),
                                   create_param_drop("dual", ["True", "False"], "True"),
                                   my_div({}, "", 
                                          ["tol",
                                           dcc.Input(id=f"{id_page}_tol",
                                                     style=style_dcc_input2,
                                                     value=1e-4,
                                           ),
                                          ]
                                   ),
                                   my_div({}, "", 
                                          ["C",
                                           dcc.Input(id=f"{id_page}_c",
                                                     style=style_dcc_input,
                                                     value=1.0,
                                           ),
                                          ]
                                   ),
                                   create_param_drop("fit_intercept", ["True", "False"], "True"),
                                   my_div({}, "", 
                                          ["intercept_scaling",
                                           dcc.Input(id=f"{id_page}_intercept_scaling",
                                                     style=style_dcc_input,
                                                     value=1.0,
                                           ),
                                          ]
                                   ),
                                   my_div({}, "", 
                                          ["random_state",
                                           dcc.Input(id=f"{id_page}_random_state2",
                                                     style=style_dcc_input,
                                                     value=None,
                                           ),
                                          ]
                                   ),
                                   create_param_drop("solver", ["lbfgs", "liblinear", "newton-cg", "newton-cholesky", "sag", "saga"], "lbfgs"),
                                   my_div({}, "", 
                                          ["max_iter",
                                           dcc.Input(id=f"{id_page}_max_iter",
                                                     style=style_dcc_input2,
                                                     value=100,
                                           ),
                                          ]
                                   ),
                                   create_param_drop("multi_class", ["auto", "ovr", "multinomial"], "auto"),
                                   my_div({}, "", 
                                          ["verbose",
                                           dcc.Input(id=f"{id_page}_verbose",
                                                     style=style_dcc_input,
                                                     value=0,
                                           ),
                                          ]
                                   ),
                                   create_param_drop("warm_start", ["True", "False"], "False"),
                                   my_div({}, "", 
                                          ["n_jobs",
                                           dcc.Input(id=f"{id_page}_n_jobs",
                                                     style=style_dcc_input,
                                                     value=None,
                                           ),
                                          ]
                                   ),
                                   my_div({}, "", 
                                          ["l1_ratio",
                                           dcc.Input(id=f"{id_page}_l1_ratio",
                                                     style=style_dcc_input,
                                                     value=None,
                                           ),
                                          ]
                                   ),
                                  ]
                           ),
                           my_button(f"{id_page}_train", "Train", {"margin-top": "2%"}, className="btn btn-outline-light", color="black")
                          ]
                   ),                   
                 ]
          )     


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


def pred_model(model, X_test):
    return model.predict(X_test)
