import os
import pickle

import numpy as np
import plotly.graph_objs as go
from dash import Input, Output, State, callback, dcc
from dash.exceptions import PreventUpdate
from joblib import load
from sklearn.linear_model import LinearRegression, LogisticRegression

from assets.layout_templates.main_page.common_css import (
    style_content_left,
    style_content_left2,
)
from assets.templates_plotly import template_visualizations
from utils.create_callback_hidden_button_cover import (
    create_callback_hidden_button_cover,
)

from ..common_css import *
from .test_models_button_functions import *

id_page = "test_models"

create_callback_hidden_button_cover(f"{id_page}_div_result")


@callback(
    Output(f"{id_page}_content_left", "style"),
    Input("main_page_button_cover", "n_clicks"),
    prevent_initial_call=True,
)
def auth_display(n_clicks):
    if n_clicks % 2 != 0:
        return style_content_left2
    return style_content_left


@callback(
    [
        Output(f"{id_page}_test_left", "options"),
        Output(f"{id_page}_test_left", "value"),
    ],
    Input("test_models_button", "n_clicks"),
    State("main_page_store", "data"),
)
def second_callback(n_clicks, data):
    try:
        path = f"""users/{data["user"]}/models/"""
        lista = os.listdir(path)
        return [lista, lista[0]]
    except:
        raise PreventUpdate


@callback(
    [
        Output(f"{id_page}_test_right", "options"),
        Output(f"{id_page}_test_right", "value"),
    ],
    Input(f"{id_page}_test_left", "value"),
    State("main_page_store", "data"),
)
def second_callback(type_model, data):
    try:
        path = f"""users/{data["user"]}/models/{type_model}"""
        lista = os.listdir(path)
        return [lista, lista[0]]
    except:
        raise PreventUpdate


@callback(
    [
        Output(f"{id_page}_div_result", "children"),
        Output(f"{id_page}_test_model_loading", "children"),
        Output(f"{id_page}_div_params", "children"),
    ],
    Input(f"{id_page}_test_right", "value"),
    [
        State(f"{id_page}_test_left", "value"),
        State("main_page_store", "data"),
    ],
    prevent_initial_call=True,
)
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
    fig = go.Figure(
        [
            go.Scatter(x=x_range_test[-100:], y=y_test[-100:], name="real"),
            go.Scatter(
                x=x_range_test[-100:],
                y=y_pred[-100:],
                name="predicción",
                mode="markers",
            ),
        ]
    )
    fig.update_layout(template=template_visualizations)
    obj_middle = dcc.Graph(figure=fig, style=style_graph)

    # content_down
    obj_down = ""

    if isinstance(model, LogisticRegression):
        obj_down = results_logistic_regresion(model, X_train, y_train, X_test, y_test)
    if isinstance(model, LinearRegression):
        obj_down = results_linear_regresion(model, X_train, y_train, X_test, y_test)
    return [obj_middle, "", obj_down]
