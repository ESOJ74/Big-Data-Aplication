import os
import pickle

import numpy as np
import plotly.graph_objs as go
from dash import Input, Output, State, callback, dcc, html
from dash.exceptions import PreventUpdate
from joblib import load

from assets.my_dash.my_html.my_div import my_div
from assets.templates_plotly import template_visualizations
from utils.create_callback_button_cover import create_callback_button_cover

from ..common_css import *
from .test_models_button_functions import pred_model

id_page = "test_models"

create_callback_button_cover(id_page, f"{id_page}_div_result")


@callback([
           Output(f"{id_page}_test_left", "options"), 
           Output(f"{id_page}_test_left", "value"),
          ],
          Input("test_models_button", "n_clicks"), 
          State('main_page_store', 'data'),
          )
def second_callback(n_clicks, data):    
    try:
        path = f"""users/{data["user"]}/models/"""
        lista = os.listdir(path)
        return [lista, lista[0]]
    except:
        raise PreventUpdate


@callback([
           Output(f"{id_page}_test_right", "options"), 
           Output(f"{id_page}_test_right", "value"),
          ],
          Input(f"{id_page}_test_left", "value"), 
          State('main_page_store', 'data'),
          )
def second_callback(type_model, data):  
    try:  
        path = f"""users/{data["user"]}/models/{type_model}"""
        lista = os.listdir(path)
        return [lista, lista[0]]
    except:
        raise PreventUpdate


@callback([
           Output(f"{id_page}_div_result", "children"),                 
           Output(f"{id_page}_test_model_loading", "children"), 
           Output(f"{id_page}_div_params", "children"),          
          ],
          Input(f"{id_page}_test_right", "value"),
          [
           State(f"{id_page}_test_left", "value"),
           State('main_page_store', 'data'),
          ],
          prevent_initial_call=True)
def display_page(model_name, type_model, data):    
         
    path = f"""users/{data["user"]}/models/{type_model}/{model_name}/"""                 
    model = load(f"{path}model.joblib")    
   
    with open(f"{path}X_train.pickle", "rb") as f:
        X_train = pickle.load(f)
    with open(f"{path}y_train.pickle", "rb") as f:
        y_train = pickle.load(f)  
    with open(f"{path}X_test.pickle", "rb") as f:
        X_test = pickle.load(f)
    with open(f"{path}y_test.pickle", "rb") as f:
        y_test = pickle.load(f)           

    y_pred = pred_model(model, X_test)

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
    obj_down = my_div(style_div_test_result, "",
                    [
                    html.P(f"Classes: {model.classes_}",
                            style=style_test_result),
                    html.P(f"Independent term: {[round(x,4) for x in model.intercept_]}",
                            style=style_test_result),
                    html.P(f"n_features_in: {model.n_features_in_}",
                            style=style_test_result),
                    html.P(f"n_iter_: {model.n_iter_}",
                            style=style_test_result),
                    html.P(f"Score train: {round(model.score(X_train, y_train),3)}",
                            style=style_test_result),
                    html.P(f"Score test: {round(model.score(X_test, y_test),3)}",
                            style=style_test_result),
                    ]
            )   
    return [obj_middle, "", obj_down]        