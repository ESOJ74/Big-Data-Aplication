from dash import dcc

from my_dash.my_html.my_div import my_div
from pages.functions_pages.drop_columns_button.drop_columns_button_callbacks import *

id_page = "drop_columns"

layout = my_div({"height": "100%"}, "", 
                [
                  my_div({"margin-top": "2%", "margin-left": "2%"}, "",
                         html.H5("DataFrame Drop"),),
                  my_div({},f"{id_page}_div_dropdown"),                  
                  my_div(style_div_content, f"{id_page}_content"),
                  dcc.Loading(
                               id="loading-2",
                               children=[my_div({}, f"{id_page}_drop_loading")],
                               type="default",
                               fullscreen=False,
                           ),
                ])