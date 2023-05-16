from assets.layout_templates.main_page.content_layout import \
    create_content_layout
from assets.layout_templates.panel_params.create_panel_params import *
from utils.create_div_split import create_div_split

from .logistic_regresion_button_callbacks import *

id_page = "logistic"


params_utils = [                
                html.H5("Params", style=style_title_params), 
                create_param_drop(id_page, "penalty",
                                  ["l1", "l2", "elasticnet"],
                                  "l2"),
                create_param_drop(id_page, "dual", ["True", "False"],
                                  "False"),
                create_param_drop(id_page, "fit_intercept",
                                  ["True", "False"],
                                  "True"),
                create_param_drop(id_page, "solver",
                                  ["lbfgs", "liblinear", "newton-cg",
                                   "newton-cholesky", "sag", "saga"],
                                   "lbfgs"),
                create_param_drop(id_page, "multi_class",
                                  ["auto", "ovr", "multinomial"],
                                  "auto"),
                create_param_drop(id_page, "warm_start",
                                  ["True", "False"],
                                  "False"),
                create_param_input(id_page, "tol", 1e-4),
                create_param_input(id_page, "c", 1.0),                
                create_param_input(id_page, "intercept_scaling", 1.0),
                create_param_input(id_page, "random_state", None),               
                create_param_input(id_page, "max_iter", 100),
                create_param_input(id_page, "l1_ratio", None),                
                create_param_input(id_page, "verbose", 0),
                create_param_input(id_page, "n_jobs", None),
               ]

content_down = my_div(style_content, "",
                      [
                       my_div(style_div_target, f"{id_page}_div_derecha",
                              [
                               my_div(style_title_target, "", html.A("Target", style={"color": color_boton_1})),
                               my_div(style_selector_target, "",
                                      my_dropdown(f"{id_page}_target",
                                                  {"background": background_in_dropdown},
                                                  placeholder="Select Target"
                                      ),
                               ),                       
                              ]
                       ),   
                       create_div_split(id_page),   
                       dcc.Loading(
                           id="loading-2",
                           children=[my_div({"margin-top": "1%"},
                                            f"{id_page}_model_loading")],
                           type="default",
                           fullscreen=False,
                       ),
                       my_div(style_div_down , f"{id_page}_div_result"),
                      ])


layout = create_content_layout(id_page,
                               my_div(style_div_content_up,
                                      f"{id_page}_content_up"
                               ),
                               content_down,                               
                               my_div(style_div_params,
                                      f"{id_page}_div_params",
                                      params_utils
                               ),)
