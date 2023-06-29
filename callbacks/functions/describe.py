import numpy as np
from dash import Input, Output, State, callback
from pandas import read_json, set_option
from utils.utils_functions import create_msg, create_obj

id_page = "describe"


@callback(
    [
        Output(f"{id_page}_content_down", "children"),
        Output("loading", "children", allow_duplicate=True),
    ],
    [Input(f"{id_page}_refresh", "n_clicks")],
    [
        State("main_page_store", "data"),
        State(f"{id_page}_percentiles", "value"),
        State(f"{id_page}_include", "value"),
        State(f"{id_page}_exclude", "value"),
    ],
    prevent_initial_call=True,
)
def add_data_to_fig(n_clicks, data, percentiles, include, exclude):
    set_option("display.max_columns", 500)
    set_option("display.width", 1000)
    if percentiles in ("", None):
        percentiles = None
    else:
        percentiles = [float(x) for x in percentiles.split(" ")]

    if include in ("", None):
        include = None
    match include:
        case "all":
            include = "all"
        case "object":
            include = [object]
        case "number":
            include = [np.number]
        case "category":
            include = ["category"]
        case _:
            include = None
    match exclude:
        case "object":
            exclude = [object]
        case "number":
            exclude = [np.number]
        case "category":
            exclude = ["category"]
        case _:
            exclude = None
    try:
        describe_df = (
            read_json(data["df"]).describe(percentiles, include, exclude).transpose()
        )
        return [create_obj(describe_df, "", ""), ""]
    except Exception as msg:
        return [create_msg(msg), ""]
