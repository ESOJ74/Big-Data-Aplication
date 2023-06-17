from dash import html

from callbacks.functions.drop import *
from utils.create_callback_content_up import content_up_functions
from utils.create_selector import SelectCreator

id_page = "drop"

content_up = content_up_functions(id_page)
content_down = ""
params = [
    html.Div("Params", className="panel-title-params"),
    SelectCreator(
        "drop",
        ["labels"],
        multi=True,
    ).create_select(),
    SelectCreator(
        "drop",
        ["axis"],
        options=[0, 1],
        value=1,
    ).create_select(),
]
