from dash import html

from callbacks.functions.describe import *  # noqa: F403
from utils.create_callback_content_up import content_up_functions
from utils.create_input import ParamInputCreator
from utils.create_selector import SelectCreator

id_page = "describe"

content_up = content_up_functions(id_page)
content_down = ""
params = [
    html.Div("Params", className="panel-title-params"),
    SelectCreator(
        "describe",
        ["include"],
        ["", "all", "number", "category", "object"],
        "",
    ).create_select(),
    SelectCreator(
        "describe",
        ["exclude"],
        ["", "number", "category", "object"],
        "",
    ).create_select(),
    ParamInputCreator("describe", "percentiles", "").create_input(),
]
