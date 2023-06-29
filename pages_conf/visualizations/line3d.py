from dash import html

from assets.template import list_of_squential
from callbacks.visualizations.line3d import * # noqa: F403
from utils.create_callback_content_up import content_up_visualizations
from utils.create_selector import SelectCreator

id_page = "line3d"

content_up = content_up_visualizations(id_page, "3d-line-plots")
content_down = ""
params = [
    html.Div("Params", className="panel-title-params"),
    SelectCreator(
        "line3d",
        ["X"],
    ).create_select(),
    SelectCreator(
        "line3d",
        ["Y"],
    ).create_select(),
    SelectCreator(
        "line3d",
        ["Z"],
    ).create_select(),
    SelectCreator(
        "line3d",
        ["color"],
    ).create_select(),
    SelectCreator(
        "line3d",
        ["symbol"],
    ).create_select(),
    SelectCreator(
        "line3d",
        ["markers"],
    ).create_select(),
    SelectCreator(
        "line3d",
        ["log_x"],
        options=["True", "False"],
        value="False",
    ).create_select(),
    SelectCreator(
        "line3d",
        ["log_y"],
        options=["True", "False"],
        value="False",
    ).create_select(),
    SelectCreator(
        "line3d",
        ["log_z"],
        options=["True", "False"],
        value="False",
    ).create_select(),    
    SelectCreator(
        "line3d",
        ["template"],
        options=list_of_squential,
        value="Plasma",
        maxHeight=80,
    ).create_select(),
]
