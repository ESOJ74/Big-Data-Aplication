from dash import html

from my_dash.my_dbc.my_button import my_button
from my_dash.my_dcc.my_dropdown import my_dropdown
from my_dash.my_html.my_div import my_div
from pages.visualization_pages.boxplot_button.boxplot_button_css import *

id_page = "boxplot_button"

s_utils = {
    "position": "relative",
    "top": "10%",
    "width": "100%",
    "height": "50%",
    "background": "#95D3DE",
    "font-family": "Roboto, Helvetica, Arial, sans-serif",
}

style_div_input = {
    "margin-left": "2%",
    "font-weight": "bold",
    "color": "#012A32"
}


def create_utils(id_page):
    return my_div(style_div_utils, "",
                 [
                   my_div({"height": "2%"}),
                   my_div(style_div_color, "",
                          [
                           html.H6("points", style=style_params),
                           my_div(style_selector_color, "",
                                  my_dropdown(f"{id_page}_points", {},
                                              options=["all", "outliers", "false"],
                                              value="outliers"),
                           )
                          ],
                   ),   
                   my_div(style_div_color, "",
                          [
                           html.H6("color", style=style_params),
                           my_div(style_selector_color, "",
                                  my_dropdown(f"{id_page}_color", {},),
                           )
                          ],
                   ), 
                   my_div(style_div_color, "",
                          [
                           html.H6("quartile", style=style_params),
                           my_div(style_selector_color, "",
                                  my_dropdown(f"{id_page}_quartilemethod", {},
                                              options=["linear", "inclusive", "exclusive"],
                                              value="linear"),
                           )
                          ],
                   ),  
                   my_div(style_div_color, "",
                          [
                           html.H6("notched", style=style_params),
                           my_div(style_selector_color, "",
                                  my_dropdown(f"{id_page}_notched", {},
                                              options=["true", "false"],
                                              value="false"),
                           )
                          ],
                   ),
                   my_div(style_div_color, "",
                          [
                           html.H6("hover", style=style_params),
                           my_div(style_selector_color, "",
                                  my_dropdown(f"{id_page}_hover_data", {},),
                           )
                          ],
                   ),                                 
                   my_button(f"{id_page}_refresh", "Refresh", style_button,
                             className="btn btn-outline-warning", color="black"),                                     
                 ]
           )