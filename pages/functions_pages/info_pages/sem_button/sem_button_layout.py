from common_functions.create_layout.create_functions_layout import create_functions_layout
from pages.functions_pages.info_pages.sem_button.sem_button_callbacks import *
from pages.functions_pages.info_pages.sem_button.sem_button_functions import create_utils

id_page = "sem"

layout = create_functions_layout(id_page, create_utils=create_utils(id_page))
