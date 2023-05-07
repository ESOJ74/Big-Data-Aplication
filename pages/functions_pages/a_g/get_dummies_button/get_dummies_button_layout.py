from assets.layout_templates.main_page.content_layout import \
    create_content_layout
from assets.layout_templates.panel_params.create_panel_params import *

from .get_dummies_button_callbacks import *

params_utils = [
                my_div(style_div_buttons, ""),
                html.H4("Params", style=style_title_params),  
                create_param_drop(id_page, "prefix", multi=True),
                create_param_drop(id_page, "dummy_na",
                                  ["True", "False"], "False"),      
                create_param_drop(id_page, "columns", multi=True),  
                create_param_drop(id_page, "sparse",
                                  ["True", "False"], "False"),
                create_param_drop(id_page, "drop_first",
                                  ["True", "False"], "False"),   
                create_param_drop(id_page, "dtype",
                                  ["int", "float", "str", "bool"], "bool"),  
                create_buttom_refresh(id_page),
               ]

content_down = my_div(style_div_content_down, f"{id_page}_content_down",
                      my_div(style_div_result, f"{id_page}_div_graph"))

layout = create_content_layout(id_page,
                               my_div(style_div_content_up, f"{id_page}_content_up"),
                               content_down,
                               my_div(style_div_params, "", params_utils))
