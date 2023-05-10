import plotly.express as px
from dash import Input, Output, State, callback, dcc, html
from pandas import read_json

from assets.my_dash.my_html.my_div import my_div
from assets.templates_plotly import template_visualizations
from utils.common_div_utils import selector_options
from utils.create_callback_button_cover import create_callback_button_cover

from ...common_css import *

id_page = "ecdf"


create_callback_button_cover(id_page, f"{id_page}_content_down")
selector_options(id_page, f"{id_page}_X", False)
selector_options(id_page, f"{id_page}_Y")
selector_options(id_page, f"{id_page}_color")
selector_options(id_page, f"{id_page}_line_group")


@callback(
    Output(f"{id_page}_content_up", "children"),
    Input("ecdf_button", "n_clicks"),
    prevent_initial_call=True,
)
def second_callback(n_clicks):
    return my_div(
        style_div_title,
        "",
        [
            html.H5("plotly.express.ecdf()", style=style_title),
            html.A(
                "Documentacion",
                href="https://plotly.com/python/ecdf-plots/",
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
        State(f"{id_page}_ecdfnorm", "value"),
        State(f"{id_page}_ecdfmode", "value"),
        State(f"{id_page}_markers", "value"),
    ],
    prevent_initial_call=True,
)
def display_page(
    n_clicks,
    data,
    state_X,
    state_Y,
    state_color,
    state_ecdfnorm,
    state_ecdfmode,
    state_markers,
):
    if state_Y is not None and len(state_Y) < 1 or state_Y == " ":
        state_Y = None
    if state_ecdfnorm is not None and len(state_ecdfnorm) < 1 or state_ecdfnorm == " ":
        state_ecdfnorm = None
    if state_color is not None and len(state_color) < 1 or state_color == " ":
        state_color = None
    state_markers = False if state_markers == "False" else True
    if state_X:
        try:
            df = read_json(data["df"])

            fig = px.ecdf(
                df,
                template=template_visualizations,
                x=state_X,
                y=state_Y,
                color=state_color,
                ecdfnorm=state_ecdfnorm,
                ecdfmode=state_ecdfmode,
                markers=state_markers,
                color_discrete_sequence=sequential.Plasma,
            ).update_layout(legend={"title_font_color": color_boton_1})
            return [dcc.Graph(figure=fig, style=style_graph), ""]
        except Exception as err:
            return [html.H6(err.__str__(), style=style_msg), ""]
    else:
        return [html.H6("X e Y deben tener valor", style=style_msg), ""]
