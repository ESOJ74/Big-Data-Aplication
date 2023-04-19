from dash import dcc

from common_functions.user_registry import user_login
from my_dash.my_html.my_div import my_div
from pages.main_page.main_page_callbacks import *
from pages.main_page.main_page_css import *
from pages.main_page.main_page_functions import create_div_buttons
from pages.main_page.main_page_lists import (buttons, functions, models,
                                             visualizations)

id_page = "main_page"

layout: dict = my_div(style_div_main, "",
                      [
                       dcc.Store(id=f"{id_page}_store"),        
                       user_login(id_page),               
                       # Up Panel
                       my_div(style_up_panel, "",
                              [
                                my_div(style_div_user, "", 
                                       my_div(style_user, f"{id_page}_panel_up_left"),
                                ),
                                my_div(style_div_app, "", 
                                       html.H5("Big Data App", style=style_app)),
                                my_div(style_div_sesion, "",
                                       my_div(style_sesion, f"{id_page}_panel_up_right"),
                                )
                              ], className="alert-primary"),
                       # Middle Panel
                       my_div(style_middle_panel, "",
                              [
                               # Left Panel
                               my_div(style_div_buttons, f"{id_page}_left",
                                      [
                                      # DataFrame panel
                                       my_div(style_dataframe_panel, "",
                                              html.H5("DataFrame", style={"color": "#0F1458"})
                                       ),
                                       create_div_buttons(
                                            style_div_1,
                                            style_button,
                                            buttons, classdiv="table-success"                                           
                                       ),
                                       # Div for Visualizations panel, Functions panel, Models panel
                                       my_div({"height": "70%"}, f"{id_page}_div_functions",
                                              [
                                               # Visualizations panel
                                               my_div(style_visualization_panel, "",
                                                      html.H5("Visualizations", style={"color": "#0F1458"})
                                               ),
                                               create_div_buttons(
                                                   style_div_2,
                                                   style_button,
                                                   visualizations,
                                               ),
                                               # Functions panel
                                               my_div(style_visualization_panel, "",
                                                      html.H5("Functions", style={"color": "#0F1458"})
                                               ),
                                               create_div_buttons(
                                                   style_div_2,
                                                   style_button,
                                                   functions,
                                                   
                                               ),
                                               # Models panel
                                               my_div(style_visualization_panel, "",
                                                      html.H5("Models", style={"color": "#0F1458"})
                                               ),
                                               create_div_buttons(
                                                   style_div_2,
                                                   style_button,
                                                   models,
                                               ),
                                              ],
                                              hidden=True,
                                       ),
                                     ],className="alert-primary",
                               ),
                               # Central Panel
                               my_div(style_div_content, f"{id_page}_page_content"),                               
                              ]
                       ),
                       # Down Panel
                       my_div(style_down_panel, "", 
                              my_div({"margin-left": "2%"}, "",
                                      html.A("GitHub", href="https://github.com/ESOJ74/Big-Data-Aplication",
                                             style={"color": "black"}, target='_blank',
                                      )
                              ), className="alert-primary"
                       ),
                      ]
               )
