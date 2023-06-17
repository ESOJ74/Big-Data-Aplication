from dash import html

from callbacks.functions.getdummies import *
from utils.create_callback_content_up import content_up_functions
from utils.create_selector import SelectCreator

id_page = "getdummies"

content_up = content_up_functions(id_page, False, "get_dummies")
content_down = ""
params = [
    html.Div("Params", className="panel-title-params"),
    SelectCreator(
        "getdummies",
        ["prefix"],
        multi=True,
    ).create_select(),
    SelectCreator(
        "getdummies",
        ["columns"],
        multi=True,
    ).create_select(),
    SelectCreator(
        "getdummies",
        ["drop_first"],
        options=["True", "False"],
        value="False",
    ).create_select(),
    SelectCreator(
        "getdummies",
        ["dummy_na"],
        options=["True", "False"],
        value="False",
    ).create_select(),
    SelectCreator(
        "getdummies",
        ["sparse"],
        options=["True", "False"],
        value="False",
    ).create_select(),
    SelectCreator(
        "getdummies",
        ["dtype"],
        options=["int", "float", "str", "bool"],
        value="bool",
    ).create_select(),
]
