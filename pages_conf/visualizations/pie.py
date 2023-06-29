from dash import html

from assets.template import list_of_squential
from callbacks.visualizations.pie import * # noqa: F403
from utils.create_callback_content_up import content_up_visualizations
from utils.create_selector import SelectCreator

id_page = "pie"

content_up = content_up_visualizations(id_page, "pie-charts")
content_down = ""
params = [
    html.Div("Params", className="panel-title-params"),
    SelectCreator(
        "pie",
        ["values"],
    ).create_select(),
    SelectCreator(
        "pie",
        ["names"],
    ).create_select(),
    SelectCreator(
        "pie",
        ["template"],
        options=list_of_squential,
        value="Plasma",
        maxHeight=200,
    ).create_select(),
]