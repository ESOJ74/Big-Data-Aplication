import plotly.express as px
from dash import Input, Output, State, callback, dcc, html
from pandas import read_json

from assets.templates_plotly import list_of_squential, template_visualizations
from utils.common_div_utils import selector_options
from utils.create_callback_content_up import create_callback_content_up_plotly
from utils.create_callback_hidden_button_cover import (
    create_callback_hidden_button_cover,
)
from utils.create_callback_style_content_left import create_callback_style_content_left
from utils.save_panel import save_panel

from ...common_css import *

id_page = "scatter_3d"


create_callback_hidden_button_cover(f"{id_page}_content_down")
create_callback_style_content_left(id_page)
create_callback_content_up_plotly(id_page, "3d-scatter-plots")
selector_options(id_page, f"{id_page}_X", False)
selector_options(id_page, f"{id_page}_Y", False)
selector_options(id_page, f"{id_page}_Z", False)
selector_options(id_page, f"{id_page}_color")
selector_options(id_page, f"{id_page}_symbol")
selector_options(id_page, f"{id_page}_size")


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
        Input(f"{id_page}_Z", "value"),
        Input(f"{id_page}_color", "value"),
        Input(f"{id_page}_symbol", "value"),
        Input(f"{id_page}_size", "value"),
        Input(f"{id_page}_opacity", "value"),
        Input(f"{id_page}_log_x", "value"),
        Input(f"{id_page}_log_y", "value"),
        Input(f"{id_page}_log_z", "value"),
        Input(f"{id_page}_template", "value"),
    ],
    [
        State("main_page_store", "data"),
        State(f"{id_page}_X", "value"),
        State(f"{id_page}_Y", "value"),
        State(f"{id_page}_Z", "value"),
        State(f"{id_page}_color", "value"),
        State(f"{id_page}_symbol", "value"),
        State(f"{id_page}_size", "value"),
        State(f"{id_page}_opacity", "value"),
        State(f"{id_page}_log_x", "value"),
        State(f"{id_page}_log_y", "value"),
        State(f"{id_page}_log_z", "value"),
        State(f"{id_page}_template", "value"),
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
    click7,
    click8,
    click9,
    click10,
    data,
    state_X,
    state_Y,
    state_Z,
    state_color,
    state_symbol,
    state_size,
    state_opacity,
    state_log_x,
    state_log_y,
    state_log_z,
    state_template,
    name_button,
):
    if state_color is not None and len(state_color) < 1 or state_color == " ":
        state_color = None

    if state_symbol is not None and len(state_symbol) < 1 or state_symbol == " ":
        state_symbol = None

    if state_size is not None and len(state_size) < 1 or state_size == " ":
        state_size = None

    state_opacity = float(state_opacity)
    state_log_x = False if state_log_x == "False" else True
    state_log_y = False if state_log_y == "False" else True
    state_log_z = False if state_log_z == "False" else True
    new_name_button = "Apply"
    content = ""
    try:
        df = read_json(data["df"])
        print(state_template)
        fig = (
            px.scatter_3d(
                df,
                x=state_X,
                y=state_Y,
                z=state_Z,
                color=state_color,
                symbol=state_symbol,
                size=state_size,
                opacity=state_opacity,
                log_x=state_log_x,
                log_y=state_log_y,
                log_z=state_log_z,
                size_max=18,
                template=template_visualizations,
                color_discrete_sequence=list_of_squential[state_template],
                color_continuous_scale=list_of_squential[state_template]
            )
            .update_layout(
                margin=dict(l=25, r=30, t=35, b=25),
                scene=dict(
                    aspectratio={"x": 0.9, "y": 0.8, "z": 1},
                ),
            )
            .update_traces(
                marker=dict(line=dict(width=0.05, color="Black")),
                selector=dict(mode="markers"),
            )
        )
        if n_clicks:
            if name_button == "Apply":
                new_name_button = "Save Panel"
                content = dcc.Graph(figure=fig, style=style_graph)
            else:
                save_panel(fig, "3d_scatter")
                content = [
                    dcc.Graph(figure=fig, style=style_graph),
                    html.H6("Panel Guardado", style=style_msg),
                ]
    except Exception as msg:
        content = html.H6("X, Y y Z deben tener valor", style=style_msg)
    return [content, "", new_name_button, 0]
