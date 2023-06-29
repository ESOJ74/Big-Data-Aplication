from dash import html

from assets.template import list_of_squential
from callbacks.visualizations.box import * # noqa: F403
from utils.create_callback_content_up import content_up_visualizations
from utils.create_selector import SelectCreator

id_page = "box"

content_up = content_up_visualizations(id_page, "box-plots")
content_down = ""
params = [
    html.Div("Params", className="panel-title-params"),
    SelectCreator(
        "box",
        ["X"],
    ).create_select(),
    SelectCreator(
        "box",
        ["Y"],
    ).create_select(),
    SelectCreator(
        "box",
        ["color"],
    ).create_select(),
    SelectCreator(
        "box",
        ["hover_data"],
    ).create_select(),
    SelectCreator(
        "box",
        ["points"],
        options=["False", "all", "outliers", "suspectedoutliers"],
        value="outliers",
    ).create_select(),
    SelectCreator(
        "box",
        ["quartilemethod"],
        options=["exclusive", "inclusive", "linear"],
        value="linear",
    ).create_select(),
    SelectCreator(
        "box", ["notched"], options=["True", "False"], value="False"
    ).create_select(),
    SelectCreator(
        "box",
        ["template"],
        options=list_of_squential,
        value="Plasma",
        maxHeight=100,
    ).create_select(),
]
