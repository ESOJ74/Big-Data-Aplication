from dash import dcc, html

from my_dash.my_html.my_div import my_div
from common_functions.common_functions_css import *


def create_visualization_layout(id_page, create_utils = "hola"):
    return my_div(style_main_div, "",
                  [                   
                   my_div(style_div_content, "",
                          [
                           my_div(style_div_title, "",
                                  html.H5(f"DataFrame {id_page.split('_')[0]}",
                                          style = {"color": "#acf4ed"}),
                           ),
                           my_div(style_div_content_up, f"{id_page}_content_up"),
                           dcc.Loading(
                               id="loading-2",
                               children=[my_div({}, f"{id_page}_visualizations_loading")],
                               type="default",
                               fullscreen=False,
                           ),
                           my_div(style_div_content_middle, f"{id_page}_content_middle"),
                           my_div(style_div_content_down, f"{id_page}_content_down"),
                          ]
                   ),
                   my_div(style_div_utils, f"{id_page}_utils", create_utils)
                  ])