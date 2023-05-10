import plotly.express as px
from dash import Input, Output, State, callback, dcc, html
from pandas import read_json

from assets.my_dash.my_html.my_div import my_div
from assets.templates_plotly import template_visualizations
from utils.common_div_utils import selector_options
from utils.create_callback_button_cover import create_callback_button_cover

from ...common_css import *

id_page = "histogram"


create_callback_button_cover(id_page, f"{id_page}_content_down")
selector_options(id_page, f"{id_page}_X", False)
selector_options(id_page, f"{id_page}_Y")
selector_options(id_page, f"{id_page}_color")
selector_options(id_page, f"{id_page}_pattern_shape")


@callback(
    Output(f"{id_page}_content_up", "children"),
    Input("histogram_button", "n_clicks"),
    prevent_initial_call=True,
)
def second_callback(n_clicks):
    return my_div(
        style_div_title,
        "",
        [
            html.H5("plotly.express.histogram()", style=style_title),
            html.A(
                "Documentacion",
                href="https://plotly.com/python/histograms/",
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
        State(f"{id_page}_nbins", "value"),
        State(f"{id_page}_bargap", "value"),
        State(f"{id_page}_histnorm", "value"),
        State(f"{id_page}_opacity", "value"),
        State(f"{id_page}_log_y", "value"),
        State(f"{id_page}_color", "value"),
        State(f"{id_page}_histfunc", "value"),
        State(f"{id_page}_pattern_shape", "value"),
    ],
    prevent_initial_call=True,
)
def display_page(
    n_clicks,
    data,
    state_X,
    state_Y,
    state_nbins,
    state_bargap,
    state_histnorm,
    state_opacity,
    state_log_y,
    state_color,
    state_histfunc,
    state_pattern_shape,
):
    if state_Y is not None and len(state_Y) < 1 or state_Y == " ":
        state_Y = None
    if state_color is not None and len(state_color) < 1 or state_color == " ":
        state_color = None
    if state_histfunc is not None and len(state_histfunc) < 1 or state_histfunc == " ":
        state_histfunc = None
    if state_histnorm is not None and len(state_histnorm) < 1 or state_histnorm == " ":
        state_histnorm = None
    if (
        state_pattern_shape is not None
        and len(state_pattern_shape) < 1
        or state_pattern_shape == " "
    ):
        state_pattern_shape = None
    state_log_y = False if state_log_y == "False" else True

    if state_X:
        df = read_json(data["df"])
        try:
            state_bargap = float(state_bargap)
            state_opacity = float(state_opacity)

            fig = px.histogram(
                df,
                template=template_visualizations,
                x=state_X,
                y=state_Y,
                nbins=state_nbins,
                histnorm=state_histnorm,
                opacity=state_opacity,
                log_y=state_log_y,
                color=state_color,
                histfunc=state_histfunc,
                pattern_shape=state_pattern_shape,
                color_discrete_sequence=sequential.Plasma,
            ).update_layout(
                legend={"title_font_color": color_boton_1}, bargap=state_bargap
            )
            return [dcc.Graph(figure=fig, style=style_graph), ""]
        except ValueError as err:
            return [html.H6(err.__str__(), style=style_msg), ""]
    else:
        return [html.H6("X debe tener valor", style=style_msg), ""]
