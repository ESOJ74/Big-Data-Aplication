from dash import dcc, html

from callbacks.models.logisticregresion import *
from utils.create_callback_content_up import content_up_models
from utils.create_div_split import create_div_split
from utils.create_input import ParamInputCreator
from utils.create_selector import SelectCreator

id_page = "LogisticRegression"

path = f"https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.{id_page}.html"
title = f"sklearn.linear_model.{id_page}()"

content_up = content_up_models(title, path)

params = [
    html.Div("Params", className="panel-title-params"),
    SelectCreator(
        id_page,
        ["penalty"],
        ["l1", "l2", "elasticnet"],
        "l2",
    ).create_select(),
    SelectCreator(
        id_page,
        ["dual"],
        ["True", "False"],
        "False",
    ).create_select(),
    SelectCreator(
        id_page,
        ["fit_intercept"],
        ["True", "False"],
        "True",
    ).create_select(),
    SelectCreator(
        id_page,
        ["solver"],
        ["lbfgs", "liblinear", "newton-cg", "newton-cholesky", "sag", "saga"],
        "lbfgs",
    ).create_select(),
    SelectCreator(
        id_page,
        ["multi_class"],
        ["auto", "ovr", "multinomial"],
        "auto",
    ).create_select(),
    SelectCreator(
        id_page,
        ["warm_start"],
        ["True", "False"],
        "False",
    ).create_select(),
    ParamInputCreator(id_page, "tol", 1e-4).create_input(),
    ParamInputCreator(id_page, "c", 1.0).create_input(),
    ParamInputCreator(id_page, "intercept_scal", 1.0).create_input(),
    ParamInputCreator(id_page, "random_state", None).create_input(),
    ParamInputCreator(id_page, "max_iter", 100).create_input(),
    ParamInputCreator(id_page, "l1_ratio", None).create_input(),
    ParamInputCreator(id_page, "verbose", 0).create_input(),
    ParamInputCreator(id_page, "n_jobs", None).create_input(),
]

content_down = html.Div(
    [
        html.Div(
            [
                html.Div("Target", className="target"),
                html.Div(
                    dcc.Dropdown(
                        id=f"{id_page}_target",
                        placeholder="Select Target",
                        className="drop-target",
                    ),
                ),
            ],
            id=f"{id_page}_div_derecha",
            className="panel-target",
        ),
        create_div_split(id_page),
        html.Div(id=f"{id_page}_div_result"),
    ],
    className="panel-content-down",
)
