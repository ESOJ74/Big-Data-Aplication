import re

from dash import Input, Output, State, callback, html
from pandas import read_json

from utils.button_apply import button_apply, button_save
from utils.create_callback_content_up import create_callback_content_up
from utils.create_callback_hidden_button_cover import \
    create_callback_hidden_button_cover
from utils.create_callback_style_content_left import \
    create_callback_style_content_left
from utils.save_function import save_function

from ...common_css import *

id_page = "replace"


create_callback_hidden_button_cover(f"{id_page}_content_down")
create_callback_content_up(id_page)
create_callback_style_content_left(id_page)


def apply_function(data, to_replace, value, limit, regex):
    df = read_json(data["df"])
    df.replace(
        to_replace=to_replace, value=value, limit=limit, regex=regex, inplace=True
    )
    data["prov_df"] = df.to_json(orient="columns")
    return df


@callback(
    [
        Output(f"{id_page}_div_graph", "children"),
        Output("main_page_store", "data", allow_duplicate=True),
        Output(f"{id_page}_loading", "children"),
        Output(f"{id_page}_refresh", "children"),
        Output(f"{id_page}_refresh", "n_clicks"),
    ],
    [
        Input(f"{id_page}_refresh", "n_clicks"),
        Input(f"{id_page}_to_replace", "value"),
        Input(f"{id_page}_value", "value"),
        Input(f"{id_page}_limit", "value"),
        Input(f"{id_page}_regex", "value"),
    ],
    [
        State("main_page_store", "data"),
        State(f"{id_page}_to_replace", "value"),
        State(f"{id_page}_value", "value"),
        State(f"{id_page}_limit", "value"),
        State(f"{id_page}_regex", "value"),
        State(f"{id_page}_refresh", "children"),
    ],
    prevent_initial_call=True,
)
def add_data_to_fig(
    clicks_button,
    click,
    click2,
    click3,
    click4,
    data,
    to_replace,
    value,
    limit,
    regex,
    name_button,
):
    if clicks_button:
        try:
            to_replace = float(to_replace) if "." in to_replace else int(to_replace)
        except:
            pass

        try:
            value = float(value) if "." in value else int(value)
        except:
            pass

        limit = None if limit == " " else int(limit)
        regex = True if regex == "True" else False
        cod1 = f"""df = df.replace(to_replace="{to_replace}", """
        cod2 = f"value={value}, "
        cod3 = f"limit={limit}, regex={regex})"
        if regex == True:
            cod1 = f"""df.replace(to_replace=r"{to_replace}", """
            to_replace = re.compile(to_replace)
        if value:
            cod2 = f"""value="{value}", """

        msg = cod1 + cod2 + cod3
        if name_button == "Apply":
            try:
                df = apply_function(data, to_replace, value, limit, regex)
                msg = html.H6(msg, style=style_div_code)
                name_button, content = button_apply(id_page, df, msg)
            except (KeyError, ValueError, TypeError) as err:
                content = (html.H6(err.__str__(), style={"color": color_code}),)
        else:
            df = save_function(data)
            file_path = f"""users/{data["user"]}/workflow.txt"""
            name_button, content = button_save(file_path, msg)
    else:
        df = read_json(data["df"])
        content = ""
        name_button = "Apply"
    return [content, data, "", name_button, 0]
