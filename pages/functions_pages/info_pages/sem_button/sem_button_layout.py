from assets.layout_templates.main_page.content_layout import \
    create_content_layout
from assets.layout_templates.panel_params.create_panel_params import *

from .sem_button_callbacks import *

id_page = "sem"



params_utils = [
                create_param_buttons_text_graph(id_page),
                html.H4("Params", style=style_title_params),  
                create_param_drop(id_page, "axis", [0, 1], 0),
                create_param_drop(id_page, "skipna", ["True", "False"], "True"),
                create_param_drop(id_page, "numeric_only", ["True", "False"], "False"),                 
                create_param_input(id_page, "ddof"),
                create_buttom_refresh(id_page)
               ]

layout = create_content_layout(id_page,
                               my_div(style_div_content_up, f"{id_page}_content_up"),
                               my_div(style_div_content_down, f"{id_page}_content_down"),
                               my_div(style_div_params,
                                      "", params_utils))
