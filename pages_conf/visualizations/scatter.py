from dash import html

from assets.template import list_of_squential
from callbacks.visualizations.scatter import *  # noqa: F403
from utils.create_callback_content_up import content_up_visualizations
from utils.create_selector import SelectCreator

id_page = "scatter"

content_up = content_up_visualizations(id_page, "line-and-scatter")
content_down = ""
params = [
    html.Div("Params", className="panel-title-params"),
    SelectCreator(
        "scatter",
        ["X"],
    ).create_select(),
    SelectCreator(
        "scatter",
        ["Y"],
    ).create_select(),
    SelectCreator(
        "scatter",
        ["color"],
    ).create_select(),
    SelectCreator(
        "scatter",
        ["size"],
    ).create_select(),
    SelectCreator(
        "scatter",
        ["hover_data"],
    ).create_select(),
    SelectCreator(
        "scatter",
        ["template"],
        options=list_of_squential,
        value="Plasma",
        maxHeight=200,
    ).create_select(),
]