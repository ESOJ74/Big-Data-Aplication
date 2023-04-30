from assets.common_css import *

from ..imports import *
from .functions.button_cover import button_cover
from .functions.left_panel import left_panel

style_middle_panel = {
    "margin-top": "0.2%",
    "width": "100%",
    "height": "88.6%",
    "background": background_dark
}

style_div_content = {
    "float": "left",
    "width": "82%",
    "height": "100%",
}

style_div_content2 = {
    "float": "left",
    "width": "100%",
    "height": "100%",
}

def middle_panel(id_page):
    return my_div(style_middle_panel, "",
                  [    
                   button_cover(id_page),                                       
                   left_panel(id_page),
                   my_div(style_div_content,
                          f"{id_page}_page_content"
                   ),                               
                  ])
