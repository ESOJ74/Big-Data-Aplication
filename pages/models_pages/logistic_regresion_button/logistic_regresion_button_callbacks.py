import os
import pickle

import numpy as np
import plotly.graph_objs as go
from dash import callback, dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from joblib import dump, load
from pandas import read_json

from assets.common_css import *
from assets.my_dash.my_html.my_div import my_div
from assets.templates_plotly import template_visualizations
from common_functions.create_callback_button_cover import \
    create_callback_button_cover
from pages.models_pages.logistic_regresion_button.logistic_regresion_button_functions import (
    create_content_up, fit_model, pred_model, split_df)

id_page = "logistic_regresion"


# Panel content_up
@callback(Output(f"{id_page}_content_up", "children"),
          Input("linear_regresion_button", "n_clicks"),
          State('main_page_store', 'data'))
def display_page(n_clicks, data):   
    return [create_content_up(read_json(data["df"]).columns)]


# Panel content_middle
@callback([
           Output(f"{id_page}_content_middle", "children", allow_duplicate=True),           
           Output(f"{id_page}_model_loading", "children", allow_duplicate=True),      
           Output(f"{id_page}_content_down", "children"),     
          ],
          Input(f"{id_page}_train", "n_clicks"),
          [
           State(f"{id_page}_model_name", "value"),
           State(f"{id_page}_dropdown_x", "value"),                          
           State('main_page_store', 'data'),
           State(f"{id_page}_test_size", "value"),
           State(f"{id_page}_random_state", "value"),
           State(f"{id_page}_penalty", "value"),
           State(f"{id_page}_dual", "value"),
           State(f"{id_page}_tol", "value"),
           State(f"{id_page}_c", "value"),
           State(f"{id_page}_fit_intercept", "value"),
           State(f"{id_page}_intercept_scaling", "value"),
           State(f"{id_page}_random_state2", "value"),
           State(f"{id_page}_solver", "value"),
           State(f"{id_page}_max_iter", "value"),
           State(f"{id_page}_multi_class", "value"),
           State(f"{id_page}_verbose", "value"),
           State(f"{id_page}_warm_start", "value"),           
           State(f"{id_page}_n_jobs", "value"),
           State(f"{id_page}_l1_ratio", "value")
          ],
          prevent_initial_call=True)
def display_page(n_clicks, model_name, value_y, data, test_size, random_state, penalty, dual, tol, c,
                 fit_intercept, intercept_scaling, random_state2, solver, max_iter,
                 multi_class, verbose, warm_start, n_jobs, l1_ratio):     
    
    if n_clicks:
        if model_name and len(model_name) > 0:
            value_x = list(read_json(data["df"]).columns)        
            value_x.remove(value_y) 
            
            try:         
                # train_test_split        
                X_train, X_test, y_train, y_test = split_df(read_json(data["df"]),
                                                            value_x, value_y, int(test_size)/100, int(random_state))          
                # Entrenamos modelo            
                regr = fit_model(X_train, y_train, penalty, dual, tol, c,fit_intercept, intercept_scaling,
                                random_state2, solver, max_iter,multi_class, verbose, warm_start, n_jobs,
                                l1_ratio)          
                obj_middle = html.H6("Modelo Entrenado y guardado", style={"color": "#b0d8d3"})

                path = f"""users/{data["user"]}/models/logistic_regresion/{model_name}"""   
                try:
                    os.stat(path)
                except:
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
                
            except (KeyError, ValueError):        
                obj_middle = html.H6("Todas las columnas deben ser numéricas", style={"color": "#b0d8d3"})
        else:
            obj_middle = html.H6("Introduzca un nombre para el modelo", style={"color": "#b0d8d3"})
    else:
        raise PreventUpdate
    return [obj_middle, "", ""]


@callback([
           Output(f"{id_page}_content_middle", "children", allow_duplicate=True),   
           Output(f"{id_page}_content_down", "children", allow_duplicate=True),    
           Output(f"{id_page}_model_loading", "children", allow_duplicate=True),           
          ],
          Input(f"{id_page}_test", "n_clicks"),
          [
           State(f"{id_page}_model_name", "value"),
           State('main_page_store', 'data')
          ],
          prevent_initial_call=True)
def display_page(n_clicks, model_name, data):
    if n_clicks:
        obj_down = ""
        if model_name and len(model_name) > 0:            
            try:
                path = f"""users/{data["user"]}/models/logistic_regresion/{model_name}/"""                 
                regr = load(f"{path}model.joblib")
                
                with open(f"{path}X_train.pickle", "rb") as f:
                    X_train = pickle.load(f)
                with open(f"{path}y_train.pickle", "rb") as f:
                    y_train = pickle.load(f)  
                with open(f"{path}X_test.pickle", "rb") as f:
                    X_test = pickle.load(f)
                with open(f"{path}y_test.pickle", "rb") as f:
                    y_test = pickle.load(f)               

                y_pred = pred_model(regr, X_test)
        
                # content_middle      
                x_range_test = np.linspace(0, X_test.shape[0], X_test.shape[0]) 
                fig = go.Figure([
                    go.Scatter(x=x_range_test[-100:], y=y_test[-100:], 
                            name='real'),
                    go.Scatter(x=x_range_test[-100:], y=y_pred[-100:], 
                            name='predicción', mode='markers'),            
                ])    
                fig.update_layout(template=template_visualizations, height=550)
                obj_middle = dcc.Graph(figure=fig)

                # content_down
                obj_down = my_div({}, "",
                                [
                                html.H6(f"Classes: {regr.classes_}",
                                        style={"color": color_boton_1}),
                                html.H6(f"Independent term: {regr.intercept_}",
                                        style={"color": color_boton_1}),
                                html.H6(f"n_features_in: {regr.n_features_in_}",
                                        style={"color": color_boton_1}),
                                html.H6(f"n_iter_: {regr.n_iter_}",
                                        style={"color": color_boton_1}),
                                html.H6(f"Score train: {regr.score(X_train, y_train)}",
                                        style={"color": color_boton_1}),
                                html.H6(f"Score test: {regr.score(X_test, y_test)}",
                                        style={"color": color_boton_1}),
                                ]
                        ) 
               
            except FileNotFoundError:
                obj_middle = html.H6("Modelo no encontrado", style={"color": "#b0d8d3"})
        else:
            obj_middle = html.H6("Introduzca un nombre para el modelo", style={"color": "#b0d8d3"})
    else:
        raise PreventUpdate
    return [obj_middle, obj_down, ""]         


create_callback_button_cover(id_page, f"{id_page}_content_middle")
