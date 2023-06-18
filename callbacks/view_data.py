from dash import callback, html
from dash.dependencies import Input, Output, State
from pandas import read_json

from dependencies.classes.my_dash_table import MyDashTable
from utils.utils_functions import create_msg

id_page = "view_data"

style_table = {
    "margin-left": "1%",
    "margin-top": "6%",
    "width": "98%",
    "height": "98%",
    "text-align": "left",
    "overflow-y": "auto"
}

style_data = {
    "padding": "-5px",
    "text-align": "left",
    "height": "0.5vmin",
    "font-family": "var(--bs-body-font-family)",
    "font-size": "0.8vmax",
    "border-right": "1.5px solid #F4F5F5",
    "border": "1.5px solid #F4F5F5",
    "color": "#535353",
    "background": "#F4F5F5",
    "border-radius": "10px",
}

style_cell = {
    "min-width": "2%",
    "max-widht": "2%",
    "padding": "-5px",
}

style_header = {
    "color": "#535353",
    "font-family": "var(--bs-body-font-family)",
    "font-size": "1.1vmax",
    "font-weight": "bold",
    "text-align": "left",
    "border-left": "1.5px solid #D2D2D2",
    "border-right": "1.5px solid #D2D2D2",
    "background": "#D2D2D2",
}

style_data_conditional = [
    {
        "if": {"row_index": "odd"},
        "backgroundColor": "#D2D2D2",
        "border": "1.5px solid #D2D2D2",
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
