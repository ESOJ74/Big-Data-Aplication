from dash import Input, Output, State, callback, html
from pandas import read_json

from assets.layout_templates.main_page.common_css import (
    style_content_left,
    style_content_left2,
)
from assets.my_dash.my_html.my_div import my_div
from utils.button_apply import button_apply, button_save
from utils.create_callback_hidden_button_cover import (
    create_callback_hidden_button_cover,
)
from utils.select_labels import select_labels

from ...common_css import *

id_page = "drop"


create_callback_hidden_button_cover(f"{id_page}_content_up")


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
    Input("drop_button", "n_clicks"),
    prevent_initial_call=True,
)
def second_callback(n_clicks):
    return my_div(
        style_div_title,
        "",
        [
            html.H5("DataFrame.drop()", style=style_title),
            html.A(
                "Documentacion",
                href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html",
                target="_blank",
            ),
        ],
    )


@callback(
    Output(f"{id_page}_labels", "options"),
    Input(f"{id_page}_axis", "value"),
    State("main_page_store", "data"),
)
def display_page(axis, data):
    df = read_json(data["df"])
    return select_labels(df, axis)


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
    action = f"""df = df.drop({state_labels_value}, axis={state_axis})"""
    if clicks_button:
        if name_button == "Apply":
            try:
                df = read_json(data["df"]).drop(state_labels_value, axis=state_axis)
                data["prov_df"] = df.to_json(orient="columns")
                if type(state_labels_value) == str:
                    state_labels_value = [state_labels_value]
                msg = html.H6(
                    f"df.drop(labels={state_labels_value}, axis={state_axis})",
                    style=style_div_code,
                )
                name_button, content = button_apply(id_page, df, msg)
                labels = select_labels(df, state_axis)
            except (KeyError, ValueError) as err:
                content = (html.H6(err.__str__(), style={"color": color_code}),)
        else:
            df = read_json(data["prov_df"])
            data["df"] = df.to_json(orient="columns")
            name_button, content = button_save(
                f"""users/{data["user"]}/workflow.txt""", ["", action]
            )
            labels = select_labels(df, state_axis)
    else:
        df = read_json(data["df"])
        labels = select_labels(df, state_axis)
        content = ""
        name_button = "Apply"
    return [content, data, "", name_button, 0, labels]


@callback(
    Output(f"{id_page}_refresh", "children", allow_duplicate=True),
    Input(f"{id_page}_labels", "value"),
    prevent_initial_call=True,
)
def add_data_to_fig(labels_value):
    return "Apply"
