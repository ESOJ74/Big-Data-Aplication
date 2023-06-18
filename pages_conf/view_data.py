from dash import html

from callbacks.view_data import *

id_page = "view_data"

content_up = ""

content_down = html.Div(
    "", f"{id_page}_content_down", className="transpose-content-down"
)

params = [html.Div(className="no-params")]
