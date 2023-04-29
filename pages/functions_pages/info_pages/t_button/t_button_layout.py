import os

from dash import Input, Output, State, callback, html
from pandas import read_csv, read_json

from common_functions.create_agGrid import create_adgrid
from common_functions.create_callback_button_cover import \
    create_callback_button_cover
from common_functions.create_layout.create_functions_layout import \
    create_functions_layout
from assets.my_dash.my_html.my_div import my_div
from pages.functions_pages.info_pages.common_css import *

id_page = "t"

layout = create_functions_layout(id_page)

create_callback_button_cover(id_page)


@callback(
        [
         Output(f"{id_page}_content", "children"),
         Output(f"{id_page}_loading", "children", allow_duplicate=True),
        ],
        Input("t_button", "n_clicks"),
        State("main_page_store", "data"),
    prevent_initial_call=True,)
def add_data_to_fig(n_clicks, data):     
    obj = []
    try:        
        df = read_json(data["df"]).head(15).T.reset_index()        
        df.rename(columns={'index': 'columns'}, inplace=True)
        df.to_csv("tmp.csv", index=False)
        df = read_csv("tmp.csv")    
        os.remove("tmp.csv")           
        obj.append(create_adgrid(f"{id_page}_ag-table", df))
        obj.append(False)
    except (TypeError, KeyError, ValueError):
        obj = [html.H6('No hay ningún DataFrame Cargado',
                       style={"margin-left": "20%", "color": "#b0d8d3"}), True]
    return [        
               my_div(style_div_content, "",
                      [
                       my_div(style_div_title, "",
                              [
                               html.H5("DataFrame.T()",
                                       style=style_title),
                               html.A("Documentacion",
                                      href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.T.html",
                                      target="_blank")
                              ],
                       ),
                       my_div(style_div_obj2, "", obj)
                      ],
               ), ""
              ]
