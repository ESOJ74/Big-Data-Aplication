from dash import html

from callbacks.functions.info import *  # noqa: F403
from utils.create_callback_content_up import content_up_functions

id_page = "info"

content_up = content_up_functions(id_page)
content_down = ""
params = [html.Div(className="no-params")]
