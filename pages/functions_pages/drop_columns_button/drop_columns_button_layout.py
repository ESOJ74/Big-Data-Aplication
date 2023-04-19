from dash import dcc

from my_dash.my_html.my_div import my_div
from pages.functions_pages.drop_columns_button.drop_columns_button_callbacks import *

id_page = "drop_columns"

layout = my_div({"height": "100%"}, "", 
                [
                  my_div({},f"{id_page}_div_dropdown"),
                  dcc.Loading(
                               id="loading-2",
                               children=[my_div({}, f"{id_page}_drop_loading")],
                               type="default",
                               fullscreen=False,
                           ),
                  my_div(style_div_content, f"{id_page}_content")
                ])