from dash import html

from assets.template import list_of_squential
from callbacks.visualizations.violin import *  # noqa: F403
from utils.create_callback_content_up import content_up_visualizations
from utils.create_selector import SelectCreator

id_page = "violin"

content_up = content_up_visualizations(id_page, "violin")
content_down = ""
params = [
    html.Div("Params", className="panel-title-params"),
    SelectCreator(
        "violin",
        ["X"],
    ).create_select(),
    SelectCreator(
        "violin",
        ["Y"],
    ).create_select(),
    SelectCreator(
        "violin",
        ["color"],
    ).create_select(),
    SelectCreator(
        "violin",
        ["hover_data"],
    ).create_select(),
    SelectCreator(
        "violin", ["box"], options=["True", "False"], value="False"
    ).create_select(),
    SelectCreator(
        "violin",
        ["points"],
        options=["all", "outliers", "False"],
        value="False",
    ).create_select(),
    SelectCreator(
        "violin", ["violinmode"], options=["overlay", "group"], value="group"
    ).create_select(),
    SelectCreator(
        "violin",
        ["template"],
        options=list_of_squential,
        value="Plasma",
        maxHeight=150,
    ).create_select(),
]
