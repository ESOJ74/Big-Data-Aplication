from dash import dcc
from .common_css import *
from assets.my_dash.my_html.my_div import my_div

style_content_left = {
    "float": "left",
    "position": "relative",
    "top": "0%",
    "left": "0%",
    "width": "85%",
    "height": "100%",
}

style_content_right = {
    "float": "left",
    "width": "15%",
    "height": "100%",
    "border-left": "2px solid black",
    "background": background_utils,
}

style_content_left_up = {
    "position": "relative",
    "top": "0%",
    "left": "0%",
    "width": "100%",
    "height": "10.7%",
}

style_content_left_down = {
    "width": "100%",
    "height": "89.3%",
}

def create_content_layout(id_page, content_left_up, content_left_down, content_right):
    return my_div(style_div_main, f"{id_page}_content_layout",
                  [
                   my_div(style_content_left, f"{id_page}_content_left",
                          [
                           my_div(style_content_left_up, f"{id_page}_content_left_up",
                                  content_left_up
                           ),
                           dcc.Loading( 
                               id="loading-2",
                               children=my_div({},
                                               f"{id_page}_loading"),
                               type="default",
                               fullscreen=False,
                           ),
                           my_div(style_content_left_down, f"{id_page}_content_left_down",
                                  content_left_down
                           )  
                          ]
                   ),
                   my_div(style_content_right, f"{id_page}_content_right",
                          content_right
                   ),                      
                  ])
