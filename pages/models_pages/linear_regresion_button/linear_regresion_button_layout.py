from common_functions.create_layout.create_models_layout import  create_models_layout
from pages.models_pages.linear_regresion_button.linear_regresion_button_functions import \
    create_utils
from pages.models_pages.linear_regresion_button.linear_regresion_button_callbacks import *

id_page = "linear_regresion"

layout = create_models_layout(id_page, create_utils(id_page))