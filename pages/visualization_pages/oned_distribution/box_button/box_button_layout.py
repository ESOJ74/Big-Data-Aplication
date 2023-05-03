from assets.layout_templates.main_page.content_layout import \
    create_content_layout
from assets.layout_templates.panel_params.create_panel_params import *

from .box_button_callbacks import *

id_page = "box"

params_utils = [                
                create_select(id_page, "X"),
                create_select(id_page, "Y"),
                html.H4("Params", style=style_title_params),  
                create_param_drop(id_page, "points",
                                  options=["False", "all",
                                           "outliers", 'suspectedoutliers'],
                                  value="outliers"
                ),  
                create_param_drop(id_page, "color"),   
                create_param_drop(id_page, "quartilemethod",
                                  options=["exclusive", "inclusive",
                                           "linear"],
                                  value="linear"
                ),       
                create_param_drop(id_page, "notched",
                                  options=["True", "False"], value="False"
                ),       
                create_param_drop(id_page, "hover_data"),              
                create_buttom_refresh(id_page)
               ]

content_down = my_div(style_div_content_down, f"{id_page}_content_down",
                      my_div(style_div_result, f"{id_page}_div_graph"))

layout = create_content_layout(id_page,
                               my_div(style_div_content_up, f"{id_page}_content_up"),
                               content_down,
                               my_div(style_div_params, "", params_utils))
