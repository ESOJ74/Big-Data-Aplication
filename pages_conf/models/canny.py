from dash import html, dcc
import dash_bootstrap_components as dbc
from utils.create_selector import SelectCreator
from utils.create_input import ParamInputCreator
from utils.create_callback_content_up import content_up_existing_models
from callbacks.models.canny import *  # noqa: F403

id_page = "canny"

path = "https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html"
path2 = "https://github.com/cynicphoenix/Canny-Edge-Detector"
title = f"cv.{id_page}()"

content_up = content_up_existing_models(title, path, path2)
content_down = html.Div(
    [
        html.Div(
            id=f"{id_page}_Div_derecha",
            children=[
                html.Div(
                    [
                        html.Div(
                            dcc.Dropdown(
                                id=f"{id_page}_drop_foto",
                                placeholder="Select Foto",
                                className="drop-target",
                            ),
                        ),
                    ],                    
                    id=f"{id_page}_div_derecha",
                    className="panel-target",
                ),
                dbc.Button(
                    "Up Foto from Local",
                    f"{id_page}_up_foto",
                    className="btn-up-foto",
                ),
            ],style={"width": "100%"},
        ),
        html.Div(id=f"{id_page}_div_result",
                 style={"margin-left": "2%", "margin-top": "1%", "width": "100%"}),
    ], style={"margin-top": "1%"}
)

params = [
    html.Div("Params", className="panel-title-params"),
    SelectCreator(
        id_page,
        ["L2gradient"],
        ["True", "False"],
        "False",
    ).create_select(),
    ParamInputCreator(id_page, "threshold1", 100).create_input(),
    ParamInputCreator(id_page, "threshold2", 200).create_input(),
    ParamInputCreator(id_page, "aperture_size", 3).create_input(),    
]
