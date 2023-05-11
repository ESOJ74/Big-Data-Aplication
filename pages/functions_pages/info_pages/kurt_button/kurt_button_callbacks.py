import plotly.express as px
from dash import Input, Output, State, callback, dcc, html
from numpy import float64
from pandas import read_json

from assets.layout_templates.main_page.common_css import (
    style_content_left,
    style_content_left2,
)
from assets.my_dash.my_html.my_div import my_div
from assets.templates_plotly import template_visualizations
from utils.create_callback_hidden_button_cover import (
    create_callback_hidden_button_cover,
)
from utils.create_callbacks_text_graph import create_callback_text_graph

from ..common_css import *

id_page = "kurt"


create_callback_hidden_button_cover(f"{id_page}_content_down")
create_callback_text_graph(id_page)


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
    Input("kurt_button", "n_clicks"),
    prevent_initial_call=True,
)
def second_callback(n_clicks):
    return my_div(
        style_div_title,
        "",
        [
            html.H5("DataFrame.kurt()", style=style_title),
            html.A(
                "Documentacion",
                href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.kurt.html",
                target="_blank",
            ),
        ],
    )


@callback(
    [
        Output(f"{id_page}_content_down", "children"),
        Output(f"{id_page}_loading", "children", allow_duplicate=True),
    ],
    [
        Input("kurt_button", "n_clicks"),
        Input(f"{id_page}_text", "className"),
        Input(f"{id_page}_graph", "className"),
        Input(f"{id_page}_refresh", "n_clicks"),
    ],
    [
        State("main_page_store", "data"),
        State(f"{id_page}_text", "className"),
        State(f"{id_page}_graph", "className"),
        State(f"{id_page}_axis", "value"),
        State(f"{id_page}_skipna", "value"),
        State(f"{id_page}_numeric_only", "value"),
    ],
    prevent_initial_call=True,
)
def second_callback(
    n_clicks,
    n_clicks_text,
    n_click_graph,
    refresh,
    data,
    state_text,
    state_graph,
    state_axis,
    state_skipna,
    state_numeric_only,
):
    try:
        obj = ""

        if type(state_axis) != int:
            state_axis = None

        if state_skipna == "True":
            state_skipna = True
        else:
            state_skipna = False

        if state_numeric_only == "True":
            state_numeric_only = True
        else:
            state_numeric_only = False

        kurt = read_json(data["df"]).kurt(state_axis, state_skipna, state_numeric_only)

        kurt_info = kurt
        if type(kurt_info) != float64:
            kurt_info = kurt_info.to_string()

        # if state_text == "btn btn-warning":

        if state_axis not in (1, 0):
            kurt_info = f"Agregación en ambos ejes: {kurt_info}"
        obj = html.Pre(kurt_info, style=style_text)

        if state_graph == "btn btn-warning":
            if state_axis == 0:
                fig = px.bar(
                    x=kurt.index,
                    y=kurt.values,
                    labels={"x": "Columns", "y": "unbiased kurtosis"},
                    template=template_visualizations,
                )
                obj = dcc.Graph(
                    figure=fig,
                    style=style_graph,
                )
            else:
                obj = html.Pre("Gráfico disponible solo para axis=0", style=style_text)

        return [my_div(style_div_obj, "", obj), ""]
    except (ValueError, TypeError) as msg:
        return [html.H6(msg.__str__(), style=style_msg), ""]
