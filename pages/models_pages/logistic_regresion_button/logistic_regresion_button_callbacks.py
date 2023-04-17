import numpy as np
import plotly.express as px
import plotly.graph_objs as go
from dash import callback, dcc, html
from dash.dependencies import Input, Output, State
from pandas import DataFrame, read_json
from sklearn.metrics import mean_squared_error, r2_score

from my_dash.my_html.my_div import my_div
from pages.models_pages.logistic_regresion_button.logistic_regresion_button_functions import (
    create_content_up, fit_model, pred_model, split_df)

id_page = "logistic_regresion"


# Panel content_up
@callback(Output(f"{id_page}_content_up", "children"),
          Input("linear_regresion_button", "n_clicks"),
          State('main_page_store', 'data'),)
def display_page(n_clicks, data):   
    return create_content_up(read_json(data["df"]).columns)


# options dropdown y
@callback(Output(f"{id_page}_dropdown_y", "options"),
          Input(f"{id_page}_dropdown_x", "value"),
          State('main_page_store', 'data'),
          prevent_initial_call=True)
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
          ],
          Input(f"{id_page}_train", "n_clicks"),
          [
           State(f"{id_page}_dropdown_x", "value"),
           State(f"{id_page}_dropdown_y", "value"),                            
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
def display_page(n_clicks, value_x, value_y, data, test_size, random_state, penalty, dual, tol, c,
                 fit_intercept, intercept_scaling, random_state2, solver, max_iter,
                 multi_class, verbose, warm_start, n_jobs, l1_ratio):     
    
    try:                
        # train_test_split        
        X_train, X_test, y_train, y_test = split_df(read_json(data["df"]),
                                                    value_x, value_y, int(test_size)/100, int(random_state))          
        # Entrenamos modelo            
        regr = fit_model(X_train, y_train, penalty, dual, tol, c,fit_intercept, intercept_scaling,
                         random_state2, solver, max_iter,multi_class, verbose, warm_start, n_jobs,
                         l1_ratio)
        
        # Hacemos las predicciones
        y_pred = pred_model(regr, X_test)
        
        # content_middle        
        data = DataFrame({value_x[0]: list(map(lambda x: x[0], X_test)), 
                        value_x[1]: list(map(lambda x: x[1], X_test)), 
                        value_y: y_test})    
         
        x1_range = np.linspace(-3, 3, 50)
        x2_range = np.linspace(-3, 3, 50)

        #fig = px.scatter(df, x=value_x[0], y=value_x[1], color=value_y)        

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data[value_x[0]], y=data[value_x[1]], mode='markers', marker=dict(color=data[value_y], colorscale='RdBu')))
        fig.add_trace(go.Contour(x=x1_range, y=x2_range, z=y_pred, 
                          colorscale='RdBu', contours=dict(start=0.5, end=0.5), 
                          line_width=2))

        obj_middle = dcc.Graph(figure=fig)

        # content_down
        obj_down = my_div({}, "",
                          [html.H6(f"Classes: {regr.classes_}"),
                           html.H6(f"Independent term: {regr.intercept_}"),
                           html.H6(f"n_features_in: {regr.n_features_in_}"),
                           html.H6(f"n_iter_: {regr.n_iter_}"),
                           html.H6(f"Score train: {regr.score(X_train, y_train)}"),
                           html.H6(f"Score test: {regr.score(X_test, y_test)}"),
                          ]
                   )     
    except (KeyError, ValueError):
        obj_down = ""
        obj_middle = html.H6("Ambas columnas deben ser numéricas")
    return [obj_middle, obj_down]

