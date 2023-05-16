from dash import dcc, html

from assets.common_css import *
from assets.my_dash.my_html.my_div import my_div
from assets.my_dash.my_dbc.my_button import my_button

style_title_train_test_split = {
    "margin-top": "5%",
    "margin-left": "3%",
    "width": "97%",
    "color": "black"
}

style_title_params = {
    "margin-top": "2%",
    "width": "100%",
    "text-align": "center",
    "margin-bottom": "2%",
    "color": "black"
}

style_content = {
    "width": "99%",
    "height": "99%",
}

style_div_split = {
    "margin-left": "2%",
    "width": "98%",
    "height": "10%",
}

style_title_split = {
    "margin-top": "5%",    
    "width": "100%",
    "height": "37%",
    "color": "black", 
}

style_div_input_split = {
    "float": "left",
    "margin-left": "3%",
    "margin-top": "0.1%",
    "height": "45%",
    "width": "15%",
}

style_params_split = {
    "float": "left",
    "width": "70%",
    "color": color_boton_1
}

style_input_split = {
    "float": "left",
    "margin-left": "2%",
    "width": "25%",
    "background": background_light,
    "font-size": "0.8em",
    "text-align": "right",
    "color": "black"
}

style_div_button_start = {
    "float": "left",
    "margin-left": "5%",
    "width": "20%",
    "height": "60%",
}


def create_div(id_page, title, id_input, value=None):
    return my_div(style_div_input_split, "",
                  [
                   html.A(title, style=style_params_split),
                   dcc.Input(id=id_input,
                             style=style_input_split,
                             value=value,
                   ),
                  ])



style_button_start = {
    "color": color_boton_1,
    "border": f"1px solid {color_boton_1}"
}
    

def create_div_split(id_page):
    return my_div(style_div_split, f"{id_page}_div_split",
                  [
                   my_div(style_title_split, "", html.A("train_test_split", style={"color": color_boton_1})),
                   create_div(id_page, "test_size", f"{id_page}_test_size", 20),
                   create_div(id_page, "random_state", f"{id_page}_random_state_split", 42),
                   my_div(style_div_button_start, "",
                          my_button(f"{id_page}_button_start", "Start Training",
                                    style_button_start,className="btn btn-outline-warning",
                                    color="black"))                               
                  ])    