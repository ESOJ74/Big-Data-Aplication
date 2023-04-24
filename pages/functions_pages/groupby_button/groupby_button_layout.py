from dash import dcc

from my_dash.my_html.my_div import my_div
from pages.functions_pages.groupby_button.groupby_button_callbacks import *

id_page = "groupby"

layout = my_div({"height": "100%"}, "", 
                [
                  my_div({"margin-top": "2%", "margin-left": "2%", "width": "60%", "height": "3%"}, "",
                         [
                          html.H5("DataFrame.groupby()", style={"float": "left", "width": "28%", "color": "#acf4ed"}),
                          html.A("Documentacion",
                                 href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html",
                                 style={"float": "left", "width": "60%"}, target="_blank"),
                         ],
                  ), 
                  my_div({},f"{id_page}_div_dropdown"),                  
                  my_div(style_div_content, f"{id_page}_content"),
                  dcc.Loading(
                      id="loading-2",
                      children=[my_div({"margin-top": "10%"}, f"{id_page}_groupby_loading")],
                      type="default",
                      fullscreen=False,
                  ),
                ])