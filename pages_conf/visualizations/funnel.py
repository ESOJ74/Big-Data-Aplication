from dash import html

from assets.template import list_of_squential
from callbacks.visualizations.funnel import * # noqa: F403
from utils.create_callback_content_up import content_up_visualizations
from utils.create_selector import SelectCreator

id_page = "funnel"

content_up = content_up_visualizations(id_page, "funnel-charts")
content_down = ""
params = [
    html.Div("Params", className="panel-title-params"),
    SelectCreator(
        "funnel",
        ["X"],
    ).create_select(),
    SelectCreator(
        "funnel",
        ["Y"],
    ).create_select(),
    SelectCreator(
        "funnel",
        ["color"],
    ).create_select(),
    SelectCreator(
        "funnel",
        ["template"],
        options=list_of_squential,
        value="Plasma",
        maxHeight=200,
    ).create_select(),
]