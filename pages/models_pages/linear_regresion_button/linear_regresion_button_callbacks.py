import numpy as np
import plotly.graph_objs as go
from dash import callback, dcc, html
from dash.dependencies import Input, Output, State
from pandas import read_json
from sklearn.metrics import mean_squared_error, r2_score

from assets.templates import template_visualizations
from common_functions.create_callback_button_cover import \
    create_callback_button_cover
from my_dash.my_html.my_div import my_div
from pages.models_pages.linear_regresion_button.linear_regresion_button_functions import (
    create_content_up, fit_model, pred_model, split_df)

id_page = "linear_regresion"


# Panel content_up
@callback(Output(f"{id_page}_content_up", "children"),
          Input("linear_regresion_button", "n_clicks"),
          State('main_page_store', 'data'),
          prevent_initial_call=True)
def content_up(n_clicks, data):   
    return create_content_up(read_json(data["df"]).columns)


# options dropdown y
@callback(Output(f"{id_page}_dropdown_y", "options"),
          Input(f"{id_page}_dropdown_x", "value"),
          State('main_page_store', 'data'))
def display_page(values, data):
    cols = []
    if values is not None:
        cols = list(read_json(data["df"]).columns)
        for value in values:
            cols.remove(value)    
    return cols


# Panel content_down
@callback([
           Output(f"{id_page}_content_middle", "children"),
           Output(f"{id_page}_content_down", "children"),
           Output(f"{id_page}_model_loading", "children")
          ],
          Input(f"{id_page}_train", "n_clicks"),
          [
           State(f"{id_page}_dropdown_x", "value"),
           State(f"{id_page}_dropdown_y", "value"),                            
           State('main_page_store', 'data'),
           State(f"{id_page}_test_size", "value"),
           State(f"{id_page}_random_state", "value"),
           State(f"{id_page}_fit_intercept", "value"),
           State(f"{id_page}_copy_X", "value"),
           State(f"{id_page}_n_jobs", "value"),
           State(f"{id_page}_positive", "value")
          ],
          prevent_initial_call=True)
def display_page(n_clicks, value_x, value_y, data, test_size, random_state, fit_intercept, copy_X, n_jobs, positive):     
    
    try:
        # train_test_split
        X_train, X_test, y_train, y_test = split_df(read_json(data["df"]),
                                                    value_x, value_y, int(test_size)/100, int(random_state))               
        # Entrenamos modelo
        regr = fit_model(X_train, y_train, fit_intercept, copy_X, n_jobs, positive)

        # Hacemos las predicciones
        y_pred = pred_model(regr, X_test)
        
        # content_middle             
        x_range_test = np.linspace(0, X_test.shape[0], X_test.shape[0]) 

        fig = go.Figure([
            go.Scatter(x=x_range_test, y=y_test, 
                       name='real'),
            go.Scatter(x=x_range_test, y=y_pred, 
                       name='predicción', mode='markers', ),            
        ])    
        fig.update_layout(template=template_visualizations, height=550)
        obj_middle = dcc.Graph(figure=fig)

        # content_down
        obj_down = my_div({}, "",
                          [html.H6(f"Coefficients: {list(map(lambda x: round(x, 2), regr.coef_))}",
                                   style={"color": "#acf4ed"}),
                           html.H6(f"Independent term: {round(regr.intercept_, 2)}",
                                   style={"color": "#acf4ed"}),
                           html.H6(f"Mean squared error: {round(mean_squared_error(y_test, y_pred), 2)}",
                                   style={"color": "#acf4ed"}),
                           html.H6(f"Variance score: {round(r2_score(y_test, y_pred), 2)}",
                                   style={"color": "#acf4ed"}),
                          ]
                   )
    except (KeyError, ValueError):
        obj_down = ""
        obj_middle = html.H6("Ambas columnas deben ser numéricas",
                             style={"color": "#acf4ed"})
    return [obj_middle, obj_down, ""]


create_callback_button_cover(id_page, f"{id_page}_content_middle")