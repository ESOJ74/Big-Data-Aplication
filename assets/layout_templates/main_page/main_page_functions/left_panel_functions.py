from pages.main_page.main_page_lists import *

from ..main_page_css import *
from .left_panel_functions_css import *


def title(title, style):
    return my_div(style, "",
                  html.H5(title, style={"color": "#0F1458"}))


def button_drop(id, name, style):
    return my_button(id, name,
                     style, color="black",
                     className="btn btn-outline-primary dropdown-toggle")


def div_button_drop(id_button, title):
    return my_div(style_div_button_drop_info, "",
                  button_drop(id_button, title,
                              style_button_drop))


def create_div_buttons(style_div, style_div_but, style_button, button_list,
                       color="black", classdiv="",
                       className="btn btn-outline-light"):      
    return my_div(style_div, "", 
                  [
                   *[my_div(style_div_but, "",
                             my_button(button[0],
                                       button[1],
                                       style_button,
                                       color=color,
                                       className=className)
                      ) for button in button_list]
                   ], className=classdiv,)


def hidden_button_group(id_group, group_list):
    return my_div(style_div_buttons_hidden,
                  id_group,                                                      
                  create_div_buttons(
                      style_content_buttons_hidden,
                      style_div_button_hidden,
                      style_button2,
                      group_list,                                                   
                  ),
                  hidden=True)


def button_group(id_group, group_list):
    return my_div(style_div_buttons_func,
                  id_group,                                                      
                  create_div_buttons(
                      style_content_buttons,
                      style_div_button,
                      style_button,
                      group_list,                                                   
                  ),
                  hidden=False)


def create_div_title_panel(title_panel, id_button):
    return my_div(style_div_title_panel, "",
                          [
                           title(title_panel, style_title),
                           my_button(id_button,
                               DashIconify(
                                   icon="ic:baseline-list",
                                   width=30,
                                   height=30
                               ),
                               style_button_show,
                               className="btn btn-outline-primary",
                               color="Black"
                           ),                           
                          ])


def create_div_buttons_panel(id_panel, children):
    return my_div(style_div_panel_buttons,
                  id_panel, children, hidden=True)


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
                   create_div_title_panel("Functions", "button_show_functions"),
                   create_div_buttons_panel("panel_functions",
                       [
                        div_button_drop(f"{id_page}_button_drop_info",
                                        "Info"
                        ),
                        hidden_button_group(f"{id_page}_div_buttons_info",
                                             functions_info
                        ),    
                        div_button_drop(f"{id_page}_button_a_g",
                                        "A-G"
                        ),
                        hidden_button_group(f"{id_page}_div_buttons_a_g",
                                             functions_a_g
                        ),
                        div_button_drop(f"{id_page}_button_h_p",
                                        "H-P"
                        ),
                        hidden_button_group(f"{id_page}_div_buttons_h_p",
                                             functions_h_p
                        ),
                        div_button_drop(f"{id_page}_button_q_z",
                                        "Q-Z"
                        ),
                        hidden_button_group(f"{id_page}_div_buttons_q_z",
                                             functions_q_z
                        ),                          
                       ]
                   )
                  ])


def panel_visualizations(id_page):
    return my_div(style_border, "",
                  [
                   create_div_title_panel("Visualizations",
                                          "button_show_visualizations"
                   ),
                   create_div_buttons_panel("panel_visualizations",
                          [
                           div_button_drop(f"{id_page}_button_basics", "Basics"),
                           hidden_button_group(f"{id_page}_div_buttons_basics",
                                               visualizations_basic),
                           div_button_drop(f"{id_page}_button_part_of_whole",
                                           "Part Of Whole"),                   
                           hidden_button_group(f"{id_page}_div_buttons_part_of_whole",
                                               visualizations_part_of_whole),    
                           div_button_drop(f"{id_page}_button_1d_distribution",
                                           "1D Distribution"),                   
                           hidden_button_group(f"{id_page}_div_buttons_1d_distribution",
                                               visualizations_1d_distribution),
                           div_button_drop(f"{id_page}_button_2d_distribution",
                                           "2D Distribution"),                   
                           hidden_button_group(f"{id_page}_div_buttons_2d_distribution",
                                               visualizations_2d_distribution),
                           div_button_drop(f"{id_page}_button_3d_dimensional",
                                           "3D Dimensional"),                   
                           hidden_button_group(f"{id_page}_div_buttons_3d_dimensional",
                                               visualizations_three_dimensional),
                          ],  
                   )
                  ])


def panel_models(id_page):
    return my_div(style_border, "",
                  [                   
                   create_div_title_panel("Models", "button_show_models"),
                   create_div_buttons_panel("panel_models",
                          [
                           div_button_drop(f"{id_page}_button_machine",
                                           "Machine Learning"),
                           hidden_button_group(f"{id_page}_div_buttons_machine",
                                               models_supervised),
                           div_button_drop(f"{id_page}_button_deep", "Deep Learning"),  
                           hidden_button_group(f"{id_page}_div_buttons_deep", models_deep),  
                           div_button_drop(f"{id_page}_button_existing_models",
                                           "Existing Models"), 
                           hidden_button_group(f"{id_page}_div_buttons_existing_models",
                                               existing_models), 
                           button_group(f"{id_page}_div_buttons_test_model", models_test),
                          ]  
                   )          
                  ])

def panel_workflow(id_page):
    return my_div(style_border, "",
                  [                   
                   create_div_title_panel("Workflow", "button_show_workflow"),
                   create_div_buttons_panel("panel_workflow",
                          [
                           button_group(f"{id_page}_div_workflow",
                                        workflow
                           ),    
                          ]  
                   )          
                  ])
