import os
import pickle

import numpy as np
import plotly.graph_objs as go
from dash import Input, Output, State, callback, dcc
from dash.exceptions import PreventUpdate
from joblib import load
from sklearn.linear_model import LinearRegression, LogisticRegression

# sourcery skip: dont-import-test-modules
from utils.test_models_button_functions import (
    results_linear_regresion,
    results_logistic_regresion,
)

id_page = "test_models"


@callback(
    [
        Output(f"{id_page}_test_left", "options"),
        Output(f"{id_page}_test_left", "value"),
    ],
    Input("testmodels", "n_clicks"),
    State("main_page_store", "data"),
)
def button_testmodels(n_clicks, data):
    try:
        path = f"""users/{data["user"]}/models/"""
        lista = os.listdir(path)
        return [lista, lista[0]]
    except Exception as e:
        raise PreventUpdate from e


@callback(
    [
        Output(f"{id_page}_test_right", "options"),
        Output(f"{id_page}_test_right", "value"),
    ],
    Input(f"{id_page}_test_left", "value"),
    State("main_page_store", "data"),
)
def drop_left(type_model, data):
    try:
        path = f"""users/{data["user"]}/models/{type_model}"""
        lista = os.listdir(path)
        return [lista, lista[0]]
    except Exception as e:
        raise PreventUpdate from e


@callback(
    [
        Output(f"{id_page}_div_result", "children"),
        Output("loading", "children"),
        Output(f"{id_page}_div_params", "children"),
    ],
    Input(f"{id_page}_test_right", "value"),
    [
        State(f"{id_page}_test_left", "value"),
        State("main_page_store", "data"),
    ],
    prevent_initial_call=True,
)
def drop_right(model_name, type_model, data):
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

    y_pred = model.predict(X_test)  # pred_model(model, X_test)

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
    # fig.update_layout(template=template_visualizations)
    obj_middle = dcc.Graph(figure=fig)

    # content_down
    obj_down = ""

    if isinstance(model, LogisticRegression):
        obj_down = results_logistic_regresion(model, X_train, y_train, X_test, y_test)
    if isinstance(model, LinearRegression):
        obj_down = results_linear_regresion(model, X_train, y_train, X_test, y_test)

    return [obj_middle, "", obj_down]
