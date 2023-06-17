from dash import html
from numpy import arange

from assets.template import list_of_squential
from callbacks.visualizations.scatter3d import *
from utils.create_callback_content_up import content_up_visualizations
from utils.create_selector import SelectCreator

id_page = "scatter3d"

content_up = content_up_visualizations(id_page, "3d-scatter-plots")
content_down = ""
params = [
    html.Div("Params", className="panel-title-params"),
    SelectCreator(
        "scatter3d",
        ["X"],
    ).create_select(),
    SelectCreator(
        "scatter3d",
        ["Y"],
    ).create_select(),
    SelectCreator(
        "scatter3d",
        ["Z"],
    ).create_select(),
    SelectCreator(
        "scatter3d",
        ["color"],
    ).create_select(),
    SelectCreator(
        "scatter3d",
        ["symbol"],
    ).create_select(),
    SelectCreator(
        "scatter3d",
        ["size"],
    ).create_select(),
    SelectCreator(
        "scatter3d",
        ["log_x"],
        options=["True", "False"],
        value="False",
    ).create_select(),
    SelectCreator(
        "scatter3d",
        ["log_y"],
        options=["True", "False"],
        value="False",
    ).create_select(),
    SelectCreator(
        "scatter3d",
        ["log_z"],
        options=["True", "False"],
        value="False",
    ).create_select(),
    SelectCreator(
        "scatter3d", ["opacity"], options=list(arange(0.1, 1.1, 0.1)), value=1
    ).create_select(),
    SelectCreator(
        "scatter3d",
        ["template"],
        options=list_of_squential,
        value="Plasma",
        maxHeight=45,
    ).create_select(),
]
