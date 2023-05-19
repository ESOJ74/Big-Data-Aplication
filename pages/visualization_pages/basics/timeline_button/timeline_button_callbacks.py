import plotly.figure_factory as ff
from dash import Input, Output, State, callback, dcc, html
from pandas import read_json

from utils.common_div_utils import selector_options
from utils.create_callback_content_up import create_callback_content_up_plotly
from utils.create_callback_hidden_button_cover import (
    create_callback_hidden_button_cover,
)
from utils.create_callback_style_content_left import create_callback_style_content_left
from utils.save_panel import save_panel

from ...common_css import *

id_page = "timeline"

create_callback_hidden_button_cover(f"{id_page}_content_down")
create_callback_style_content_left(id_page)
create_callback_content_up_plotly(id_page, "gantt")
selector_options(id_page, f"{id_page}_index_col")


@callback(
    [
        Output(f"{id_page}_content_down", "children"),
        Output(f"{id_page}_loading", "children", allow_duplicate=True),
        Output(f"{id_page}_refresh", "children"),
        Output(f"{id_page}_refresh", "n_clicks"),
    ],
    [
        Input(f"{id_page}_refresh", "n_clicks"),
        Input(f"{id_page}_index_col", "value"),
        Input(f"{id_page}_show_colorbar", "value"),
        Input(f"{id_page}_group_tasks", "value"),
    ],
    [
        State("main_page_store", "data"),
        State(f"{id_page}_index_col", "value"),
        State(f"{id_page}_show_colorbar", "value"),
        State(f"{id_page}_group_tasks", "value"),
        State(f"{id_page}_refresh", "children"),
    ],
    prevent_initial_call=True,
)
def display_page(
    n_clicks,
    click,
    click1,
    click2,
    data,
    state_index_col,
    state_show_colorbar,
    state_group_task,
    name_button,
):
    if state_show_colorbar == "True":
        state_show_colorbar = True
    else:
        state_show_colorbar = False

    if state_group_task == "True":
        state_group_task = True
    else:
        state_group_task = False
    new_name_button = "Apply"
    content = ""
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
        if n_clicks:
            if name_button == "Apply":
                new_name_button = "Save Panel"
                content = dcc.Graph(figure=fig, style=style_graph)
            else:
                save_panel(fig, "timeline")
                content = [
                    dcc.Graph(figure=fig, style=style_graph),
                    html.H6("Panel Guardado", style=style_msg),
                ]
    except Exception as err:
        content = html.H6(str(err).__str__(), style=style_msg)
    return [content, "", new_name_button, 0]
