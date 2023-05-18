from dash import Input, Output, State, callback, html
from pandas import read_json

from utils.button_apply import button_apply, button_save
from utils.create_callback_content_up import create_callback_content_up
from utils.create_callback_hidden_button_cover import \
    create_callback_hidden_button_cover
from utils.create_callback_style_content_left import \
    create_callback_style_content_left
from utils.save_function import save_function
from utils.select_labels import select_labels

from ...common_css import *

id_page = "groupby"


create_callback_hidden_button_cover(f"{id_page}_div_graph")
create_callback_content_up(id_page)
create_callback_style_content_left(id_page)


def apply_function(data, state_by, state_axis):
    df = read_json(data["df"])
    df = df.groupby(state_by, axis=state_axis).sum()
    df = df.reset_index()
    data["prov_df"] = df.to_json(orient="columns")
    return df


@callback(
    [
        Output(f"{id_page}_div_graph", "children"),
        Output("main_page_store", "data", allow_duplicate=True),
        Output(f"{id_page}_loading", "children"),
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
                msg = html.H6(f"df.groupby({state_by}).sum()", style=style_div_code)
                name_button, content = button_apply(id_page, df, msg, len(state_by))
                state_by = select_labels(df, state_axis, True)
            except (KeyError, ValueError) as err:
                content = (html.H6(err.__str__(), style={"color": color_boton_1}),)
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
    return [content, data, "", name_button, 0, state_by]
