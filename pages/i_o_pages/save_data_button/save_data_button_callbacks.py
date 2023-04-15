import os

from dash import html, Input, Output, State, callback
from pandas import read_json
import openpyxl

id_page = "save_data"


@callback(Output(f"{id_page}_content", "children"),
          Input(f"{id_page}_aceptar", "n_clicks"),
          [
            State(f"{id_page}_input", "value"),
            State(f"{id_page}_dropdown", "value"),
            State("main_page_store", "data"),
          ],
          prevent_initial_call=True,)
def save_data(n_clicks, input_value, drop_value, data):
    
    load_data_content = html.H6("Introduzca el nombre para el archivo")
    if input_value is not None:
        load_data_content = html.H6("DataFrame Guardado")
        try:
            df = read_json(data["df"])
            match drop_value:
                case "To CSV":
                    if os.path.exists(f"""users/{data["user"]}/csv""")==False:                        
                        os.mkdir(f"""users/{data["user"]}/csv""")
                    df.to_csv(f"""users/{data["user"]}/csv/{input_value}.csv""", index=False)
                case "To JSON":
                    if os.path.exists(f"""users/{data["user"]}/json""")==False:                        
                        os.mkdir(f"""users/{data["user"]}/json""")
                    df.to_json(f"""users/{data["user"]}/json/{input_value}.json""")
                case "To EXCEL":
                    if os.path.exists(f"""users/{data["user"]}/excel""")==False:                        
                        os.mkdir(f"""users/{data["user"]}/excel""")
                    df.to_excel(f"""users/{data["user"]}/excel/{input_value}.xlsx""", index=False) 
        except (TypeError, KeyError):
            load_data_content = html.H6("No hay DataFrame cargado")
    return load_data_content
