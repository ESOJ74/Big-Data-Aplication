from importlib import import_module

from dash import callback, dcc, html
from dash.dependencies import Input, Output
from dash_iconify import DashIconify

from assets.common_css import (backgroud_left_panel, background_light,
                               background_up_panel)
from assets.my_dash.my_dbc.my_button import my_button
from assets.my_dash.my_html.my_div import my_div
from pages.main_page.main_page_lists import (buttons, buttons_data, functions,
                                             functions_info, models,
                                             visualizations)
