from dash import dcc

from my_dash.my_html.my_div import my_div
from pages.functions_pages.groupby_button.groupby_button_callbacks import *

id_page = "groupby"

layout = my_div({"height": "100%"}, "", 
                [
                  my_div({"margin-top": "2%", "margin-left": "2%"}, "",
                         html.H5("DataFrame Groupby"),),
                  my_div({},f"{id_page}_div_dropdown"),                  
                  my_div(style_div_content, f"{id_page}_content"),
                  dcc.Loading(
                      id="loading-2",
                      children=[my_div({"margin-top": "10%"}, f"{id_page}_groupby_loading")],
                      type="default",
                      fullscreen=False,
                  ),
                ])