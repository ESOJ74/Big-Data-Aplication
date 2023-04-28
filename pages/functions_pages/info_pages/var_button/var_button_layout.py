from common_functions.create_layout.create_functions_layout import \
    create_functions_layout
from common_functions.panel_params.create_panel_params import *
from pages.functions_pages.info_pages.var_button.var_button_callbacks import *

id_page = "var"

params_utils = [
                create_param_buttons_text_graph(id_page),
                html.H4("Params", style=style_div_params),  
                create_param_drop(id_page, "axis", [0, 1], 0),
                create_param_drop(id_page, "skipna", ["True", "False"], "True"),
                create_param_drop(id_page, "numeric_only", ["True", "False"], "False"),                 
                create_param_input(id_page, "ddof"),
                create_buttom_refresh(id_page)
               ]

layout = create_functions_layout(id_page, create_utils=my_div(style_div_utils,
                                                              "", params_utils))