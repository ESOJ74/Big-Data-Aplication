import plotly.express as px
from dash import Input, Output, State, callback
from numpy import float64
from pandas import read_json

from assets.template import list_of_squential
from utils.create_callback_text_graph import create_callback_text_graph
from utils.utils_functions import create_msg, create_obj

id_page = "var"

create_callback_text_graph(id_page)


@callback(
    [
        Output(f"{id_page}_content_down", "children"),
        Output("loading", "children", allow_duplicate=True),
    ],
    [
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
        State(f"{id_page}_ddof", "value"),
        State(f"{id_page}_numeric_only", "value"),
        State(f"{id_page}_template", "value"),
    ],
    prevent_initial_call=True,
)
def add_data_to_fig(
    n_clicks_text,
    n_click_graph,
    refresh,
    data,
    state_text,
    state_graph,
    state_axis,
    state_skipna,
    state_ddof,
    state_numeric_only,
    state_template,
):
    try:
        obj = ""
        state_ddof = int(state_ddof)

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

        var = read_json(data["df"]).var(
            state_axis, state_skipna, state_ddof, state_numeric_only
        )
        var_info = var
        if state_axis not in (1, 0):
            return [create_msg(f"axis no ha sido seleccionado"), ""]
        if type(var_info) != float64:
            var_info = var_info.to_string()

        fig = px.bar(
            x=var.index,
            y=var.values,
            labels={"x": "Columns", "y": "unbiased standard error of the mean"},
            # template=template_visualizations,
            color_continuous_scale=list_of_squential[state_template],
            color_discrete_sequence=list_of_squential[state_template],
        )
        return [create_obj(var_info, fig, state_graph, state_axis), ""]
    except (ValueError, TypeError) as msg:
        return [create_msg(msg), ""]
