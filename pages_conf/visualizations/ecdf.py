from dash import html

from assets.template import list_of_squential
from callbacks.visualizations.ecdf import * # noqa: F403
from utils.create_callback_content_up import content_up_visualizations
from utils.create_selector import SelectCreator

id_page = "ecdf"

content_up = content_up_visualizations(id_page, "ecdf-plots")
content_down = ""
params = [
    html.Div("Params", className="panel-title-params"),
    SelectCreator(
        "ecdf",
        ["X"],
    ).create_select(),
    SelectCreator(
        "ecdf",
        ["Y"],
    ).create_select(),
    SelectCreator(
        "ecdf",
        ["color"],
    ).create_select(),
    SelectCreator(
        "ecdf", ["ecdfnorm"], options=[" ", "percent"], value=" "
    ).create_select(),
    SelectCreator(
        "ecdf",
                ["ecdfmode"],
                options=["standard", "reversed", "complementary"],
                value="standard",
    ).create_select(),
    SelectCreator(
        "ecdf", ["markers"], options=["False", "True"], value="False"
    ).create_select(),
    SelectCreator(
        "ecdf",
        ["template"],
        options=list_of_squential,
        value="Plasma",
        maxHeight=200,
    ).create_select(),
]