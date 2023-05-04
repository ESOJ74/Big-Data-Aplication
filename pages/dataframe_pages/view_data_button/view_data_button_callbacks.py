from dash import Input, Output, State, callback, html
from pandas import read_json

from assets.layout_templates.main_page.common_css import *
from assets.my_dash.my_html.my_div import my_div
from utils.create_agGrid import create_adgrid
from utils.create_callback_button_cover import create_callback_button_cover

id_page = "view_data"


create_callback_button_cover(id_page, f"{id_page}_content_down")

@callback([
           Output(f"{id_page}_content_down", 'children'),
           Output(f"{id_page}_loading", "children")
          ],       
          Input('view_data_button', 'n_clicks'),
          State('main_page_store', 'data'))
def view_data(n_clicks, data):

    obj = []
    if "df" in data:
        df = read_json(data["df"]) 
        obj = my_div({"margin-top": "1%"}, "",
                     create_adgrid(f"{id_page}_ag-table", df))
    else:
        obj = [html.H6('No hay ningún DataFrame Cargado',
                       style={"margin-left": "4%", 
                              "margin-top": "2%",
                              "color": color_boton_1})]
    return [obj, ""]
