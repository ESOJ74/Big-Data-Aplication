import plotly.express as px
from dash import Input, Output, State, callback, dcc, html
from pandas import read_json
from assets.templates_plotly import list_of_squential, template_visualizations
from assets.templates_plotly import template_visualizations
from utils.common_div_utils import selector_options
from utils.create_callback_content_up import create_callback_content_up_plotly
from utils.create_callback_hidden_button_cover import (
    create_callback_hidden_button_cover,
)
from utils.create_callback_style_content_left import create_callback_style_content_left
from utils.save_panel import save_panel

from ...common_css import *

id_page = "funnel"

create_callback_hidden_button_cover(f"{id_page}_content_down")
create_callback_style_content_left(id_page)
create_callback_content_up_plotly(id_page, "funnel-charts")
selector_options(id_page, f"{id_page}_X", False)
selector_options(id_page, f"{id_page}_Y", False)
selector_options(id_page, f"{id_page}_color")


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
        Input(f"{id_page}_color", "value"),
        Input(f"{id_page}_template", "value"),
    ],
    [
        State("main_page_store", "data"),
        State(f"{id_page}_X", "value"),
        State(f"{id_page}_Y", "value"),
        State(f"{id_page}_color", "value"),
        State(f"{id_page}_template", "value"),
        State(f"{id_page}_refresh", "children"),
    ],
    prevent_initial_call=True,
)
def display_page(
    n_clicks, click, click1, click2, click3, data, state_X, state_Y, state_color, state_template, name_button
):
    if state_color is not None and len(state_color) < 1 or state_color == " ":
        state_color = None
    new_name_button = "Apply"
    content = ""
    try:
        df = read_json(data["df"])

        fig = px.funnel(
            df,
            template=template_visualizations,
            x=state_X,
            y=state_Y,
            color=state_color,
            color_discrete_sequence=list_of_squential[state_template],
        )
        if n_clicks:
            if name_button == "Apply":
                new_name_button = "Save Panel"
                content = dcc.Graph(figure=fig, style=style_graph)
            else:
                save_panel(fig, "funnel")
                content = [
                    dcc.Graph(figure=fig, style=style_graph),
                    html.H6("Panel Guardado", style=style_msg),
                ]
    except Exception:
        content = html.H6("X e Y deben tener valor", style=style_msg)
    return [content, "", new_name_button, 0]
