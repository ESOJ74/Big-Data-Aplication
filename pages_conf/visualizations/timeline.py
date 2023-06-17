from dash import html

from assets.template import list_of_squential
from callbacks.visualizations.timeline import *
from utils.create_callback_content_up import content_up_visualizations
from utils.create_selector import SelectCreator

id_page = "timeline"

content_up = content_up_visualizations(id_page, "gantt")
content_down = ""
params = [
    html.Div("Params", className="panel-title-params"),    
    SelectCreator(
        "timeline",
        ["show_colorbar"],        
    ).create_select(),
     SelectCreator(
        "timeline",
        ["group_tasks"],        
    ).create_select(),
    SelectCreator(
        "timeline",
        ["template"],
        options=list_of_squential,
        value="Plasma",
        maxHeight=200,
    ).create_select(),
]