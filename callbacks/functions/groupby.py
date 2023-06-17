from dash import Input, Output, State, callback, html
from pandas import read_json

from utils.buttons import button_apply, button_save
from utils.in_out import save_function
from utils.select_labels import select_labels

id_page = "groupby"


def apply_function(data, state_by, state_axis):
    df = read_json(data["df"])
    df = df.groupby(state_by, axis=state_axis).sum()
    df = df.reset_index()
    data["prov_df"] = df.to_json(orient="columns")
    return df


@callback(
    [
        Output(f"{id_page}_content_down", "children"),
        Output("main_page_store", "data", allow_duplicate=True),
        Output("loading", "children", allow_duplicate=True),
        Output(f"{id_page}_refresh", "children"),
        Output(f"{id_page}_refresh", "n_clicks"),
        Output(f"{id_page}_by", "options", allow_duplicate=True),
    ],
    [
        Input(f"{id_page}_refresh", "n_clicks"),
        Input(f"{id_page}_by", "value"),
        Input(f"{id_page}_axis", "value"),
    ],
    [
        State("main_page_store", "data"),
        State(f"{id_page}_by", "value"),
        State(f"{id_page}_axis", "value"),
        State(f"{id_page}_refresh", "children"),
    ],
    prevent_initial_call=True,
)
def add_data_to_fig(
    clicks_button, click, click2, data, state_by, state_axis, name_button
):
    if clicks_button:
        msg = f"""df = df.groupby({state_by}, axis={state_axis}).sum()"""
        if name_button == "Apply":
            try:
                df = apply_function(data, state_by, state_axis)
                msg = html.H6(f"df.groupby({state_by}).sum()",
                              style={"color": "white", "font-size": "1vmax", "margin-left": "2%"})
                name_button, content = button_apply(df, msg, len(state_by))
                state_by = select_labels(df, state_axis, True)
            except (KeyError, ValueError) as err:
                content = (html.H6(err.__str__(),
                                   style={"color": "white", "font-size": "1vmax", "margin-left": "2%"}),)
        else:
            df = save_function(data)
            name_button, content = button_save(
                f"""users/{data["user"]}/workflow.txt""", msg
            )
            state_by = select_labels(df, state_axis, True)
    else:
        df = read_json(data["df"])
        state_by = select_labels(df, state_axis, True)
        content = ""
        name_button = "Apply"
    content = html.Div(content)
    return [content, data, "", name_button, 0, state_by]
