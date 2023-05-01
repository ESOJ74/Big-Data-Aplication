from dash import dcc, html

from assets.layout_templates.main_page.common_css import *
from assets.my_dash.my_dbc.my_button import my_button
from assets.my_dash.my_dcc.my_dropdown import my_dropdown
from assets.my_dash.my_html.my_div import my_div

style_div_selector = {
    "margin-left": "5%",
    "margin-top": "2%",
    "height": "12%",
    "width": "95%",
}

style_selector = {
    "float": "left",
    "margin-left": "2%",
    "width": "45%",
    "height": "3.2em",
    "border-radius": "7px 7px 5px 5px",
    "padding": "2px 2px 0px 2px",
    "font-size": "0.8em",
    "color": "black",
    "background": "#2f6374",
}

style_params = {
    "float": "left",
    "width": "50%",
    "color": color_boton_1
}

style_div_selector2 = {
    "margin-top": "3%",
    "margin-left": "5%",
    "height": "7%",
    "width": "95%",
}

style_selector2 = {
    "float": "left",
    "width": "70%",
    "height": "3.2em",
    "border-radius": "7px 7px 5px 5px",
    "padding": "2px 2px 0px 2px",
    "font-size": "0.8em",
    "color": "black",
    "background": "#2f6374",
}

style_params2 = {
    "float": "left",
    "width": "20%",
    "color": color_boton_1
}

style_input = {
    "float": "left",
    "margin-left": "2%",
    "margin-bottom": "4%",
    "width": "45%",
    "background": background_light,
    "color": "black"
}

style_div_buttons = {
    "margin-top": "2%",
    "width": "100%",
    "height": "8%",
}

style_button = {
    "float": "left",
    "margin-top": "5%",
    "margin-left": "5%",
    "width": "40%"
}

style_button_refresh = {
    "margin-top": "35%",
    "margin-left": "5%",
    "width": "10vmax"
}

style_button_save = {
    "margin-top": "5%",
    "margin-left": "5%",
    "width": "10vmax"
}


def create_select(id_page, id_param, options=[], value="", multi=False):
    return my_div(style_div_selector2, "", 
                  [
                   html.H6(id_param, style=style_params2),
                   my_div(style_selector2, "",
                          my_dropdown(f"{id_page}_{id_param}",
                                      {"background": background_light},
                                      options=options,
                                      value=value,
                                      multi=multi
                          ),
                   )                                           
                  ])


def create_param_drop(id_page, id_param, options=[], value="", multi=False):
    return my_div(style_div_selector, "", 
                  [
                   html.H6(id_param, style=style_params),
                   my_div(style_selector, "",
                          my_dropdown(f"{id_page}_{id_param}",
                                      {"background": background_light},
                                      options=options,
                                      value=value,
                                      multi=multi
                          ),
                   )                                           
                  ])

def create_param_input(id_page, id_param, value=1):
    return my_div({"margin-left": "5%"}, "",
                  [
                   html.H6(id_param, style=style_params),
                   dcc.Input(id=f"{id_page}_{id_param}",
                             style=style_input,
                             value=value,
                   ),
                  ])

def create_param_buttons_text_graph(id_page):
    return my_div(style_div_buttons, "",
                       [
                        my_button(f"{id_page}_text", "Text", style_button,
                                  className="btn btn-warning", color="black",
                                  n_clicks=1
                        ),
                        my_button(f"{id_page}_graph", "Graph", style_button,
                                  className="btn btn-outline-warning",
                                  color="black"
                        ),        
                       ]
                )


def create_buttom_refresh(id_page):
    return my_button(f"{id_page}_refresh", "Apply", style_button_refresh,
                     className="btn btn-outline-warning", color="black")


def create_buttom_save(id_page):
    return my_button(f"{id_page}_save", "Save changes", style_button_save,
                     className="btn btn-outline-warning", color="black",
                     disabled=True)