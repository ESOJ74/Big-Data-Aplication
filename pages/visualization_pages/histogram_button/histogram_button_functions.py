from dash import dcc, html

from assets.my_dash.my_dbc.my_button import my_button
from assets.my_dash.my_dcc.my_dropdown import my_dropdown
from assets.my_dash.my_html.my_div import my_div
from assets.visualizations_css import *

id_page = "histogram"


def create_utils(id_page):
    return my_div(style_div_utils, "",
                 [
                   my_div(style_div_nbins, "",  
                          [
                           html.H6("nbins", style=style_params),
                           dcc.Input(id=f"{id_page}_nbins",
                                     style=style_input_nbins,
                                     value=20,
                           )
                          ]
                   ),
                   my_div(style_div_color, "",
                          [
                           html.H6("color", style=style_params),
                           my_div(style_selector_color, "",
                                  my_dropdown(f"{id_page}_color", {},),
                           )
                          ],
                   ),                        
                   my_button(f"{id_page}_refresh", "Refresh", style_button,
                             className="btn btn-outline-warning", color="black")   
                 ]
           )