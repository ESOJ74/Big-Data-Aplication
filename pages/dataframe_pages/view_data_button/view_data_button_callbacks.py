from dash import Input, Output, Patch, State, callback, html
from pandas import read_json

from assets.layout_templates.main_page.common_css import *
from assets.my_dash.my_dbc.my_button import my_button
from utils.create_agGrid import create_adgrid
from utils.create_callback_button_cover import \
    create_callback_button_cover

style_boton_files = {  
    "margin-left": "1%",
    "margin-bottom": "1%",
    "width": "13%",
    "font-size": "0.7vmax",
    "border": "2px solid",
    "font-family": font_family,
    "color": color_boton_1,
}

id_page = "view_data"


@callback([
           Output('view_data_content', 'children'),
           Output('add-data-rows', 'disabled'),
          ],
          Input('view_data_button', 'n_clicks'),
          State('main_page_store', 'data'))
def view_data(n_clicks, data):

    obj = []
    try:        
        df = read_json(data["df"])[0:10]
        obj.append(
            [my_button(f"{id_page}_add-data-rows", "View full DataFrame",
                                   style_boton_files,
                                   className="btn btn-outline-primary",
                                   color="black"
                         ), 
            create_adgrid(f"{id_page}_ag-table", df)])
        obj.append(False)
    except (TypeError, KeyError, ValueError):
        obj = [html.H6('No hay ningún DataFrame Cargado',
                       style={"margin-left": "20%", "color": color_boton_1}), True]
    return obj


@callback([
           Output(f"{id_page}_ag-table", "rowData"),
           Output(f"{id_page}_add-data-rows", "disabled", allow_duplicate=True),
          ],
          Input(f"{id_page}_add-data-rows", "n_clicks"),
          State("main_page_store", "data"),
          prevent_initial_call=True,)
def add_data_to_fig(n_clicks, data):    
    df = read_json(data["df"])[10:]
    patched_table = Patch()
    patched_table.extend(df.to_dict("records"))
    return [patched_table, True]


create_callback_button_cover(id_page)