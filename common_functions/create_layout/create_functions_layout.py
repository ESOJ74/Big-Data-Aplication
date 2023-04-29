
from dash import dcc, html

from assets.functions_css import *
from assets.my_dash.my_html.my_div import my_div


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


def create_functions_layout_with_dropdown(id_page):
    return my_div(style_div_panel, "", 
                  [
                   my_div(style_div_title, "",
                          [
                           html.H5(f"DataFrame.{id_page}()", style=style_title),
                           html.A("Documentacion",
                                  href=f"https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.{id_page}.html",
                                  style=style_div_A, target="_blank"),
                          ],
                   ),
                   my_div(style_div_dropdown, f"{id_page}_div_dropdown"),
                   my_div(style_div_content, f"{id_page}_content"),
                   dcc.Loading(
                       id="loading-2",
                       children=[my_div({}, f"{id_page}_loading")],
                       type="default",
                       fullscreen=False,
                   ),
                  ]
           )