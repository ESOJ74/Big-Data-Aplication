import plotly.express as px
from dash import Input, Output, State, callback, dcc, html
from pandas import read_json

from assets.layout_templates.main_page.common_css import (
    style_content_left,
    style_content_left2,
)
from assets.my_dash.my_html.my_div import my_div
from assets.templates_plotly import template_visualizations
from utils.common_div_utils import selector_options
from utils.create_callback_hidden_button_cover import (
    create_callback_hidden_button_cover,
)

from ...common_css import *

id_page = "strip"


create_callback_hidden_button_cover(f"{id_page}_content_down")
selector_options(id_page, f"{id_page}_X", False)
selector_options(id_page, f"{id_page}_Y", False)
selector_options(id_page, f"{id_page}_color")
selector_options(id_page, f"{id_page}_hover_data")
selector_options(id_page, f"{id_page}_facet_col")


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
    Input("strip_button", "n_clicks"),
    prevent_initial_call=True,
)
def second_callback(n_clicks):
    return my_div(
        style_div_title,
        "",
        [
            html.H5("plotly.express.strip()", style=style_title),
            html.A(
                "Documentacion",
                href="https://plotly.com/python/strip-charts/",
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
        State(f"{id_page}_X", "value"),
        State(f"{id_page}_Y", "value"),
        State(f"{id_page}_stripmode", "value"),
        State(f"{id_page}_color", "value"),
        State(f"{id_page}_hover_data", "value"),
        State(f"{id_page}_facet_col", "value"),
    ],
    prevent_initial_call=True,
)
def display_page(
    n_clicks,
    data,
    state_X,
    state_Y,
    state_stripmode,
    state_color,
    state_hover_data,
    state_facet_col,
):
    if state_color is not None and len(state_color) < 1 or state_color == " ":
        state_color = None
    if (
        state_hover_data is not None
        and len(state_hover_data) < 1
        or state_hover_data == " "
    ):
        state_hover_data = None
    if (
        state_facet_col is not None
        and len(state_facet_col) < 1
        or state_facet_col == " "
    ):
        state_facet_col = None

    if state_X and state_Y:
        df = read_json(data["df"])

        fig = px.strip(
            df,
            template=template_visualizations,
            x=state_X,
            y=state_Y,
            hover_data=state_hover_data,
            stripmode=state_stripmode,
            color=state_color,
            facet_col=state_facet_col,
            color_discrete_sequence=sequential.Plasma,
        )
        return [dcc.Graph(figure=fig, style=style_graph), ""]
    else:
        return [html.H6("X e Y deben tener valor", style=style_msg), ""]
