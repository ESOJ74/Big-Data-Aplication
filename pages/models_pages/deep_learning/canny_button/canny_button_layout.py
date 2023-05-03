from assets.layout_templates.main_page.content_layout import \
    create_content_layout
from assets.layout_templates.panel_params.create_panel_params import *

from .canny_button_callbacks import *

id_page = "canny"

content_down = my_div(style_content, "",
                      [
                       my_div(style_div_drop_foto, f"{id_page}_div_derecha",
                              [                               
                               my_div(style_selector_foto, "",
                                      my_dropdown(f"{id_page}_drop_foto",
                                                  {"background": background_in_dropdown},
                                                  placeholder="Select Foto"
                                      ),
                               ),
                               my_button(f"{id_page}_up_foto", "Up Foto from Local",
                                   style_div_button_foto,
                                   className="btn btn-outline-primary",
                                   color="black"
                         ),                 
                              ]
                       ),                          
                       dcc.Loading(
                           id="loading-2",
                           children=[my_div({"margin-top": "1%"},
                                            f"{id_page}_model_loading")],
                           type="default",
                           fullscreen=False,
                       ),
                       my_div(style_div_down , f"{id_page}_div_result"),
                      ])

params_utils = [                
                html.H5("Params", style=style_title_params),                 
                create_param_input(id_page, "threshold1", 100),
                create_param_input(id_page, "threshold2", 200),                
                create_param_input(id_page, "aperture_size", 3),
                create_param_drop(id_page, "L2gradient", ["True", "False"],
                                  "False"),
                create_buttom_refresh(id_page)
               ]
layout = create_content_layout(id_page,
                               my_div(style_div_content_up,
                                      f"{id_page}_content_up"
                               ),
                               content_down,                           
                               my_div(style_div_params,
                                      f"{id_page}_div_params",
                                      params_utils
                               ),)
