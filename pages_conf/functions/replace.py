from dash import html

from callbacks.functions.replace import *  # noqa: F403
from utils.create_callback_content_up import content_up_functions
from utils.create_input import ParamInputCreator
from utils.create_selector import SelectCreator

id_page = "replace"

content_up = content_up_functions(id_page)
content_down = ""
params = [
    html.Div("Params", className="panel-title-params"),
    ParamInputCreator("replace", "to_replace", None).create_input(),
    ParamInputCreator("replace", "value", None).create_input(),
    ParamInputCreator("replace", "limit", " ").create_input(),
    SelectCreator(
        "replace",
        ["regex"],
        ["True", "False"],
        "False",
    ).create_select(),
]
