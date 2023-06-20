import os

from dash import Input, Output, State, callback
from pandas import read_csv, read_json

from dependencies.classes.my_dash_table import MyDashTable
from utils.utils_functions import create_msg

id_page = "t"

style_table = {
    "margin-left": "1%",
    "margin-top": "2%",
    "width": "98%",
    "max-height": "550px",
    "text-align": "left",
    "overflow": "auto"
}
style_data = {
    "padding": "-5px",
    "text-align": "left",
    "height": "0.5vmin",
    "font-family": "var(--bs-body-font-family)",
    "font-size": "0.7vmax",
    "border-right": "1.5px solid #F4F5F5",
    "border": "1.5px solid #F4F5F5",
    "color": "#535353",
    "background": "#F4F5F5",
    "border-radius": "10px",
}
style_cell = {
    "min-width": "2%",
    "max-width": "2%",
    "padding": "-5px",
}
style_header = {
    "color": "white",
    "font-family": "var(--bs-body-font-family)",
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
    },
    {
        "if": {"column_id": "columns"},
        "font-size": "0.8vmax",
        "font-weight": "bold",
    },
]


@callback(
    Output(f"{id_page}_content_down", "children"),
    Input("t", "n_clicks"),
    State("main_page_store", "data"),
    prevent_initial_call=True,
)
def add_data_to_fig(n_clicks, data):
    try:
        df = read_json(data["df"]).head(6).T.reset_index()
        df.rename(columns={"index": "columns"}, inplace=True)
        df.to_csv("tmp.csv", index=False)
        df = read_csv("tmp.csv")
        os.remove("tmp.csv")
        obj = MyDashTable.my_dash_table(
            df,
            style_table,
            style_data,
            style_header,
            style_cell,
            style_data_conditional,
        )
        return [obj, ""]
    except (TypeError, KeyError, ValueError) as msg:
        return [create_msg(msg), ""]
