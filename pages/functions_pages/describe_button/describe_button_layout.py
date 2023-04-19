from dash import Input, Output, State, callback, dcc, html
from pandas import read_json

from my_dash.my_html.my_div import my_div

style_div_content = {
    "position": "relative",
    "top": "10%",
    "left": "10%",
    "width": "70%",
    "font-size": "1.2em",
    "font-weight": "bold",
    "background": "#C5F4FD",
    "color": "#03353E",    
}

id_page = "describe"

layout = [
          dcc.Loading(
              id="loading-2",
              children=[my_div({"margin-top": "10%"}, f"{id_page}_describe_loading")],
              type="default",
              fullscreen=False,
          ),
          my_div(style_div_content, f"{id_page}_content")
]


@callback(
        [
         Output(f"{id_page}_content", "children"),
         Output(f"{id_page}_describe_loading", "children", allow_duplicate=True),
        ],
        Input("info_button", "n_clicks"),
        State("main_page_store", "data"),
    prevent_initial_call=True,)
def add_data_to_fig(n_clicks, data):     
    return [my_div({"text-align": "center"}, "",
                  html.Pre(read_json(data["df"]).describe().__str__())), ""]