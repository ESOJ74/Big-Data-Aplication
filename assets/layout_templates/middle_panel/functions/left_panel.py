from assets.layout_templates.imports import *

from .left_panel_css import *


def title(title, style):
    return my_div(style, "",
                  html.H5(title, style={"color": "#0F1458"}))


def button_drop(id, name, style):
    return my_button(id, name,
                     style, color="black",
                     className="btn btn-outline-primary dropdown-toggle")


def create_div_buttons(style_div, style_div_button, style_button, button_list, color="black",
                       classdiv="", className="btn btn-outline-light"):      
    return my_div(style_div, "", 
                  [
                   *[my_div(style_div_button, "",
                             my_button(button[0],
                                       button[1],
                                       style_button,
                                       color=color,
                                       className=className)
                      ) for button in button_list]
                   ], className=classdiv,)


def panel_dataFrame(id_page):
    return my_div(style_div_data, "",
                          [
                           title("DataFrame", style_title_data ),
                           my_div({"width": "100%", "height": "30%"},
                                  f"{id_page}_content_data",
                                  [
                                   my_div(style_div_button_data, "",
                                          button_drop(f"{id_page}_button_data",
                                                     "Data", style_button_data
                                          )
                                   ),
                                   my_div(style_div_button_view, "",
                                          create_div_buttons(
                                              style_div_0,
                                              style_div_button2,
                                              style_button_data,
                                              buttons,
                                              classdiv="table-success"                                           
                                          ),
                                   ),                                    
                                  ]
                           ),
                           my_div(style_div_div_data,
                                  f"{id_page}_div_data",
                                  create_div_buttons(
                                      style_div_1,
                                      style_div_button2,
                                      style_button1,
                                      buttons_data,
                                      classdiv="table-success"                                           
                                  ),
                                  hidden=True
                           ),
                          ])


def panel_functions(id_page):
    return my_div(style_border, "",
                  [
                    title("Functions", style_title),
                          my_div(style_div_button_drop_info, "",
                                 button_drop(f"{id_page}_button_drop_info", "Info",
                                             style_button_drop_info
                                 ),                                      
                          ),
                    my_div(style_div_buttons_info,
                           f"{id_page}_div_buttons_info",                                                      
                           create_div_buttons(
                                style_div_buttons_functions,
                                style_div_button,
                                style_button2,
                                functions_info,                                                   
                           ), hidden=True
                    ),
                    my_div(style_div_buttons_func, 
                           f"{id_page}_div_buttons",
                           create_div_buttons(
                               style_div_buttons_functions,
                               style_div_button,
                               style_button,
                               functions,                                                   
                           ), hidden=False
                    )
                   ])


def panel_visualizations(id_page):
    return my_div(style_border, "",
                  [
                   title("Visualizations", style_title),
                   create_div_buttons(
                        style_div_2,
                        style_div_button,
                        style_button,
                        visualizations,
                   )
                  ])


def panel_models(id_page):
    return my_div(style_border, "",
                  [
                   title("Models", style_title),
                   create_div_buttons(
                        style_div_2,
                        style_div_button,
                        style_button,
                        models,
                   )
                  ])


def left_panel(id_page):
    return my_div(style_div_middle_left,
                  f"{id_page}_div_middle_left",
                  [       
                   # DataFrame panel
                   panel_dataFrame(id_page),
                   # Div for Visualizations panel, Functions panel, Models panel
                   my_div({"height": "70%"},                          
                          f"{id_page}_div_functions",
                          [
                           # Functions panel
                           panel_functions(id_page),
                           # Visualizations panel
                           panel_visualizations(id_page),                                               
                           # Models panel
                           panel_models(id_page),
                          ],
                          hidden=True,
                   ),
                  ],
                  className="alert-primary",
                  hidden=True,)