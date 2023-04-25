import os

from dash import Input, Output, State, callback, dcc, html
from pandas import read_csv, read_json

from common_functions.create_agGrid import create_adgrid
from common_functions.create_callback_button_cover import \
    create_callback_button_cover
from my_dash.my_html.my_div import my_div

style_div_content = {
    "position": "relative",
    "top": "-1vmax",
    "left": "3%",
    "width": "95%",
    "font-size": "1.2em",
    "font-weight": "bold",
}

id_page = "t"

layout = [
          dcc.Loading(
              id="loading-2",
              children=[my_div({"margin-top": "10%"}, f"{id_page}_t_loading")],
              type="default",
              fullscreen=False,
          ),
          my_div(style_div_content, f"{id_page}_content")
]


@callback(
        [
         Output(f"{id_page}_content", "children"),
         Output(f"{id_page}_t_loading", "children", allow_duplicate=True),
        ],
        Input("t_button", "n_clicks"),
        State("main_page_store", "data"),
    prevent_initial_call=True,)
def add_data_to_fig(n_clicks, data):     
    obj = []
    try:        
        df = read_json(data["df"]).head().T.reset_index()        
        df.rename(columns={'index': 'columns'}, inplace=True)
        df.to_csv("tmp.csv", index=False)
        df = read_csv("tmp.csv")    
        os.remove("tmp.csv")           
        obj.append(create_adgrid(f"{id_page}_ag-table", df))
        obj.append(False)
    except (TypeError, KeyError, ValueError):
        obj = [html.H6('No hay ningún DataFrame Cargado',
                       style={"margin-left": "20%", "color": "#b0d8d3"}), True]
    return obj


create_callback_button_cover(id_page)