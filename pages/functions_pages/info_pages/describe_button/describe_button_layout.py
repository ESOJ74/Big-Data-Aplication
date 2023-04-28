from common_functions.create_layout.create_functions_layout import \
    create_functions_layout
from common_functions.panel_params.create_panel_params import *
from pages.functions_pages.info_pages.describe_button.describe_button_callbacks import *

id_page = "describe"

params_utils = [
                html.H4("Params", style=style_div_params),                  
                create_param_input(id_page, "percentiles", ""), 
                create_param_drop(id_page, "include", ["", "all", 'number', "category", "object"], ""), 
                create_param_drop(id_page, "exclude", ["", 'number', "category", "object"], ""),                    
                create_buttom_refresh(id_page)
               ]

layout = create_functions_layout(id_page, create_utils=my_div(style_div_utils,
                                                              "", params_utils))
