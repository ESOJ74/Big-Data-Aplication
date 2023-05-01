from assets.layout_templates.main_page.down_panel import down_panel
from assets.layout_templates.main_page.main_page_css import *
from assets.layout_templates.main_page.middle_panel import middle_panel
from assets.layout_templates.main_page.up_panel import up_panel
from assets.my_dash.my_html.my_div import my_div
from pages.main_page.main_page_callbacks import *
from utils.user_registry import user_login

id_page = "main_page"

style_div_main = {
    "position": "absolute",
    "left": "0px",
    "top": "0px",
    "width": "100%",
    "height": "100%",
    "font-family": font_family,
}

layout = my_div(style_div_main, "",
                [
                 dcc.Store(id=f"{id_page}_store"),        
                 user_login(id_page),   
                 # Up Panel
                 up_panel(id_page),           
                 # Middle Panel                 
                 middle_panel(id_page),
                 # Down Panel
                 down_panel(),
                ])
