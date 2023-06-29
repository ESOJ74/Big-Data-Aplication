import os
import pickle
from datetime import datetime

from dash import Input, Output, State, callback
from dash.exceptions import PreventUpdate
from joblib import dump
from pandas import read_json
from sklearn.linear_model import LinearRegression

from utils.split_df import split_df
from utils.utils_functions import create_msg

id_page = "LinearRegression"


def fit_model(X, y, fit_intercept, copy_X, n_jobs, positive):
    fit_intercept = fit_intercept != "False"
    copy_X = copy_X != "False"
    positive = positive != "False"
    if n_jobs is not None:
        n_jobs = int(n_jobs)

    # Creamos el objeto de Regresión Linear
    regr = LinearRegression(
        fit_intercept=fit_intercept, copy_X=copy_X, n_jobs=n_jobs, positive=positive
    )
    regr.fit(X, y)
    return regr


@callback(
    [
        Output(f"{id_page}_target", "options"),
        Output(f"{id_page}_target", "value"),
    ],
    Input("linearregresion", "n_clicks"),
    State("main_page_store", "data"),
    prevent_initial_call=True,
)
def second_callback(n_clicks, data):
    df = read_json(data["df"])[:1]
    if columns := [
        c
        for c in df.columns
        if "int" not in str(df[c].dtype) and "float" not in str(df[c].dtype)
    ]:
        return [columns, columns[0]]
    else:
        return [df.columns, df.columns[0]]


@callback(
    [
        Output(f"{id_page}_div_result", "children"),
        Output("loading", "children", allow_duplicate=True),
    ],
    Input(f"{id_page}_button_start", "n_clicks"),
    [
        State(f"{id_page}_target", "options"),
        State(f"{id_page}_target", "value"),
        State("main_page_store", "data"),
        State(f"{id_page}_test_size", "value"),
        State(f"{id_page}_random_state_split", "value"),
        State(f"{id_page}_fit_intercept", "value"),
        State(f"{id_page}_copy_X", "value"),
        State(f"{id_page}_n_jobs", "value"),
        State(f"{id_page}_positive", "value"),
    ],
    prevent_initial_call=True,
)
def display_page(
    n_clicks,
    options_y,
    value_y,
    data,
    test_size,
    random_state,
    fit_intercept,
    copy_X,
    n_jobs,
    positive,
):
    if not n_clicks:
        raise PreventUpdate
    df = read_json(data["df"])
    value_x = [x for x in df.columns if x not in options_y]

    if not value_x:
        value_x = list(df.columns)
        value_x.remove(value_y)

    try:
        # train_test_split
        X_train, X_test, y_train, y_test = split_df(
            df, value_x, value_y, int(test_size) / 100, int(random_state)
        )
        # Entrenamos modelo
        regr = fit_model(X_train, y_train, fit_intercept, copy_X, n_jobs, positive)

        date_model = str(datetime.now()).split(".")[0]

        obj_middle = create_msg(
            f"""Modelo Entrenado.
                                     Guardado como {value_y}_{date_model}"""
        )

        # Guardamos Modelo
        path = f"""users/{data["user"]}/models/linear_regresion"""
        try:
            os.stat(path)
        except Exception:
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
        obj_middle = create_msg(err.__str__())
    return [obj_middle, ""]
