from .left_panel import left_panel

from .main_page_css import *
from .main_page_functions.button_cover import *


def middle_panel(id_page):
    return my_div(style_middle_panel, "",
                  [    
                   button_cover(id_page),                                       
                   left_panel(id_page),
                   my_div(style_div_content,
                          f"{id_page}_page_content"
                   ),                               
                  ])
