from dash import callback, html
from dash.dependencies import Input, Output, State
from pandas import read_json

from dependencies.classes.my_dash_table import MyDashTable
from utils.utils_functions import create_msg

id_page = "view_data"

style_table = {
    "margin-left": "1%",
    "margin-top": "0%",
    "width": "98%",
    "height": "98%",
    "text-align": "left",
    "overflow": "auto",
}
style_data = {
    "padding": "-5px",
    "text-align": "left",
    "height": "0.5vmin",
    "font-size": "0.7vmax",
    "border": "transparent",
    "color": "#535353",
    "background": "#E8F6FF",
    "border-radius": "10px",
}
style_cell = {
    "min-width": "2%",
    "max-width": "2%",
    "padding": "-5px",
}
style_header = {
    "color": "white",
    "font-size": "0.8vmax",
    "font-weight": "bold",
    "text-align": "left",
    "border": "transparent",
    "background": "#08397E",
}

style_data_conditional = [
    {
        "if": {"row_index": "odd"},
        "color": "white",
        "backgroundColor": "#9EC7FC",
        "border": "transparent",
        "borderRadius": "35px",
    }
]


@callback(
    [
        Output(f"{id_page}_content_down", "children"),
        Output("loading", "children", allow_duplicate=True),
    ],
    Input("view_data", "n_clicks"),
    State("main_page_store", "data"),
    prevent_initial_call=True,
)
def auth_display(n_clicks, data):
    obj = []
    if "df" in data:
        df = read_json(data["df"])
        obj = html.Div(
            # create_adgrid(f"{id_page}_ag-table", df),
            MyDashTable.my_dash_table(
                df,
                style_table,
                style_data,
                style_header,
                style_cell,
                style_data_conditional,
            ),
        )
    else:
        obj = [create_msg("No hay ningún DataFrame Cargado")]
    return [obj, ""]
