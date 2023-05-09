import plotly.express as px
from dash import Input, Output, State, callback, dcc, html
from pandas import read_json

from assets.my_dash.my_html.my_div import my_div
from assets.templates_plotly import template_visualizations_2
from utils.common_div_utils import selector_options
from utils.create_callback_button_cover import create_callback_button_cover

from ...common_css import *

id_page = "scatter_3d"


create_callback_button_cover(id_page, f"{id_page}_content_down")
selector_options(id_page, f"{id_page}_X", False)
selector_options(id_page, f"{id_page}_Y", False)
selector_options(id_page, f"{id_page}_Z", False)
selector_options(id_page, f"{id_page}_color")
selector_options(id_page, f"{id_page}_symbol")
selector_options(id_page, f"{id_page}_size")


@callback(
    Output(f"{id_page}_content_up", "children"),
    Input("scatter_3d_button", "n_clicks"),
    prevent_initial_call=True,
)
def second_callback(n_clicks):
    return my_div(
        style_div_title,
        "",
        [
            html.H5("plotly.express.scatter_3d()", style=style_title),
            html.A(
                "Documentacion",
                href="https://plotly.com/python/3d-scatter-plots/",
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
        State(f"{id_page}_Z", "value"),
        State(f"{id_page}_color", "value"),
        State(f"{id_page}_symbol", "value"),
        State(f"{id_page}_size", "value"),
        State(f"{id_page}_opacity", "value"),
    ],
    prevent_initial_call=True,
)
def display_page(
    n_clicks,
    data,
    state_X,
    state_Y,
    state_Z,
    state_color,
    state_symbol,
    state_size,
    state_opacity,
):
    try:
        if state_color is not None and len(state_color) < 1 or state_color == " ":
            state_color = None

        if state_symbol is not None and len(state_symbol) < 1 or state_symbol == " ":
            state_symbol = None

        if state_size is not None and len(state_size) < 1 or state_size == " ":
            state_size = None

        state_opacity = float(state_opacity)

        df = read_json(data["df"])

        fig = (
            px.scatter_3d(
                df,
                template=template_visualizations_2,
                x=state_X,
                y=state_Y,
                z=state_Z,
                height=550,
                color=state_color,
                symbol=state_symbol,
                size=state_size,
                opacity=state_opacity,
                size_max=18,
                color_discrete_sequence=sequential.Plasma,
            )
            .update_layout(
                legend={"title_font_color": color_boton_1},
                margin=dict(l=0, r=0, t=0, b=30),
                width=None,
                scene=dict(
                    xaxis=dict(gridcolor=color_axis_scatter_3d),
                    yaxis=dict(gridcolor=color_axis_scatter_3d),
                    zaxis=dict(gridcolor=color_axis_scatter_3d),
                ),
            )
            .update_traces(
                marker=dict(line=dict(width=0.05, color="Black")),
                selector=dict(mode="markers"),
            )
        )
        return [dcc.Graph(figure=fig), ""]
    except ValueError as msg:
        return [html.H6(msg.__str__(), style=style_msg), ""]
