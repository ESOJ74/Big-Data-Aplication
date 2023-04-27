from dash import dcc
from dash_iconify import DashIconify
import dash_bootstrap_components as dbc
from common_functions.user_registry import user_login
from my_dash.my_html.my_div import my_div
from my_dash.my_dbc.my_button import my_button
from pages.main_page.main_page_callbacks import *
from pages.main_page.main_page_css import *
from pages.main_page.main_page_functions import (button_cover, create_div_buttons1,
                                                 create_div_buttons)
from pages.main_page.main_page_lists import (buttons, functions, functions_info, models,
                                             buttons_data, visualizations)

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
                                       my_div({"width": "100%", "height": "4.5%"}, f"{id_page}_content_data",
                                              [my_div(style_div_button_data, "",
                                                      [                                               
                                                        my_button(f"{id_page}_button_data", "Data",
                                                                  style_button_data, color="black",
                                                                  className="btn btn-outline-primary dropdown-toggle"
                                                        ),                                                           
                                                       ]
                                               ),
                                               my_div(style_div_button_view, "",
                                                      create_div_buttons1(
                                                          style_div_0,
                                                          style_button_data,
                                                          buttons,
                                                          classdiv="table-success"                                           
                                                      ),
                                               ),
                                               
                                              ]
                                       ),
                                       my_div({"width": "38%", "height": "5%"}, f"{id_page}_div_data",
                                                               create_div_buttons1(
                                                                   style_div_1,
                                                                   style_button1,
                                                                   buttons_data,
                                                                   classdiv="table-success"                                           
                                                               ),
                                                               hidden=True
                                                        ),
                                       # Div for Visualizations panel, Functions panel, Models panel
                                       my_div({"height": "70%"}, f"{id_page}_div_functions",
                                              [
                                               # Functions panel
                                               my_div(style_h5_panel_functions, "",
                                                      html.H5("Functions", style=style_title_color)
                                               ),
                                               my_div(style_div_button_drop_info, "",
                                                      my_button(f"{id_page}_button_drop_info", "Info",
                                                                style_button_drop_info, color="black",
                                                                className="btn btn-outline-primary dropdown-toggle"
                                                      ), 
                                               ),
                                               my_div(style_div_buttons_info, f"{id_page}_div_duttons_info",                                                      
                                                      create_div_buttons(
                                                          style_div_3,
                                                          style_button2,
                                                          functions_info,                                                   
                                                      ), hidden=True
                                               ),
                                               create_div_buttons(
                                                   style_div_buttons_functions,
                                                   style_button,
                                                   functions,                                                   
                                               ),
                                               # Visualizations panel
                                               my_div(style_h5_panel, "",
                                                      html.H5("Visualizations", style=style_title_color)
                                               ),
                                               create_div_buttons(
                                                   style_div_2,
                                                   style_button,
                                                   visualizations,
                                               ),                                               
                                               # Models panel
                                               my_div(style_h5_panel, "",
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
