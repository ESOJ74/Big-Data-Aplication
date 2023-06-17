from dash import html

from callbacks.functions.groupby import *
from utils.create_callback_content_up import content_up_functions
from utils.create_selector import SelectCreator

id_page = "groupby"

content_up = content_up_functions(id_page)
content_down = ""
params = [
    html.Div("Params", className="panel-title-params"),
    SelectCreator(
        "groupby",
        ["by"],
        multi=True,
    ).create_select(),
    SelectCreator(
        "groupby",
        ["axis"],
        [0, 1],
        0,
    ).create_select(),
]
