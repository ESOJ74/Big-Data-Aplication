from utils.create_callback_content_up import content_up_functions
from callbacks.functions.t import *  # noqa: F403
from dash import html

id_page = "t"

content_up = content_up_functions(id_page)
content_down = html.Div(
    id=f"{id_page}_content_down", className="transpose-content-down"
)
params = [html.Div(className="no-params")]
