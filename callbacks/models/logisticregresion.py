import os
import pickle
from datetime import datetime

from dash import Input, Output, State, callback
from dash.exceptions import PreventUpdate
from joblib import dump
from pandas import read_json
from sklearn.linear_model import LogisticRegression

from utils.split_df import split_df
from utils.utils_functions import create_msg

id_page = "LogisticRegression"


def fit_model(
    X,
    y,
    penalty,
    dual,
    tol,
    c,
    fit_intercept,
    intercept_scaling,
    random_state,
    solver,
    max_iter,
    multi_class,
    verbose,
    warm_start,
    n_jobs,
    l1_ratio,
):
    dual = dual == "True"
    fit_intercept = fit_intercept == "True"
    warm_start = warm_start == "True"
    if tol is not None:
        tol = float(tol)
    if c is not None:
        c = float(c)
    if intercept_scaling is not None:
        intercept_scaling = int(intercept_scaling)
    if random_state is not None:
        random_state = int(random_state)
    if max_iter is not None:
        max_iter = int(max_iter)
    if verbose is not None:
        verbose = int(verbose)
    if n_jobs is not None:
        n_jobs = int(n_jobs)
    if l1_ratio is not None:
        l1_ratio = int(l1_ratio)

    # Creamos el objeto de Regresión Linear
    regr = LogisticRegression(
        penalty=penalty,
        dual=dual,
        tol=tol,
        C=c,
        fit_intercept=fit_intercept,
        intercept_scaling=intercept_scaling,
        random_state=random_state,
        solver=solver,
        max_iter=max_iter,
        multi_class=multi_class,
        verbose=verbose,
        warm_start=warm_start,
        n_jobs=n_jobs,
        l1_ratio=l1_ratio,
    )
    regr.fit(X, y)
    return regr


@callback(
    [
        Output(f"{id_page}_target", "options"),
        Output(f"{id_page}_target", "value"),
    ],
    Input("logisticregresion", "n_clicks"),
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
        State(f"{id_page}_penalty", "value"),
        State(f"{id_page}_dual", "value"),
        State(f"{id_page}_tol", "value"),
        State(f"{id_page}_c", "value"),
        State(f"{id_page}_fit_intercept", "value"),
        State(f"{id_page}_intercept_scal", "value"),
        State(f"{id_page}_random_state", "value"),
        State(f"{id_page}_solver", "value"),
        State(f"{id_page}_max_iter", "value"),
        State(f"{id_page}_multi_class", "value"),
        State(f"{id_page}_verbose", "value"),
        State(f"{id_page}_warm_start", "value"),
        State(f"{id_page}_n_jobs", "value"),
        State(f"{id_page}_l1_ratio", "value"),
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
    penalty,
    dual,
    tol,
    c,
    fit_intercept,
    intercept_scaling,
    random_state2,
    solver,
    max_iter,
    multi_class,
    verbose,
    warm_start,
    n_jobs,
    l1_ratio,
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
        regr = fit_model(
            X_train,
            y_train,
            penalty,
            dual,
            tol,
            c,
            fit_intercept,
            intercept_scaling,
            random_state2,
            solver,
            max_iter,
            multi_class,
            verbose,
            warm_start,
            n_jobs,
            l1_ratio,
        )

        date_model = str(datetime.now()).split(".")[0]

        obj_middle = create_msg(
            f"""Modelo Entrenado.
                                 Guardado como {value_y}_{date_model}"""
        )

        # Guardamos Modelo
        path = f"""users/{data["user"]}/models/logistic_regresion"""
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
