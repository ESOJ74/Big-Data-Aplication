from dash import dcc, html

from assets.common_css import background_light
from my_dash.my_dbc.my_button import my_button
from my_dash.my_dcc.my_dropdown import my_dropdown
from my_dash.my_html.my_div import my_div

style_selector_color = {
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

style_div_color = {
    "margin-left": "5%",
    "margin-top": "2%",
    "height": "12%",
    "width": "95%",
}

style_params = {
    "float": "left",
    "width": "50%",
    "color": "#acf4ed"
}

style_input = {
    "float": "left",
    "margin-left": "2%",
    "margin-bottom": "4%",
    "width": "45%",
    "background": background_light,
    "color": "black"
}

style_div_color = {
    "margin-left": "5%",
    "margin-top": "2%",
    "height": "12%",
    "width": "95%",
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
    "width": "40%"
}

def create_param_drop(id_page, id_param, options, value):
    return my_div(style_div_color, "", 
                  [
                   html.H6(id_param, style=style_params),
                   my_div(style_selector_color, "",
                          my_dropdown(f"{id_page}_{id_param}",
                                      {"background": background_light},
                                      options=options,
                                      value=value,
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
    return my_button(f"{id_page}_refresh", "Refresh", style_button_refresh,
                          className="btn btn-outline-warning", color="black")