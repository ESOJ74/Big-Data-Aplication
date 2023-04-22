from dash import dcc
from dash_iconify import DashIconify

from common_functions.user_registry import user_login
from my_dash.my_html.my_div import my_div
from pages.main_page.main_page_callbacks import *
from pages.main_page.main_page_css import *
from pages.main_page.main_page_functions import (button_cover,
                                                 create_div_buttons)
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
                               # Button Cover
                               my_div(style_div_button_cover_right,
                                      f"{id_page}_div_button_cover",
                                      button_cover(f"{id_page}_button_cover", "btn btn-primary btn-sm",
                                                   style_button_cover_right,
                                                   children=DashIconify(
                                                                icon="ic:baseline-arrow-circle-left",   #2a9fd6
                                                                width=30
                                                            ),
                                      ),
                                      hidden=True
                               ), 
                               # Middle Left Panel                        
                               my_div(style_div_middle_left,
                                      f"{id_page}_div_middle_left",
                                      [       
                                       # DataFrame panel
                                       my_div(style_dataframe_panel, "",
                                              html.H5("DataFrame", style=style_title_color)
                                       ),
                                       create_div_buttons(
                                            style_div_1,
                                            style_button,
                                            buttons,
                                            classdiv="table-success"                                           
                                       ),
                                       # Div for Visualizations panel, Functions panel, Models panel
                                       my_div({"height": "70%"}, f"{id_page}_div_functions",
                                              [
                                               # Functions panel
                                               my_div(style_visualization_panel, "",
                                                      html.H5("Functions", style=style_title_color)
                                               ),
                                               create_div_buttons(
                                                   style_div_2,
                                                   style_button,
                                                   functions,                                                   
                                               ),
                                               # Visualizations panel
                                               my_div(style_visualization_panel, "",
                                                      html.H5("Visualizations", style=style_title_color)
                                               ),
                                               create_div_buttons(
                                                   style_div_2,
                                                   style_button,
                                                   visualizations,
                                               ),                                               
                                               # Models panel
                                               my_div(style_visualization_panel, "",
                                                      html.H5("Models", style=style_title_color)
                                               ),
                                               create_div_buttons(
                                                   style_div_2,
                                                   style_button,
                                                   models,
                                               ),
                                              ],
                                              hidden=True,
                                       ),
                                     ],
                                     className="alert-primary",
                                     hidden=True,
                               ),
                               # Central Panel
                               my_div(style_div_content, f"{id_page}_page_content"),                               
                              ]
                       ),
                       # Down Panel
                       my_div(style_down_panel, "", 
                              my_div({"margin-left": "2%"}, "",
                                      html.A("GitHub", href="https://github.com/ESOJ74/Big-Data-Aplication",
                                             style={"color": "black"}, target="_blank",
                                      )
                              ), className="alert-primary"
                       ),
                      ]
               )
