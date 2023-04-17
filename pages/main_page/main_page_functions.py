from importlib import import_module

from dash import callback, html
from dash.dependencies import Input, Output

from my_dash.my_dbc.my_button import my_button
from my_dash.my_html.my_div import my_div


def create_div_buttons(style_div, style_button, button_list, color="black", classdiv="", className="btn btn-outline-light"):   
    return my_div(style_div, "", 
                  [
                   *[my_div({"margin-top": "0%", "width": "90%", "font-weight": "bold"}, "",
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
