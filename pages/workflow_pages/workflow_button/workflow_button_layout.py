from assets.layout_templates.main_page.content_layout import \
    create_content_layout
from assets.layout_templates.panel_params.create_panel_params import *
from assets.my_dash.my_html.my_div import my_div
from ...models_pages.common_css import *
from .workflow_button_callbacks import *


params_utils = [                
                create_param_drop(id_page, "Workflow"),
                html.H4("Params", style=style_title_params),  
                create_param_drop(id_page, "color"),     
                create_param_drop(id_page, "line_group"),                          
                create_buttom_refresh(id_page)
               ]

content_up = my_div(style_div_content_up, f"{id_page}_content_up",
                      [
                       my_div(style_div_target,
                              f"{id_page}_div_derecha",
                              [
                               my_div(style_title_target, "",
                                      html.A("Workflow")
                               ),
                               my_div(style_selector_workflow, "",
                                      my_dropdown(f"{id_page}_workflow",
                                                  {"background": background_in_dropdown},
                                      ),
                               ),                                             
                              ]
                       ),                          
                       my_div(style_div_down , f"{id_page}_div_result"),
                      ])

content_down = my_div(style_div_content_down, f"{id_page}_content_down",
                      [
                          my_div(style_div_result, f"{id_page}_div_code"),
                          my_div({}, f"{id_page}_div_button_save", 
                                 my_button(f"{id_page}_button_save", "Save",
                                       style_boton_aceptar,
                                       className="btn btn-outline-warning",
                                       color="black"
                             )),
                      ])

layout = create_content_layout(id_page,
                               content_up,
                               content_down,
                               my_div(style_div_params, ""))