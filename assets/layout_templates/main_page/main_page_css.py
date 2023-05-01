from dash import html, dcc
from dash_iconify import DashIconify
from ...my_dash.my_dbc.my_button import my_button

from assets.layout_templates.main_page.common_css import *

from ...my_dash.my_html.my_div import my_div

#up panel
style_up_panel = {
    "width": "100%",
    "height": "5%",    
    "background": background_up_panel
}

style_div_user = {
    "float": "left",
    "width": "10%",
}

style_user = {
    "margin-left": "15%",
    "margin-top": "5%",
}

style_div_app = {
    "float": "left",
    "width": "83%",
}

style_app = {
    "margin-left": "35%",
    "margin-top": "0.3%",
    "color": color_boton_1,
}

style_div_sesion = {
    "float": "left",
    "width": "7%",
}

style_sesion = {
    "margin-top": "6%"
}

# Middle Panel
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

# Down Panel
style_down_panel = {
    "margin-top": "0.2%",
    "width": "100%",
    "height": "5%",
    "background": background_up_panel,
}

#Button Cover
style_div_button_cover_right ={
    "position": "absolute",
    "left": "15.1vmax",
    "top": "5.4%",
}

style_button_cover_right = {
    "background": "#04212c",
    "border": "0px solid #2a9fd6",
    "border-radius": "80px",
    "color": color_boton_1,    
}

style_div_button_cover_left ={
    "position": "absolute",    
    "top": "5.4%",
    "border-left": "2.5px solid black",
}

style_button_cover_left = {
    "background": "#204765",
    "border": "0px solid #060606",
    "border-radius": "80px",
    "color": color_boton_1,
}

# Left Panel
style_div_middle_left = {
    "float": "left",
    "width": "18%",
    "height": "100%", "border-right": "2px solid black",
    "background": backgroud_left_panel,
}
