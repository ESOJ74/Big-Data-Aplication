from dash import html

from assets.template import list_of_squential
from callbacks.visualizations.sunburst import *  # noqa: F403
from utils.create_callback_content_up import content_up_visualizations
from utils.create_selector import SelectCreator

id_page = "sunburst"

content_up = content_up_visualizations(id_page, "sunburst-charts")
content_down = ""
params = [
    html.Div("Params", className="panel-title-params"),    
    SelectCreator(
        "sunburst",
        ["template"],
        options=list_of_squential,
        value="Plasma",
        maxHeight=200,
    ).create_select(),
]