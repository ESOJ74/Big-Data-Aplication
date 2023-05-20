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

id_page = "histogram"


create_callback_hidden_button_cover(f"{id_page}_content_down")
create_callback_style_content_left(id_page)
create_callback_content_up_plotly(id_page, "histograms")
selector_options(id_page, f"{id_page}_X", False)
selector_options(id_page, f"{id_page}_Y")
selector_options(id_page, f"{id_page}_color")
selector_options(id_page, f"{id_page}_pattern_shape")


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
        Input(f"{id_page}_nbins", "value"),
        Input(f"{id_page}_bargap", "value"),
        Input(f"{id_page}_histnorm", "value"),
        Input(f"{id_page}_opacity", "value"),
        Input(f"{id_page}_log_y", "value"),
        Input(f"{id_page}_color", "value"),
        Input(f"{id_page}_histfunc", "value"),
        Input(f"{id_page}_pattern_shape", "value"),
        Input(f"{id_page}_template", "value"),
    ],
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
    state_nbins,
    state_bargap,
    state_histnorm,
    state_opacity,
    state_log_y,
    state_color,
    state_histfunc,
    state_pattern_shape,
    state_template,
    name_button,
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
    new_name_button = "Apply"
    content = ""
    try:
        df = read_json(data["df"])
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
            color_discrete_sequence=list_of_squential[state_template],
        ).update_layout(bargap=state_bargap)
        if n_clicks:
            if name_button == "Apply":
                new_name_button = "Save Panel"
                content = dcc.Graph(figure=fig, style=style_graph)
            else:
                save_panel(fig, "histogram")
                content = [
                    dcc.Graph(figure=fig, style=style_graph),
                    html.H6("Panel Guardado", style=style_msg),
                ]
    except Exception:
        content = html.H6("X debe tener valor", style=style_msg)
    return [content, "", new_name_button, 0]
