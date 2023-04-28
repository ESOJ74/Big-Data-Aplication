from common_functions.create_layout.create_visualization_layout import \
    create_visualization_layout
from pages.visualization_pages.boxplot_button.boxplot_button_callbacks import *
from pages.visualization_pages.boxplot_button.boxplot_button_functions import create_utils

id_page = "boxplot_button"

layout = create_visualization_layout(id_page, create_utils(id_page))