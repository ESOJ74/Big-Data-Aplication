from dash import html

from assets.template import list_of_squential
from callbacks.visualizations.bar import *
from utils.create_callback_content_up import content_up_visualizations
from utils.create_selector import SelectCreator

id_page = "bar"

content_up = content_up_visualizations(id_page, "bar-charts")
content_down = ""
params = [
    html.Div("Params", className="panel-title-params"),
    SelectCreator(
        "bar",
        ["X"],
    ).create_select(),
    SelectCreator(
        "bar",
        ["Y"],
    ).create_select(),
    SelectCreator(
        "bar",
        ["color"],
    ).create_select(),
    SelectCreator(
        "bar",
        ["template"],
        options=list_of_squential,
        value="Plasma",
        maxHeight=200,
    ).create_select(),
]