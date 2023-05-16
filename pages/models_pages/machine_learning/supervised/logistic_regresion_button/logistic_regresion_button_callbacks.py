import os
import pickle
from datetime import datetime

from dash import Input, Output, State, callback, html
from dash.exceptions import PreventUpdate
from joblib import dump
from pandas import read_json

from assets.my_dash.my_html.my_div import my_div
from utils.create_callback_hidden_button_cover import create_callback_hidden_button_cover

from ....common_css import *
from .logistic_regresion_button_functions import fit_model, split_df

id_page = "logistic"

create_callback_hidden_button_cover(f"{id_page}_content_up", True)


@callback(Output(f"{id_page}_content_up", "children"), 
          Input("logistic_regresion_button", "n_clicks"), 
          prevent_initial_call=True,)
def second_callback(n_clicks):    
    return my_div(style_div_title, "",
                  [
                   html.H5("sklearn.linear_model.LogisticRegression()",
                           style=style_title),
                   html.A("Documentacion",
                          href="https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html",
                          target="_blank")
                  ])


@callback([
           Output(f"{id_page}_target", "options"), 
           Output(f"{id_page}_target", "value"),
          ],
          Input(f"logistic_regresion_button", "n_clicks"), 
          State('main_page_store', 'data'),
          prevent_initial_call=True,)
def second_callback(n_clicks, data):
    df = read_json(data["df"])[:1]
    columns = [c for c in df.columns
               if "int" not in str(df[c].dtype)
               and "float" not in str(df[c].dtype)]    
    if len(columns) > 0:
        return [columns, columns[0]]  
    else:
        return [df.columns, df.columns[0]]


@callback([
           Output(f"{id_page}_div_result", "children"),           
           Output(f"{id_page}_model_loading", "children"), 
          ],
          Input(f"{id_page}_button_start", "n_clicks"),
          [             
           State(f"{id_page}_target", "options"),          
           State(f"{id_page}_target", "value"), 
           State('main_page_store', 'data'),
           State(f"{id_page}_test_size", "value"),
           State(f"{id_page}_random_state_split", "value"),
           State(f"{id_page}_penalty", "value"),
           State(f"{id_page}_dual", "value"),
           State(f"{id_page}_tol", "value"),
           State(f"{id_page}_c", "value"),
           State(f"{id_page}_fit_intercept", "value"),
           State(f"{id_page}_intercept_scaling", "value"),
           State(f"{id_page}_random_state", "value"),
           State(f"{id_page}_solver", "value"),
           State(f"{id_page}_max_iter", "value"),
           State(f"{id_page}_multi_class", "value"),
           State(f"{id_page}_verbose", "value"),
           State(f"{id_page}_warm_start", "value"),           
           State(f"{id_page}_n_jobs", "value"),
           State(f"{id_page}_l1_ratio", "value")
          ],
          prevent_initial_call=True)
def display_page(n_clicks, options_y, value_y, data, test_size,
                 random_state, penalty, dual, tol, c, fit_intercept,
                 intercept_scaling, random_state2, solver, max_iter,
                 multi_class, verbose, warm_start, n_jobs, l1_ratio):     

    if n_clicks:      
  
        df = read_json(data["df"])
        value_x = [x for x in df.columns if x not in options_y]          

        if len(value_x) == 0:
            value_x = list(df.columns)
            value_x.remove(value_y)

        try:         
            # train_test_split        
            X_train, X_test, y_train, y_test =\
                  split_df(df, value_x, value_y,
                           int(test_size)/100, int(random_state))  
                 
            # Entrenamos modelo            
            regr = fit_model(X_train, y_train, penalty, dual, tol,
                             c,fit_intercept, intercept_scaling,
                            random_state2, solver, max_iter,multi_class,
                            verbose, warm_start, n_jobs, l1_ratio)  

            date_model = str(datetime.now()).split('.')[0]
                    
            obj_middle = html.H6(f"""Modelo Entrenado.
                                 Guardado como {value_y}_{date_model}""",
                                 style={"color": color_boton_1})

            # Guardamos Modelo
            path = f"""users/{data["user"]}/models/logistic_regresion"""   
            try:
                os.stat(path)
            except:
                os.makedirs(path)     
            path = path + f"/{value_y}_{date_model}"    
            os.makedirs(path)
            dump(regr, f"{path}/model.joblib")              
                                      
            with open(f"{path}/X_train.pickle", "wb") as f:
                pickle.dump(X_train, f)
            with open(f"{path}/y_train.pickle", "wb") as f:
                pickle.dump(y_train, f)
            with open(f"{path}/X_test.pickle", "wb") as f:
                pickle.dump(X_test, f)
            with open(f"{path}/y_test.pickle", "wb") as f:
                pickle.dump(y_test, f)           
        except (KeyError, ValueError) as err:        
            obj_middle = html.H6(err.__str__(),
                                 style={"color": color_boton_1})

        return [obj_middle, ""]
    else:
        raise PreventUpdate
    

