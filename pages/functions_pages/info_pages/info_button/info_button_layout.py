from dash import Input, Output, State, callback, html
from pandas import read_json

from assets.layout_templates.main_page.content_layout import \
    create_content_layout
from assets.my_dash.my_html.my_div import my_div
from utils.create_callback_hidden_button_cover import create_callback_hidden_button_cover

from ..common_css import *

id_page = "info"

layout = create_content_layout(
    id_page,
    my_div(style_div_content_up, f"{id_page}_content_up"),
    my_div(style_div_content_down, f"{id_page}_content_down"),
    my_div(style_div_params, ""),
)

create_callback_hidden_button_cover(f"{id_page}_content_down", True)


@callback(
    Output(f"{id_page}_content_up", "children"),
    Input("info_button", "n_clicks"),
    prevent_initial_call=True,
)
def second_callback(n_clicks):
    return my_div(
        style_div_title,
        "",
        [
            html.H5("DataFrame.info()", style=style_title),
        ],
    )


@callback(
    [
        Output(f"{id_page}_content_down", "children"),
        Output(f"{id_page}_loading", "children", allow_duplicate=True),
    ],
    Input("info_button", "n_clicks"),
    State("main_page_store", "data"),
    prevent_initial_call=True,
)
def add_data_to_fig(n_clicks, data):
    df = read_json(data["df"])

    stop = df.shape[0]
    columns = list(df.columns)
    list_index = list(range(len(columns)))
    list_non_null = df.isnull().sum()
    list_non_null = [
        f"{stop - list_non_null[column]} non-null" for column in list_non_null
    ]
    list_dtype = [df[column].dtype for column in columns]
    list_dtypes = dict((i, list_dtype.count(i)) for i in list_dtype)
    maxi = len(max(columns, key=len))

    texto = (
        "<class 'pandas.core.frame.DataFrame'>"
        + "\n"
        + f"RangeIndex: {stop} entries, 0 to {stop - 1}"
        + "\n"
        + f"Data Columns (total {len(columns)} columns)"
        + "\n"
        + f" #   Column{' '*(maxi - 4)}Non-Null Count  Dtype"
        + "\n"
        + f"---  ------{' '*(maxi - 4)}--------------  ----- "
    )
    for x in zip(list_index, columns, list_non_null, list_dtype):
        texto += "\n" + f" {x[0]}   {x[1]}{' '*(maxi + 2 - len(x[1]))}{x[2]}  {x[3]}"

    texto += (
        "\n"
        + f"dtypes: {', '.join([f'{key}({list_dtypes[key]})' for key in  list_dtypes])}"
        + "\n"
        + f"memory usage: {df.memory_usage(index=False).sum() / 1000} KB"
    )

    return [
        my_div(
            style_div_content,
            "",
            my_div(
                style_div_obj,
                "",
                html.Pre(texto, style=style_text2),
            ),
        ),
        "",
    ]
