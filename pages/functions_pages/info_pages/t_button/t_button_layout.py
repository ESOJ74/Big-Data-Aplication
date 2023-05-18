import os

from dash import Input, Output, State, callback, html
from pandas import read_csv, read_json

from assets.layout_templates.main_page.common_css import (
    style_content_left,
    style_content_left2,
)
from assets.layout_templates.main_page.content_layout import create_content_layout
from assets.my_dash.my_dash_table.my_dash_table import my_dash_table
from assets.my_dash.my_html.my_div import my_div
from pages.functions_pages.info_pages.common_css import *
from utils.create_callback_hidden_button_cover import (
    create_callback_hidden_button_cover,
)

id_page = "t"

layout = create_content_layout(
    id_page,
    my_div(style_div_content_up, f"{id_page}_content_up"),
    my_div(style_div_content_down, f"{id_page}_content_down"),
    my_div(style_div_params, ""),
)

create_callback_hidden_button_cover(f"{id_page}_content_down")


@callback(
    Output(f"{id_page}_content_left", "style"),
    Input("main_page_button_cover", "n_clicks"),
    prevent_initial_call=True,
)
def auth_display(n_clicks):
    if n_clicks % 2 != 0:
        return style_content_left2
    return style_content_left


@callback(
    Output(f"{id_page}_content_up", "children"),
    Input("t_button", "n_clicks"),
    prevent_initial_call=True,
)
def second_callback(n_clicks):
    return my_div(
        style_div_title,
        "",
        [
            html.H5("DataFrame.T()", style=style_title),
            html.A(
                "Documentacion",
                href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.T.html",
                target="_blank",
            ),
        ],
    )


@callback(
    [
        Output(f"{id_page}_content_down", "children"),
        Output(f"{id_page}_loading", "children", allow_duplicate=True),
    ],
    Input("t_button", "n_clicks"),
    State("main_page_store", "data"),
    prevent_initial_call=True,
)
def add_data_to_fig(n_clicks, data):
    obj = []
    try:
        df = read_json(data["df"]).head(15).T.reset_index()
        df.rename(columns={"index": "columns"}, inplace=True)
        df.to_csv("tmp.csv", index=False)
        df = read_csv("tmp.csv")
        os.remove("tmp.csv")
        obj.append(my_dash_table(df))
        obj.append(False)
    except (TypeError, KeyError, ValueError):
        obj = [
            html.H6(
                "No hay ningún DataFrame Cargado",
                style={"margin-left": "20%", "color": "#b0d8d3"},
            ),
            True,
        ]
    return [my_div(style_graph, "", obj), ""]
