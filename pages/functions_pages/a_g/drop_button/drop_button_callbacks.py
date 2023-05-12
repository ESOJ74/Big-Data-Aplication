from dash import Input, Output, State, callback, html
from pandas import read_json

from utils.button_apply import button_apply, button_save1
from utils.create_callback_content_up import create_callback_content_up
from utils.create_callback_hidden_button_cover import (
    create_callback_hidden_button_cover,
)
from utils.create_callback_style_content_left import create_callback_style_content_left
from utils.select_labels import select_labels

from ...common_css import *

id_page = "drop"


create_callback_hidden_button_cover(f"{id_page}_content_up")
create_callback_content_up(id_page)
create_callback_style_content_left(id_page)


@callback(
    Output(f"{id_page}_refresh", "children", allow_duplicate=True),
    Input(f"{id_page}_labels", "value"),
    prevent_initial_call=True,
)
def add_data_to_fig(labels_value):
    return "Apply"


@callback(
    [
        Output(f"{id_page}_div_graph", "children"),
        Output("main_page_store", "data", allow_duplicate=True),
        Output(f"{id_page}_loading", "children"),
        Output(f"{id_page}_refresh", "children"),
        Output(f"{id_page}_refresh", "n_clicks"),
        Output(f"{id_page}_labels", "options", allow_duplicate=True),
    ],
    [
        Input(f"{id_page}_refresh", "n_clicks"),
        Input(f"{id_page}_labels", "value"),
    ],
    [
        State("main_page_store", "data"),
        State(f"{id_page}_labels", "value"),
        State(f"{id_page}_axis", "value"),
        State(f"{id_page}_refresh", "children"),
    ],
    prevent_initial_call=True,
)
def add_data_to_fig(
    clicks_button, click, data, state_labels_value, state_axis, name_button
):
    if clicks_button:
        if name_button == "Apply":
            if type(state_labels_value) == str:
                state_labels_value = []

            df = read_json(data["df"])
            df.drop(state_labels_value, axis=state_axis, inplace=True)
            data["prov_df"] = df.to_json(orient="columns")
            msg = html.H6(
                f"df.drop(labels={state_labels_value}, axis={state_axis})",
                style=style_div_code,
            )
            name_button, content = button_apply(id_page, df, msg)
            labels = select_labels(df, state_axis)
        else:
            df = read_json(data["prov_df"])
            data["df"] = df.to_json(orient="columns")
            file_path = f"""users/{data["user"]}/workflow.txt"""
            action = f"""df = df.drop({state_labels_value}, axis={state_axis})"""
            name_button, content = button_save1(file_path, action)
            labels = select_labels(df, state_axis)
    else:
        df = read_json(data["df"])
        labels = select_labels(df, state_axis)
        content = ""
        name_button = "Apply"
    return [content, data, "", name_button, 0, labels]
