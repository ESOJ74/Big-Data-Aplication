import plotly.express as px
from dash import Input, Output, State, callback, dcc, html
from pandas import read_json

from assets.my_dash.my_html.my_div import my_div
from assets.templates_plotly import template_visualizations
from utils.common_div_utils import selector_options
from utils.create_callback_button_cover import create_callback_button_cover

from ...common_css import *

id_page = "funnel"


create_callback_button_cover(id_page, f"{id_page}_content_down")
selector_options(id_page, f"{id_page}_X", False)
selector_options(id_page, f"{id_page}_Y", False)
selector_options(id_page, f"{id_page}_color")


@callback(
    Output(f"{id_page}_content_up", "children"),
    Input("funnel_button", "n_clicks"),
    prevent_initial_call=True,
)
def second_callback(n_clicks):
    return my_div(
        style_div_title,
        "",
        [
            html.H5("plotly.express.funnel()", style=style_title),
            html.A(
                "Documentacion",
                href="https://plotly.com/python/funnel-charts/",
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
        State(f"{id_page}_color", "value"),
    ],
    prevent_initial_call=True,
)
def display_page(
    n_clicks,
    data,
    state_X,
    state_Y,
    state_color,
):
    if state_color is not None and len(state_color) < 1 or state_color == " ":
        state_color = None

    if state_X and state_Y:
        df = read_json(data["df"])

        fig = px.funnel(
            df,
            template=template_visualizations,
            x=state_X,
            y=state_Y,
            color=state_color,
            color_discrete_sequence=sequential.Plasma,
        ).update_layout(legend={"title_font_color": color_boton_1})
        return [dcc.Graph(figure=fig, style=style_graph), ""]
    else:
        return [html.H6("X e Y deben tener valor", style=style_msg), ""]
