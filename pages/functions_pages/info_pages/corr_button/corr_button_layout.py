from common_functions.create_layout.create_functions_layout import create_functions_layout
from pages.functions_pages.info_pages.corr_button.corr_button_callbacks import *
from common_functions.panel_params.create_panel_params import *

id_page = "corr"

params_utils = [
                create_param_buttons_text_graph(id_page),
                html.H4("Params", style=style_div_params),  
                create_param_drop(id_page, "method", ["pearson", "kendall", "spearman"], "pearson"),
                create_param_drop(id_page, "numeric_only", ["True", "False"], "False"),
                create_param_input(id_page, "min_periods"),
                create_buttom_refresh(id_page)
               ]

layout = create_functions_layout(id_page, create_utils=my_div(style_div_utils,
                                                              "", params_utils))
