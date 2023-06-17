from dash import html

from assets.template import list_of_squential
from callbacks.visualizations.strip import *
from utils.create_callback_content_up import content_up_visualizations
from utils.create_selector import SelectCreator

id_page = "strip"

content_up = content_up_visualizations(id_page, "strip-charts")
content_down = ""
params = [
    html.Div("Params", className="panel-title-params"),
    SelectCreator(
        "strip",
        ["X"],
    ).create_select(),
    SelectCreator(
        "strip",
        ["Y"],
    ).create_select(),
    SelectCreator(
        "strip",
        ["color"],
    ).create_select(),
    SelectCreator(
        "strip",
        ["hover_data"],
    ).create_select(),
    SelectCreator(
        "strip",
        ["facet_col"],
    ).create_select(),
    SelectCreator(
        "strip", ["stripmode"], options=["overlay", "group"], value="group"
    ).create_select(),
    SelectCreator(
        "strip",
        ["template"],
        options=list_of_squential,
        value="Plasma",
        maxHeight=200,
    ).create_select(),
]