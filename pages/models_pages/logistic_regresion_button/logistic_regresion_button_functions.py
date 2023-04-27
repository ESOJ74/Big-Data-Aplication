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
    return my_div(style_div_selectors, "",
                  [
                   my_div(style_div_dropdown, "",
                          [my_div(style_div_target, "",
                                  html.H6("Target", style={"color": "#acf4ed"})
                           ),                  
                           my_div(style_selector, "",
                                  my_dropdown(f"{id_page}_dropdown_x",
                                              {"background": "radial-gradient(circle farthest-side at bottom left, #6da9d8 0%, #204765 50%, #04212c 95%)"},
                                              columns,
                                              value=columns[-1]
                                  ),
                           ),
                          ]
                   ),
                   my_div(style_div_model_name, "",
                          [
                           html.H6("Nombre Modelo", style=style_params_model_name),
                           dcc.Input(id=f"{id_page}_model_name",
                                     style=style_input_model_name,
                           )
                          ]
                   ),
                   my_div(style_div_buttons, "",
                          [
                           my_button(f"{id_page}_train", "Train", style_button,
                             className="btn btn-outline-warning", color="black"),
                           my_button(f"{id_page}_test", "Test", style_button,
                             className="btn btn-outline-warning", color="black"),
        
                          ]),
                  ]
           )


def create_param_drop(id_param, options, value):
    return my_div(style_div_color, "", 
                  [
                   html.H6(id_param, style=style_params),
                   my_div(style_selector_color, "",
                          my_dropdown(f"{id_page}_{id_param}",{"background": "radial-gradient(circle farthest-side at top left, #00c8ff 0%, #00fff9 80%)"},
                                      options=options,
                                      value=value,
                          ),
                   )                                           
                  ]
           )


def create_utils(id_page):
    return my_div(style_div_utils, "",
                  [
                   html.H5("train_test_split", style={"margin-left": "2%", "color": "black"}),
                   my_div(style_div_input, "",  
                          [
                           html.H6("test_size", style=style_params),
                           dcc.Input(id=f"{id_page}_test_size",
                                     style=style_input,
                                     value=20,
                           )
                          ]
                   ),
                   my_div(style_div_input, "",  
                          [
                           html.H6("random_state", style=style_params),
                           dcc.Input(id=f"{id_page}_random_state",
                                     style=style_input,
                                     value=42,
                           )
                          ]
                   ),       
                   html.H5("Model", style={"margin-top": "0%", "margin-left": "2%", "color": "black"}),  
                   create_param_drop("penalty", ["l1", "l2", "elasticnet"], "l2"),
                   create_param_drop("dual", ["True", "False"], "True"),
                   my_div(style_div_input, "",  
                          [
                           html.H6("tol", style=style_params),
                           dcc.Input(id=f"{id_page}_tol",
                                     style=style_input,
                                     value=1e-4,
                           ),
                           my_div({"float":"left", "margin-left": "10%"}, "", html.H6(" ", style=style_params),),
                           html.H6("c", style=style_params),
                           dcc.Input(id=f"{id_page}_c",
                                     style=style_input,
                                     value=1.0,
                           )
                          ]
                   ), 
                    
                   create_param_drop("fit_intercept", ["True", "False"], "True"),
                   my_div(style_div_input, "",  
                          [
                           html.H6("intercept_scaling", style=style_params),
                           dcc.Input(id=f"{id_page}_intercept_scaling",
                                     style=style_input,
                                     value=1.0,
                           )
                          ]
                   ), 
                   my_div(style_div_input, "",  
                          [
                           html.H6("random_state", style=style_params),
                           dcc.Input(id=f"{id_page}_random_state2",
                                     style=style_input,
                                     value=None,
                           )
                          ]
                   ),
                   create_param_drop("solver", ["lbfgs", "liblinear", "newton-cg", "newton-cholesky", "sag", "saga"], "lbfgs"),
                   my_div(style_div_input, "",  
                          [
                           html.H6("max_iter", style=style_params),
                           dcc.Input(id=f"{id_page}_max_iter",
                                     style=style_input,
                                     value=100,
                           ),
                           my_div({"float":"left", "margin-left": "5%"}, "", html.H6(" ", style=style_params),),
                           html.H6("l1_ratio", style=style_params),
                           dcc.Input(id=f"{id_page}_l1_ratio",
                                     style=style_input,
                                     value=None,                     
                           )
                          ]
                   ),
                   create_param_drop("multi_class", ["auto", "ovr", "multinomial"], "auto"),
                   my_div(style_div_input, "",  
                          [
                           html.H6("verbose", style=style_params),
                           dcc.Input(id=f"{id_page}_verbose",
                                     style=style_input,
                                     value=0,
                           ),
                           my_div({"float":"left", "margin-left": "10%"}, "", html.H6(" ", style=style_params),),
                           html.H6("n_jobs", style=style_params),
                           dcc.Input(id=f"{id_page}_n_jobs",
                                     style=style_input,
                                     value=None,
                           )
                          ]
                   ),
                   create_param_drop("warm_start", ["True", "False"], "False"), 
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
