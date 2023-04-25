from common_functions.create_visualization_layout import \
    create_visualization_layout
from pages.visualization_pages.histogram_button.histogram_button_callbacks import *
from pages.visualization_pages.histogram_button.histogram_button_functions import create_utils

id_page = "histogram"

layout = create_visualization_layout(id_page, create_utils(id_page))