from common_functions.create_functions_layout import create_functions_layout
from pages.functions_pages.info_pages.corr_button.corr_button_callbacks import *
from pages.functions_pages.info_pages.corr_button.corr_button_functions import create_utils

id_page = "corr"

layout = create_functions_layout(id_page, create_utils=create_utils(id_page))
