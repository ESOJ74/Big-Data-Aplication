from dash import Input, Output, State, callback, html
from dash.exceptions import PreventUpdate
from pandas import get_dummies, read_json

from assets.my_dash.my_html.my_div import my_div
from utils.button_apply import button_apply, button_save
from utils.common_div_utils import selector_options
from utils.create_callback_button_cover import create_callback_button_cover

from ...common_css import *

id_page = "get_dummies"


create_callback_button_cover(id_page, f"{id_page}_content_down")
selector_options(id_page, f"{id_page}_prefix")
selector_options(id_page, f"{id_page}_columns")


@callback(
    Output(f"{id_page}_content_up", "children"),
    Input("get_dummies_button", "n_clicks"),
    prevent_initial_call=True,
)
def second_callback(n_clicks):
    return my_div(
        style_div_title,
        "",
        [
            html.H5("DataFrame.get_dummies()", style=style_title),
            html.A(
                "Documentacion",
                href="https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html",
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
    Input(f"{id_page}_refresh", "n_clicks"),
    [
        State("main_page_store", "data"),
        State(f"{id_page}_prefix", "value"),
        State(f"{id_page}_dummy_na", "value"),
        State(f"{id_page}_columns", "value"),
        State(f"{id_page}_sparse", "value"),
        State(f"{id_page}_drop_first", "value"),
        State(f"{id_page}_dtype", "value"),
        State(f"{id_page}_refresh", "children"),
    ],
    prevent_initial_call=True,
)
def add_data_to_fig(
    clicks_button,
    data,
    state_prefix,
    state_dummy_na,
    state_columns,
    state_sparse,
    state_drop_first,
    state_dtype,
    name_button,
):
    if clicks_button:
        if state_prefix is not None and len(state_prefix) < 1 or state_prefix[0] == " ":
            state_prefix = None
        if (
            state_columns is not None
            and len(state_columns) < 1
            or state_columns[0] == " "
        ):
            state_columns = None
            state_dummy_na = True if state_dummy_na == "True" else False
            state_sparse = True if state_sparse == "True" else False
            state_drop_first = True if state_drop_first == "True" else False
        match state_dtype:
            case "int":
                state_dtype_2 = int
            case "float":
                state_dtype_2 = float
            case "str":
                state_dtype_2 = str
            case "bool":
                state_dtype_2 = bool

        cod1 = (
            f"df = pd.get_dummies(df, prefix={state_prefix}, dummy_na={state_dummy_na},"
        )
        cod2 = f" columns={state_columns}, sparse={state_sparse}, drop_first={state_drop_first},"
        cod3 = f" dtype={state_dtype})"
        action = cod1 + cod2 + cod3

        if name_button == "Apply":
            try:
                df = read_json(data["df"])
                df = get_dummies(
                    df,
                    prefix=state_prefix,
                    dummy_na=state_dummy_na,
                    columns=state_columns,
                    sparse=state_sparse,
                    drop_first=state_drop_first,
                    dtype=state_dtype_2,
                )

                data["prov_df"] = df.to_json(orient="columns")
                msg = html.H6(action, style=style_div_code)
                name_button, content = button_apply(id_page, df, msg)
            except (KeyError, ValueError) as err:
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
        Input(f"{id_page}_prefix", "value"),
        Input(f"{id_page}_dummy_na", "value"),
        Input(f"{id_page}_columns", "value"),
        Input(f"{id_page}_sparse", "value"),
        Input(f"{id_page}_drop_first", "value"),
        Input(f"{id_page}_dtype", "value"),
    ],
    prevent_initial_call=True,
)
def add_data_to_fig(value1, value2, value3, value4, value5, value6):
    return ["", "Apply"]
