from dash import Input, Output, State, callback, html
from pandas import read_json

from utils.buttons import button_apply, button_save
from utils.in_out import save_function
from utils.select_labels import select_labels

id_page = "drop"


def apply_function(data, state_labels_value, state_axis):
    df = read_json(data["df"])
    df.drop(state_labels_value, axis=state_axis, inplace=True)
    data["prov_df"] = df.to_json(orient="columns")
    return df


@callback(
    [
        Output(f"{id_page}_content_down", "children"),
        Output("main_page_store", "data", allow_duplicate=True),
        Output("loading", "children", allow_duplicate=True),
        Output(f"{id_page}_refresh", "children"),
        Output(f"{id_page}_refresh", "n_clicks"),
        Output(f"{id_page}_labels", "options", allow_duplicate=True),
    ],
    [
        Input(f"{id_page}_refresh", "n_clicks"),
        Input(f"{id_page}_labels", "value"),
        Input(f"{id_page}_axis", "value"),
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
    clicks_button, click, click2, data, state_labels_value, state_axis, name_button
):
    if clicks_button:
        msg = f"df.drop(labels={state_labels_value}, axis={state_axis})"
        if name_button == "Apply":
            if type(state_labels_value) == str:
                state_labels_value = []

            df = apply_function(data, state_labels_value, state_axis)
            msg = html.H6(msg,
                          style={"color": "white", "font-size": "1vmax", "margin-left": "2%"})
            name_button, content = button_apply(df, msg)
            labels = select_labels(df, state_axis)
        else:
            df = save_function(data)
            file_pathname = f"""users/{data["user"]}/workflow.txt"""
            name_button, content = button_save(file_pathname, msg)
            labels = select_labels(df, state_axis)
            content = html.Div(content)
    else:
        df = read_json(data["df"])
        labels = select_labels(df, state_axis)
        content = ""
        name_button = "Apply"
    content = html.Div(content)
    return [content, data, "", name_button, 0, labels]
