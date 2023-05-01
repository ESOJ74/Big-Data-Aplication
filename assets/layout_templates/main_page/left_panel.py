from .main_page_functions.left_panel_functions import *

from .main_page_css import *


def left_panel(id_page):
    return my_div(style_div_middle_left,
                  f"{id_page}_div_middle_left",
                  [       
                   # DataFrame panel
                   panel_dataFrame(id_page),
                   # Div for Visualizations panel, Functions panel, Models panel
                   my_div({"height": "70%"},                          
                          f"{id_page}_div_functions",
                          [
                           # Functions panel
                           panel_functions(id_page),
                           # Visualizations panel
                           panel_visualizations(id_page),                                               
                           # Models panel
                           panel_models(id_page),
                          ],
                          hidden=True,
                   ),
                  ],
                  className="alert-primary",
                  hidden=True,)
