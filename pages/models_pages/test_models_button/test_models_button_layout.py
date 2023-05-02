from assets.layout_templates.main_page.content_layout import \
    create_content_layout
from assets.layout_templates.panel_params.create_panel_params import *

from .test_models_button_callbacks import *

id_page = "test_models"

content_up = my_div(style_content, "",
                    [
                     my_div(style_div_drop_test, f"{id_page}_div_test_left",
                            [
                             my_div(style_title_test_left, "", html.A("Model Type")),
                                    my_div(style_selector_test, "",
                                           my_dropdown(f"{id_page}_test_left",
                                                       {"background": background_in_dropdown},
                                                       placeholder="Select model"
                                           ),
                                    ),  
                            my_div(style_title_test_right, "", html.A("Model")),
                                    my_div(style_selector_test_right, "",
                                           my_dropdown(f"{id_page}_test_right",
                                                       {"background": background_in_dropdown},
                                                       placeholder="Select model"
                                           ),
                                    ),                     
                            ]
                     ),   
                               
                    ])
content_down = my_div(style_content, "",
                      [                     
                       dcc.Loading(
                               id="loading-2",
                               children=[my_div({"margin-top": "1%"}, f"{id_page}_test_model_loading")],
                               type="default",
                               fullscreen=False,
                       ),
                       my_div(style_div_down , f"{id_page}_div_result"),
                      ])


layout = create_content_layout(id_page,
                               content_up,
                               content_down,                               
                               my_div(style_div_params, f"{id_page}_div_params", ""),)