import os
import shutil
from tkinter import filedialog

from dash import Input, Output, State, callback, html
from dash.dependencies import Input, Output, State
from pandas import read_csv, read_json

id_page = "load_data"


# drop_dir
@callback([
           Output(f"{id_page}_drop_dir", "options"),
           Output(f"{id_page}_drop_dir", "value"),
          ],
          Input("load_data_button", "n_clicks"),
          State("main_page_store", "data"),
    prevent_initial_call=True
)
def load_data(n_clicks, data):
    list_dir = os.listdir(f"""users/{data["user"]}""")
    return [list_dir, list_dir[0]]


#drop_file
@callback([
           Output(f"{id_page}_drop_file", "options"),
           Output(f"{id_page}_drop_file", "value"),
          ],
          Input(f"{id_page}_drop_dir", "value"),
          State("main_page_store", "data"),
    prevent_initial_call=True
)
def load_data(drop_dir, data):
    list_dir = []
    file = ""
    try:
        list_dir = os.listdir(f"""users/{data["user"]}/{drop_dir}""")
        file = list_dir[0]
    except FileNotFoundError:
        pass
        
    return [list_dir, file]


#up_file
@callback([
           Output(f"{id_page}_content", "children", allow_duplicate=True),
           Output(f"{id_page}_up_file", "n_clicks"),
          ],
          Input(f"{id_page}_up_file", "n_clicks"),
          State("main_page_store", "data"),
    prevent_initial_call=True
)
def load_data(n_clicks, data):
    archivo = filedialog.askopenfilename()
    filename = archivo.split('/')[-1]
    extension = filename.split('.')[-1]
    if os.path.exists(f"""users/{data["user"]}/{extension}""")==False:
        os.mkdir(f"""users/{data["user"]}/{extension}""")
    shutil.copy(archivo, f"""users/{data["user"]}/{extension}/{filename}""")        
    return ["Archivo subido", 0]


@callback(
    [
        Output("main_page_store", "data", allow_duplicate=True),
        Output(f"{id_page}_content", "children"),
        Output(f"main_page_div_functions", "hidden"),
    ],
    [
        Input(f"{id_page}_aceptar", "n_clicks")
    ],
    [
        State(f"{id_page}_drop_dir", "value"),
        State(f"{id_page}_drop_file", "value"),        
        State("main_page_store", "data")
    ],
    prevent_initial_call=True
)
def load_data(accept, drop_value, input_value, data):   
    
    load_data_content = ""
    hidden = True
    data["df"] = ""    
    
    if input_value is not None and len(input_value) > 0:
        path = f"""users/{data["user"]}/{drop_value}/{input_value}"""  

        match drop_value:
            case "csv" | "txt":
                data["df"] = read_csv(path).to_json(orient="columns")
            case _:
                pass

        load_data_content = html.H6("DataFrame Cargado")
        hidden = False
            
    return [data, load_data_content, hidden]
