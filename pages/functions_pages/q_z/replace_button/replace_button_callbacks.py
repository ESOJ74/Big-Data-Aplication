from dash import Input, Output, State, callback, html
from dash.exceptions import PreventUpdate
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

from ...common_css import *

id_page = "replace"


create_callback_hidden_button_cover(f"{id_page}_content_down")


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
    Input("replace_button", "n_clicks"),
    prevent_initial_call=True,
)
def second_callback(n_clicks):
    return my_div(
        style_div_title,
        "",
        [
            html.H5("DataFrame.replace()", style=style_title),
            html.A(
                "Documentacion",
                href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.replace.html",
                target="_blank",
            ),
        ],
    )


@callback(
    [
        Output(f"{id_page}_div_graph", "children"),
        Output("main_page_store", "data", allow_duplicate=True),
        Output(f"{id_page}_loading", "children"),
        Output(f"{id_page}_refresh", "children"),
        Output(f"{id_page}_refresh", "n_clicks"),
    ],
    [Input(f"{id_page}_refresh", "n_clicks")],
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
def add_data_to_fig(clicks_button, data, to_replace, value, limit, regex, name_button):
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
            import re

            cod1 = f"""df.replace(to_replace=r"{to_replace}", """
            to_replace = re.compile(to_replace)
        if value:
            cod2 = f"""value="{value}", """

        action = cod1 + cod2 + cod3

        if name_button == "Apply":
            try:
                df = read_json(data["df"]).replace(
                    to_replace=to_replace, value=value, limit=limit, regex=regex
                )
                data["prov_df"] = df.to_json(orient="columns")
                msg = html.H6(action, style=style_div_code)
                name_button, content = button_apply(id_page, df, msg)
            except (KeyError, ValueError, TypeError) as err:
                content = (html.H6(err.__str__(), style={"color": color_code}),)
        else:
            df = read_json(data["prov_df"])
            data["df"] = df.to_json(orient="columns")
            name_button, content = button_save(
                f"""users/{data["user"]}/workflow.txt""", ["", action]
            )
    else:
        raise PreventUpdate
    return [content, data, "", name_button, 0]


@callback(
    [
        Output(f"{id_page}_div_graph", "children", allow_duplicate=True),
        Output(f"{id_page}_refresh", "children", allow_duplicate=True),
    ],
    [
        Input(f"{id_page}_to_replace", "value"),
        Input(f"{id_page}_value", "value"),
        Input(f"{id_page}_limit", "value"),
        Input(f"{id_page}_regex", "value"),
    ],
    prevent_initial_call=True,
)
def add_data_to_fig(value1, value2, value3, value4):
    return ["", "Apply"]
