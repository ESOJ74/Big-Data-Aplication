from importlib import import_module

from dash import callback
from dash.dependencies import Input, Output

from my_dash.my_dbc.my_button import my_button
from my_dash.my_html.my_div import my_div

style_div_button = {
    "float": "left", "margin-left": "0.8%", "width": "32%", "font-weight": "bold"
}

def button_cover(id, className, style, children):
    return my_button(id, 
                     children,
                     style, 
                     n_clicks=0,
                     className=className)


def create_div_buttons(style_div, style_button, button_list, color="black",
                       classdiv="", className="btn btn-outline-light"):      
    return my_div(style_div, "", 
                  [
                   *[my_div(style_div_button, "",
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
        list(map(lambda x: Output(x[0], "n_clicks"), buttons_list)) +
        [Output("main_page_div_button_cover", "hidden", allow_duplicate=True)],
        list(map(lambda x: Input(x[0], "n_clicks"), buttons_list)),
        prevent_initial_call=True)
    def display_page(*args):
        button = buttons_list[list(args).index(1)][0]
        try:
            cont = [import_module(f'pages.{module}.{button}.{button}_layout').layout]
        except ModuleNotFoundError:
            cont = [f"{button_name} no implementada"]
        return cont + [0 for x in buttons_list] + [True]
