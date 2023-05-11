import plotly.figure_factory as ff
from dash import Input, Output, State, callback, dcc, html
from pandas import read_json
from assets.layout_templates.main_page.common_css import (
    style_content_left,
    style_content_left2,
)
from assets.my_dash.my_html.my_div import my_div
from utils.common_div_utils import selector_options
from utils.create_callback_hidden_button_cover import (
    create_callback_hidden_button_cover,
)

from ...common_css import *

id_page = "timeline"


create_callback_hidden_button_cover(f"{id_page}_content_down")
selector_options(id_page, f"{id_page}_index_col")


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
    Input("timeline_button", "n_clicks"),
    prevent_initial_call=True,
)
def second_callback(n_clicks):
    return my_div(
        style_div_title,
        "",
        [
            html.H5("plotly.scatter.timeline()", style=style_title),
            html.A(
                "Documentacion",
                href="https://plotly.com/python/gantt/",
                target="_blank",
            ),
        ],
    )


@callback(
    [
        Output(f"{id_page}_content_down", "children"),
        Output(f"{id_page}_loading", "children", allow_duplicate=True),
    ],
    Input(f"{id_page}_refresh", "n_clicks"),
    [
        State("main_page_store", "data"),
        State(f"{id_page}_index_col", "value"),
        State(f"{id_page}_show_colorbar", "value"),
        State(f"{id_page}_group_tasks", "value"),
    ],
    prevent_initial_call=True,
)
def display_page(
    n_clicks, data, state_index_col, state_show_colorbar, state_group_task
):
    if state_show_colorbar == "True":
        state_show_colorbar = True
    else:
        state_show_colorbar = False

    if state_group_task == "True":
        state_group_task = True
    else:
        state_group_task = False

    if state_index_col:
        try:
            df = read_json(data["df"])

            colors = {}
            for x, y in zip(df[state_index_col], sequential.Plasma):
                colors[x] = y

            fig = ff.create_gantt(
                df,
                colors=colors,
                index_col=state_index_col,
                show_colorbar=state_show_colorbar,
                group_tasks=state_group_task,
            )
            return [dcc.Graph(figure=fig, style=style_graph), ""]
        except Exception as msg:
            return [html.H6(msg.__str__(), style=style_msg), ""]
    else:
        return [html.H6("X e Y deben tener valor", style=style_msg), ""]
