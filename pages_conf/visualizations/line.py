from dash import html

from assets.template import list_of_squential
from callbacks.visualizations.line import * # noqa: F403
from utils.create_callback_content_up import content_up_visualizations
from utils.create_selector import SelectCreator

id_page = "line"

content_up = content_up_visualizations(id_page, "line-charts")
content_down = ""
params = [
    html.Div("Params", className="panel-title-params"),
    SelectCreator(
        "line",
        ["X"],
    ).create_select(),
    SelectCreator(
        "line",
        ["Y"],
    ).create_select(),
    SelectCreator(
        "line",
        ["color"],
    ).create_select(),
    SelectCreator(
        "line",
        ["template"],
        options=list_of_squential,
        value="Plasma",
        maxHeight=200,
    ).create_select(),
]