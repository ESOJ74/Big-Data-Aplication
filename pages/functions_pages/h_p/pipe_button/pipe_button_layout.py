
from assets.layout_templates.main_page.content_layout import \
    create_content_layout
from assets.layout_templates.panel_params.create_panel_params import *

from ....models_pages.common_css import *
from .pipe_button_callbacks import *

params_utils = [                
                create_select(id_page, "X"),
                create_select(id_page, "Y"),
                html.H4("Params", style=style_title_params),  
                create_param_drop(id_page, "color"),     
                create_param_drop(id_page, "line_group"),                          
                create_buttom_refresh(id_page)
               ]

content_down = my_div(style_content, "",
                      [
                       my_div(style_div_target,
                              f"{id_page}_div_derecha",
                              [
                               my_div(style_title_target, "",
                                      html.A("Pipe")
                               ),
                               my_div(style_selector_target_pipe, "",
                                      my_dropdown(f"{id_page}_pipe",
                                                  {"background": background_in_dropdown},
                                                  placeholder="Select Pipe"
                                      ),
                               ),
                               my_div(style_div_button_apply_pipe, "",   
                                      my_button(f"{id_page}_button_apply_pipe", "Apply Pipe",
                                      {}, className="btn btn-outline-warning",
                                      color="black"),  
                               )                
                              ]
                       ),                          
                       my_div(style_div_down , f"{id_page}_div_result"),
                      ])

layout = create_content_layout(id_page,
                               my_div(style_div_content_up, f"{id_page}_content_up"),
                               content_down,
                               my_div(style_div_params, ""))