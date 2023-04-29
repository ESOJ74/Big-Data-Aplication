from dash import dcc

from assets.layout_templates.down_panel import down_panel
from assets.layout_templates.middle_panel import middle_panel
from assets.layout_templates.up_panel import up_panel
from common_functions.user_registry import user_login
from my_dash.my_html.my_div import my_div
from pages.main_page.main_page_callbacks import *

id_page = "main_page"

style_div_main = {
    "position": "absolute",
    "left": "0px",
    "top": "0px",
    "width": "100%",
    "height": "100%",
    "font-family": "Roboto, Helvetica, Arial, sans-serif",
}

layout: dict = my_div(style_div_main, "",
                      [
                       dcc.Store(id=f"{id_page}_store"),        
                       user_login(id_page),   
                       # Up Panel
                       up_panel.up_panel(id_page),           
                       # Middle Panel                 
                       middle_panel.middle_panel(id_page),
                       # Down Panel
                       down_panel.down_panel(),
                      ]
               )
