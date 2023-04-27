from common_functions.create_functions_layout import create_functions_layout
from pages.functions_pages.kurt_button.kurt_button_callbacks import *
from pages.functions_pages.kurt_button.kurt_button_functions import \
    create_utils

id_page = "kurt"

layout = create_functions_layout(id_page, create_utils=create_utils(id_page))
