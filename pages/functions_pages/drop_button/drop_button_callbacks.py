from dash import Input, Output, State, callback, html
from dash.exceptions import PreventUpdate
from pandas import read_json

from assets.functions_css import *
from common_functions.create_agGrid import create_adgrid
from common_functions.create_callback_button_cover import \
    create_callback_button_cover
from common_functions.create_callback_button_save import \
    create_callback_button_save
from common_functions.create_content_up import create_single_dropdown
from my_dash.my_dbc.my_button import my_button
from my_dash.my_html.my_div import my_div

id_page = "drop"


create_callback_button_cover(id_page)
create_callback_button_save(id_page)
create_single_dropdown(id_page, f"{id_page}_div_dropdown", style_selector)


@callback(
    [
      Output(f"{id_page}_content", "children", allow_duplicate=True),
      Output("main_page_store", "data", allow_duplicate=True),
      Output(f"{id_page}_loading", "children", allow_duplicate=True),
    ],
    Input(f"{id_page}_dropdown", "value"),
    [      
      State(f"{id_page}_dropdown", "value"),
      State("main_page_store", "data"),
    ],
    prevent_initial_call=True,)
def add_data_to_fig(accept, value, data):     
    if accept:        
        try:
            df = read_json(data["df"]).drop([f"{value}"], axis=1)  
            data["prov_df"] = df.to_json(orient="columns")
            content = [
                       my_div({"margin-top": "3%", "width": "97%"}, "",
                              create_adgrid(f"{id_page}_ag-table", df.head())
                       ),
                       html.H6(f"df.drop([{value}], axis=1)",
                               style={"margin-top": "2%", "color": "#b0d8d3"}),
                       my_div({"margin-top": "1%"}, "",    
                              my_button(f"{id_page}_save", "Save",
                                        style_boton_aceptar,
                                        className="btn btn-outline-warning",
                                        color="black") 
                       )]
        except KeyError:
            content = html.H6("Seleccione una columna", style={"color": "#acf4ed"}),
    else:
        raise PreventUpdate
    return [content, data, ""]
