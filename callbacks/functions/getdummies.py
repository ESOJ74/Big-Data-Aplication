from pandas import get_dummies, read_json
from dash import Input, Output, State, callback, html

from utils.buttons import button_apply, button_save
from utils.in_out import save_function
from utils.selector_options import selector_options

id_page = "getdummies"

selector_options(id_page, f"{id_page}_prefix")
selector_options(id_page, f"{id_page}_columns")


def apply_function(
    data,
    state_prefix,
    state_dummy_na,
    state_columns,
    state_sparse,
    state_drop_first,
    state_dtype_2,
):
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
    return df


@callback(
    [
        Output(f"{id_page}_content_down", "children"),
        Output("main_page_store", "data", allow_duplicate=True),
        Output("loading", "children", allow_duplicate=True),
        Output(f"{id_page}_refresh", "children"),
        Output(f"{id_page}_refresh", "n_clicks"),
    ],
    [
        Input(f"{id_page}_refresh", "n_clicks"),
        Input(f"{id_page}_prefix", "value"),
        Input(f"{id_page}_dummy_na", "value"),
        Input(f"{id_page}_columns", "value"),
        Input(f"{id_page}_sparse", "value"),
        Input(f"{id_page}_drop_first", "value"),
        Input(f"{id_page}_dtype", "value"),
    ],
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
    value1,
    value2,
    value3,
    value4,
    value5,
    value6,
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
            state_dummy_na = state_dummy_na == "True"
            state_sparse = state_sparse == "True"
            state_drop_first = state_drop_first == "True"
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
        cod2 = f" columns={state_columns}, sparse={state_sparse}, drop_first={state_drop_first},"  # noqa: E501
        cod3 = f" dtype={state_dtype})"
        msg = cod1 + cod2 + cod3

        if name_button == "Apply":
            try:
                df = apply_function(
                    data,
                    state_prefix,
                    state_dummy_na,
                    state_columns,
                    state_sparse,
                    state_drop_first,
                    state_dtype_2,
                )
                msg = html.H6(
                    msg,
                    style={"color": "white", "font-size": "1vmax", "margin-left": "2%"},
                )
                name_button, content = button_apply(df, msg)
            except (KeyError, ValueError) as err:
                content = (
                    (
                        html.H6(
                            err.__str__(),
                            style={
                                "color": "white",
                                "font-size": "1vmax",
                                "margin-left": "2%",
                            },
                        )
                    ),
                )
        else:
            df = save_function(data)
            name_button, content = button_save(
                f"""users/{data["user"]}/workflow.txt""", msg
            )
    else:
        content = ""
        name_button = "Apply"
    content = html.Div(content)
    return [content, data, "", name_button, 0]
