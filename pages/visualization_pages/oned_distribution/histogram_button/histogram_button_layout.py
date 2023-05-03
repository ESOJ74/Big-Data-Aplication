from assets.layout_templates.main_page.content_layout import \
    create_content_layout
from assets.layout_templates.panel_params.create_panel_params import *

from .histogram_button_callbacks import *

id_page = "histogram"

params_utils = [                
                create_select(id_page, "X"),
                create_select(id_page, "Y"),
                html.H4("Params", style=style_title_params),  
                create_param_input(id_page, "nbins", 20),
                create_param_input(id_page, "bargap", 0),
                create_param_drop(id_page, "histnorm",
                                  options=[" ", "percent", "probability",
                                           "density", "probability density"],
                                           value=" "),  
                create_param_input(id_page, "opacity", 1),
                create_param_drop(id_page, "log_y", options=["True", "False"],
                                  value="False"),     
                create_param_drop(id_page, "color"),    
                create_param_drop(id_page, "histfunc",
                                  options=["count","sum","avg", "min", "max"],
                                  value="count"),  
                create_param_drop(id_page, "pattern_shape"),                      
                create_buttom_refresh(id_page),
               ]

content_down = my_div(style_div_content_down, f"{id_page}_content_down",
                      my_div(style_div_result, f"{id_page}_div_graph"))

layout = create_content_layout(id_page,
                               my_div(style_div_content_up, f"{id_page}_content_up"),
                               content_down,
                               my_div(style_div_params, "", params_utils))
