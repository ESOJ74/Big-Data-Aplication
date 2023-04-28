
from dash import dcc

from common_functions.common_functions_css import (style_div_content_functions,
                                                   style_div_utils_functions)
from my_dash.my_html.my_div import my_div


def create_functions_layout(id_page, create_utils=""):
    return [
            dcc.Loading(
                id="loading-2",
                children=[my_div({"margin-top": "2%", "height": "5%"},
                                 f"{id_page}_loading")],
                type="default",
                fullscreen=False,
            ),
            my_div(style_div_content_functions, f"{id_page}_content"),
            my_div(style_div_utils_functions, f"{id_page}_utils", create_utils)
           ]