import numpy as np
from dash import dcc, html
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

from my_dash.my_dbc.my_button import my_button
from my_dash.my_dcc.my_dropdown import my_dropdown
from my_dash.my_html.my_div import my_div
from pages.models_pages.linear_regresion_button.linear_regresion_button_css import *

id_page = "linear_regresion"


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


def create_param_drop(id_param, value):
    return my_div({"width": "100%"}, "", 
                  [my_div({"float": "left", "width": "45%"}, "", id_param),
                   my_div({"float": "left", "width": "55%"}, "",
                          my_dropdown(f"{id_page}_{id_param}",
                                      {"width": "80%", "color": "black"},
                                      ["True", "False"],
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
                                  [create_param_drop("fit_intercept", "True"),
                                   create_param_drop("copy_X", "True"),
                                   my_div({}, "", 
                                          ["n_jobs",
                                           dcc.Input(id=f"{id_page}_n_jobs",
                                                     style=style_dcc_input,
                                                     value=None,
                                           ),
                                          ]
                                   ),
                                   create_param_drop("positive", "False")
                                  ]
                           ),
                           my_button(f"{id_page}_train", "Train", {"margin-top": "2%"})
                          ]
                   ),                   
                 ]
          )     


def split_df(df, value_x, value_y, test_size, random_state):
    if len(value_x) == 1:       
        X = np.array(df[[value_x][0]])                     
    else:                       
        X = np.array(df[value_x])    
    return train_test_split(
        X, df[value_y].values, test_size=test_size, random_state=random_state)


def fit_model(X, y, fit_intercept, copy_X, n_jobs, positive):
    fit_int = True
    copy = True
    posit = False    

    if fit_int == "False": fit_int = False    
    if copy_X == "False": copy = False
    if n_jobs is not None: n_jobs = int(n_jobs)    
    if positive == "True": posit = True    

    # Creamos el objeto de Regresión Linear
    regr = LinearRegression(fit_intercept=fit_int, copy_X=copy, n_jobs=n_jobs, positive=posit)
    # Entrenamos nuestro modelo
    regr.fit(X, y)
    return regr


def pred_model(model, X_test):
    return model.predict(X_test)
