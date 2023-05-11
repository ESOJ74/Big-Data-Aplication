import plotly.express as px
from dash import Input, Output, State, callback, dcc, html

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

id_page = "icicle"


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
    Input("icicle_button", "n_clicks"),
    prevent_initial_call=True,
)
def second_callback(n_clicks):
    return my_div(
        style_div_title,
        "",
        [
            html.H5("plotly.express.icicle()", style=style_title),
            html.A(
                "Documentacion",
                href="https://plotly.com/python/icicle-charts/",
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
    ],
    prevent_initial_call=True,
)
def display_page(n_clicks, data):
    data = dict(
        character=[
            "Eve",
            "Cain",
            "Seth",
            "Enos",
            "Noam",
            "Abel",
            "Awan",
            "Enoch",
            "Azura",
        ],
        parent=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"],
        value=[10, 14, 12, 10, 2, 6, 6, 4, 4],
    )

    fig = px.icicle(
        data,
        names="character",
        parents="parent",
        values="value",
    )
    fig.update_traces(root_color="lightgrey")
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
    return [dcc.Graph(figure=fig, style=style_graph), ""]
