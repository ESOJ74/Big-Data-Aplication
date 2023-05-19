import plotly.express as px
from dash import Input, Output, State, callback, dcc, html
from pandas import read_json

from assets.templates_plotly import template_visualizations
from utils.common_div_utils import selector_options
from utils.create_callback_content_up import create_callback_content_up_plotly
from utils.create_callback_hidden_button_cover import (
    create_callback_hidden_button_cover,
)
from utils.create_callback_style_content_left import create_callback_style_content_left
from utils.save_panel import save_panel

from ...common_css import *

id_page = "violin"


create_callback_hidden_button_cover(f"{id_page}_content_down")
create_callback_style_content_left(id_page)
create_callback_content_up_plotly(id_page, "violin")
selector_options(id_page, f"{id_page}_X")
selector_options(id_page, f"{id_page}_Y", False)
selector_options(id_page, f"{id_page}_color")
selector_options(id_page, f"{id_page}_hover_data")


@callback(
    [
        Output(f"{id_page}_content_down", "children"),
        Output(f"{id_page}_loading", "children", allow_duplicate=True),
        Output(f"{id_page}_refresh", "children"),
        Output(f"{id_page}_refresh", "n_clicks"),
    ],
    [
        Input(f"{id_page}_refresh", "n_clicks"),
        Input(f"{id_page}_X", "value"),
        Input(f"{id_page}_Y", "value"),
        Input(f"{id_page}_box", "value"),
        Input(f"{id_page}_points", "value"),
        Input(f"{id_page}_violinmode", "value"),
        Input(f"{id_page}_color", "value"),
        Input(f"{id_page}_hover_data", "value"),
    ],
    [
        State("main_page_store", "data"),
        State(f"{id_page}_X", "value"),
        State(f"{id_page}_Y", "value"),
        State(f"{id_page}_box", "value"),
        State(f"{id_page}_points", "value"),
        State(f"{id_page}_violinmode", "value"),
        State(f"{id_page}_color", "value"),
        State(f"{id_page}_hover_data", "value"),
        State(f"{id_page}_refresh", "children"),
    ],
    prevent_initial_call=True,
)
def display_page(
    n_clicks,
    click,
    click1,
    click2,
    click3,
    click4,
    click5,
    click6,
    data,
    state_X,
    state_Y,
    state_box,
    state_points,
    state_violinmode,
    state_color,
    state_hover_data,
    name_button,
):
    if state_color is not None and len(state_color) < 1 or state_color == " ":
        state_color = None
    if (
        state_hover_data is not None
        and len(state_hover_data) < 1
        or state_hover_data == " "
    ):
        state_hover_data = None
    if state_X is not None and len(state_X) < 1 or state_X == " ":
        state_X = None
    if state_points == "False":
        state_points = False
    state_box = False if state_box == "False" else True
    new_name_button = "Apply"
    content = ""
    try:
        df = read_json(data["df"])

        fig = px.violin(
            df,
            x=state_X,
            y=state_Y,
            box=state_box,
            points=state_points,
            violinmode=state_violinmode,
            color=state_color,
            hover_data=state_hover_data,
            template=template_visualizations,
            color_discrete_sequence=sequential.Plasma,
        )
        if n_clicks:
            if name_button == "Apply":
                new_name_button = "Save Panel"
                content = dcc.Graph(figure=fig, style=style_graph)
            else:
                save_panel(fig, "violin")
                content = [
                    dcc.Graph(figure=fig, style=style_graph),
                    html.H6("Panel Guardado", style=style_msg),
                ]
    except Exception:
        content = html.H6("X e Y deben tener valor", style=style_msg)
    return [content, "", new_name_button, 0]
