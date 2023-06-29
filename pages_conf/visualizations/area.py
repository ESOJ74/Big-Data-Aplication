from dash import html

from assets.template import list_of_squential
from callbacks.visualizations.area import *  # noqa: F403
from utils.create_callback_content_up import content_up_visualizations
from utils.create_selector import SelectCreator

id_page = "area"

content_up = content_up_visualizations(id_page, "filled-area-plots")
content_down = ""
params = [
    html.Div("Params", className="panel-title-params"),
    SelectCreator(
        "area",
        ["X"],
    ).create_select(),
    SelectCreator(
        "area",
        ["Y"],
    ).create_select(),
    SelectCreator(
        "area",
        ["color"],
    ).create_select(),
    SelectCreator(
        "area",
        ["line_group"],
    ).create_select(),
    SelectCreator(
        "area",
        ["template"],
        options=list_of_squential,
        value="Plasma",
        maxHeight=200,
    ).create_select(),
]
