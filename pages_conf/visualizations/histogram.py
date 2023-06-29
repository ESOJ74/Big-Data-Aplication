from dash import html

from assets.template import list_of_squential
from callbacks.visualizations.histogram import * # noqa: F403
from utils.create_callback_content_up import content_up_visualizations
from utils.create_input import ParamInputCreator
from utils.create_selector import SelectCreator

id_page = "histogram"

content_up = content_up_visualizations(id_page, "histograms")
content_down = ""
params = [
    html.Div("Params", className="panel-title-params"),
    SelectCreator(
        "histogram",
        ["X"],
    ).create_select(),
    SelectCreator(
        "histogram",
        ["Y"],
    ).create_select(),    
    SelectCreator(
        "histogram",
        ["color"],
    ).create_select(),
    SelectCreator(
        "histogram",
        ["pattern_shape"],
    ).create_select(),
    SelectCreator(
        "histogram",
        ["histnorm"],
                options=[
                    " ",
                    "percent",
                    "probability",
                    "density",
                    "probability density",
                ],
                value=" ",
    ).create_select(),
    SelectCreator(
        "histogram",
                ["log_y"],
                options=["True", "False"],
                value="False",
    ).create_select(),
    SelectCreator(
        "histogram",
                ["histfunc"],
                options=["count", "sum", "avg", "min", "max"],
                value="count",
    ).create_select(),
    ParamInputCreator("histogram", "nbins", 20).create_input(),
    ParamInputCreator("histogram", "bargap", 0).create_input(),
    ParamInputCreator("histogram", "opacity", 1).create_input(),
    SelectCreator(
        "histogram",
        ["template"],
        options=list_of_squential,
        value="Plasma",
        maxHeight=40,
    ).create_select(),
]