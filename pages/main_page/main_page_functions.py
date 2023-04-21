from importlib import import_module

from dash import callback
from dash.dependencies import Input, Output
from dash_iconify import DashIconify

from my_dash.my_dbc.my_button import my_button
from my_dash.my_html.my_div import my_div


def button_left_right(id, className, style, icon):
    return my_button(id, 
                     DashIconify(
                          icon=icon,   #2a9fd6
                          width=30
                     ),
                     style, #{"position": "absolute","left": "0%", "top": "43px", "background": "#060606", "border": "1px solid #060606"},
                     n_clicks=0,
                     className=className) #"btn btn-primary disabled btn-sm")


def create_div_buttons(style_div, style_button, button_list, color="black", classdiv="", className="btn btn-outline-light"):   
    return my_div(style_div, "", 
                  [
                   *[my_div({ "float": "left", "margin-top": "0%", "width": "32%", "font-weight": "bold"}, "",
                             my_button(button[0],
                                       button[1],
                                       style_button,
                                       color=color,
                                       className=className)
                      ) for button in button_list]
                   ], className=classdiv,
           )


def create_callback(buttons_list, module, button_name=""):
    @callback(
        [Output("main_page_page_content", "children", allow_duplicate=True)] +
        list(map(lambda x: Output(x[0], "n_clicks"), buttons_list)),
        list(map(lambda x: Input(x[0], "n_clicks"), buttons_list)),
        prevent_initial_call=True)
    def display_page(*args):
        button = buttons_list[list(args).index(1)][0]
        try:
            cont = [import_module(f'pages.{module}.{button}.{button}_layout').layout]
        except ModuleNotFoundError:
            cont = [f"{button_name} no implementada"]
        return cont + [0 for x in buttons_list]
