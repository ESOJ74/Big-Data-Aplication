from dash import dcc, html

from common_functions.create_layout.create_models_layout import create_models_layout
from my_dash.my_html.my_div import my_div
from pages.models_pages.logistic_regresion_button.logistic_regresion_button_callbacks import *
from pages.models_pages.logistic_regresion_button.logistic_regresion_button_css import *
from pages.models_pages.logistic_regresion_button.logistic_regresion_button_functions import \
    create_utils

id_page = "logistic_regresion"


def create_models_layout(id_page, create_utils):
    return my_div(style_main_div, "",
                  [                   
                   my_div(style_div_content, "",
                          [
                           my_div(style_div_title, "",
                                  html.H5(f"{' '.join(id_page.split('_'))}",
                                          style = {"color": "#acf4ed"}),
                           ),
                           my_div(style_div_content_up, f"{id_page}_content_up"),
                           dcc.Loading(
                               id="loading-2",
                               children=[my_div({}, f"{id_page}_model_loading")],
                               type="default",
                               fullscreen=False,
                           ),
                           my_div(style_div_content_middle, f"{id_page}_content_middle"),
                           my_div(style_div_content_down, f"{id_page}_content_down"),
                          ]
                   ),
                   my_div(style_div_content_utils, f"{id_page}_utils", create_utils)
                  ])

layout = create_models_layout(id_page, create_utils(id_page))