import numpy as np
from dash import Input, Output, State, callback, dcc, html
from pandas import read_json, set_option

from assets.common_css import background_dark, background_light
from common_functions.create_callback_button_cover import \
    create_callback_button_cover
from my_dash.my_dbc.my_button import my_button
from my_dash.my_html.my_div import my_div
from pages.functions_pages.info_pages.common_css import *

id_page = "describe"

create_callback_button_cover(id_page)

@callback(
        [
         Output(f"{id_page}_content", "children"),
         Output(f"{id_page}_loading", "children", allow_duplicate=True),
        ],
        [
         Input("describe_button", "n_clicks"),
         Input(f"{id_page}_refresh", "n_clicks")
        ],
        [
         State("main_page_store", "data"),
         State(f"{id_page}_percentiles", "value"),
         State(f"{id_page}_include", "value"),
         State(f"{id_page}_exclude", "value"),
        ],
        prevent_initial_call=True,)
def add_data_to_fig(n_clicks, n_clicks2, data, percentiles, include, exclude):     
    set_option('display.max_columns', 500)
    set_option('display.width', 1000)

    if percentiles in ('', None):
        percentiles = None
    else:
        print(percentiles)
        percentiles = [float(x) for x in percentiles.split(" ")]
       
    if include in ('', None):
        include = None

    match include:
        case "all":
            include = "all"
        case "object":
            include = [object]
        case "number":
            include = [np.number]
        case "category":
            include = ['category']
        case _:
            include = None

    match exclude:
        case "object":
            exclude = [object]
        case "number":
            exclude = [np.number]
        case "category":
            exclude = ["category"]
        case _:
            exclude = None

    try:         
        return [
                my_div(style_div_content, "",
                    [
                     my_div(style_div_title, "",
                            [
                             html.H5("DataFrame.describe()", style=style_title),
                             html.A("Documentacion", 
                                    href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html",
                                    target="_blank")
                            ],
                     ),
                     my_div(style_div_obj, "",
                            html.Pre(read_json(data["df"]).describe(percentiles, include, exclude).__str__(),
                                     style=style_text)
                     ),
                    ],
                ), ""]
    except Exception as err:        
        return [html.Pre(str(err), style=style_msg), ""]
