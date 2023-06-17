from dash import html

from assets.template import list_of_squential
from callbacks.functions.corr import *
from utils.buttons_text_graph import ButtonsTextGraph
from utils.create_callback_content_up import content_up_functions
from utils.create_input import ParamInputCreator
from utils.create_selector import SelectCreator

id_page = "corr"

content_up = content_up_functions(id_page)
content_down = ""
params = [
    html.Div("Params", className="panel-title-params"),
    ButtonsTextGraph(id_page).buttons_text_graph(),
    SelectCreator(
        "corr",
        ["numeric_only"],
        ["True", "False"],
        "False",
    ).create_select(),
    SelectCreator(
        "corr",
        ["method"],
        ["pearson", "kendall", "spearman"],
        "pearson",
    ).create_select(),
    ParamInputCreator("corr", "min_periods").create_input(),    
    SelectCreator(
        "corr",
        ["template"],
        options=list_of_squential,
        value="Plasma",
        maxHeight=100,
    ).create_select(),
]
