from common_functions.create_models_layout import create_models_layout
from pages.models_pages.logistic_regresion_button.logistic_regresion_button_callbacks import *
from pages.models_pages.logistic_regresion_button.logistic_regresion_button_functions import create_utils

id_page = "logistic_regresion"

layout = create_models_layout(id_page, create_utils(id_page))