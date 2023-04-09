from dash import callback, dcc
from dash.dependencies import Input, Output, State

id_page = "bar_button"


@callback(Output(f"{id_page}_utils", "children"),
          Input("bar_button", "n_clicks"),
          prevent_initial_call=True)
def display_page(n_clicks):          
    return "bar"