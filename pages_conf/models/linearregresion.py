from dash import dcc, html

from utils.create_callback_content_up import content_up_models
from utils.create_div_split import create_div_split
from utils.create_input import ParamInputCreator
from utils.create_selector import SelectCreator
from callbacks.models.linearregresion import *

id_page = "LinearRegression"

path = f"https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.{id_page}.html"
title = f"sklearn.linear_model.{id_page}()"

content_up = content_up_models(title, path)

params = [
    html.Div("Params", className="panel-title-params"),
    SelectCreator(
        id_page,
        ["fit_intercept"],
        ["True", "False"],
        "True",
    ).create_select(),
    SelectCreator(
        id_page,
        ["copy_X"],
        ["True", "False"],
        "True",
    ).create_select(),
    SelectCreator(
        id_page,
        ["positive"],
        ["True", "False"],
        "False",
    ).create_select(),
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
