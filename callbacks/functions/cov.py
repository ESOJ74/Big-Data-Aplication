import plotly.express as px
from dash import Input, Output, State, callback
from pandas import read_json

from assets.template import list_of_squential
from utils.create_callback_text_graph import create_callback_text_graph
from utils.utils_functions import create_msg, create_obj

id_page = "cov"

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
        State(f"{id_page}_ddof", "value"),
        State(f"{id_page}_numeric_only", "value"),
        State(f"{id_page}_min_periods", "value"),
        State(f"{id_page}_template", "value"),
    ],
    prevent_initial_call=True,
)
def second_callback(
    click1,
    click2,
    click3,
    data,
    state_text,
    state_graph,
    state_ddof,
    state_numeric_only,
    state_min_periods,
    state_template,
):
    try:
        state_min_periods = int(state_min_periods)

        if state_numeric_only == "True":
            state_numeric_only = True
        else:
            state_numeric_only = False

        cov = read_json(data["df"]).cov(
            state_min_periods, state_ddof, state_numeric_only
        )
        fig = px.imshow(
                cov,
                #template=template_visualizations,
                color_continuous_scale=list_of_squential[state_template],
                contrast_rescaling="infer",
                aspect="auto",
            )      
        return [create_obj(cov.__str__(), fig, state_graph), ""]
    except ValueError as msg:
        return [create_msg(msg), ""]
