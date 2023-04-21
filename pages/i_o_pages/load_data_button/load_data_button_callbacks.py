import os
import shutil
from tkinter import filedialog

from dash import Input, Output, State, callback, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from pandas import read_sql
from sqlalchemy import create_engine

from my_dash.my_html.my_div import my_div
from pages.i_o_pages.load_data_button.load_data_button_functions import \
    read_data

id_page = "load_data"


# botones
@callback([
           Output(f"{id_page}_div_archivos", "hidden"),
           Output(f"{id_page}_div_db", "hidden"),
           Output(f"{id_page}_archivos", "n_clicks"),
           Output(f"{id_page}_database", "n_clicks"),
           Output(f"{id_page}_content", "style"),
           Output(f"{id_page}_content", "children", allow_duplicate=True),
          ],
          [
           Input(f"{id_page}_archivos", "n_clicks"),
           Input(f"{id_page}_up_file", "n_clicks"),
           Input(f"{id_page}_database", "n_clicks"),
          ],
    prevent_initial_call=True)
def load_data(click_archivos, click_up, click_db):    
    hidden_arch = True
    hidden_db = True
    style = {"margin-top": "5%", "margin-left": "15%"}
    if click_archivos:
        hidden_arch = False
        style = {"margin-top": "7%", "margin-left": "3.5%"}
    if click_db:
        hidden_db = False
        style = {"margin-top": "7%", "margin-left": "3.5%"}
    return [hidden_arch, hidden_db, 0, 0, style, ""]

            
#dropdown Archivos
@callback([
           Output(f"{id_page}_drop_file", "options"),
           Output(f"{id_page}_drop_file", "value"),
          ],
          Input(f"{id_page}_archivos", "n_clicks"),
          State("main_page_store", "data"),
    prevent_initial_call=True)
def load_data(drop_dir, data):    
    file = ""   
    list_dir = os.listdir(f"""users/{data["user"]}/data""")

    if len(list_dir) > 0:
        file = list_dir[0]   
    return [list_dir, file]
         
    
# content archivos
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
        State(f"{id_page}_drop_file", "value"),        
        State("main_page_store", "data")
    ],
    prevent_initial_call=True)
def load_data(accept, input_value, data): 
    
    if accept:
        if input_value is not None and len(input_value) > 0:
            path = f"""users/{data["user"]}/data/{input_value}"""  
            data["df"] = read_data(input_value.split('.')[-1], path)         
            load_data_content = html.H6("DataFrame Cargado")
            hidden = False
        else:
            load_data_content = html.H6("Seleccione Archivos") 
    else:
        raise PreventUpdate   
    return [data, load_data_content, hidden]


#up_file from local
@callback(Output(f"{id_page}_content", "children", allow_duplicate=True),      
          Input(f"{id_page}_up_file", "n_clicks"),
          State("main_page_store", "data"),
          prevent_initial_call=True
)
def load_data(n_clicks, data):
    
    archivo = filedialog.askopenfilename()

    if type(archivo) != tuple:
        filename = archivo.split('/')[-1]        
        shutil.copy(archivo, f"""users/{data["user"]}/data/{filename}""")    
        msg = html.H6("Archivo subido")    
    else:
        msg = ""
    return msg


#up file from database
@callback(Output(f"{id_page}_content", "children", allow_duplicate=True),      
          Input(f"{id_page}_aceptar_db", "n_clicks"),
          [
           State(f"{id_page}_user", "value"),
           State(f"{id_page}_password", "value"),
           State(f"{id_page}_host", "value"),
           State(f"{id_page}_port", "value"),
           State(f"{id_page}_bd", "value"),
           State(f"{id_page}_schema", "value"),
           State(f"{id_page}_table", "value"),
           State("main_page_store", "data"),
          ],
          prevent_initial_call=True
)
def load_data(n_clicks, user, password, host, port, bd, schema, table, data):
    
    try:
        engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{bd}")
        query = f"select * from {table}"
        if schema:
            query = f"select * from {schema}.{table}"
        read_sql(query, engine).to_csv(f"""users/{data["user"]}/data/{table}.csv""")
        msg = my_div({"margin-left": "30%"}, "", html.H6(f"Archivo guardado como {table}.csv"))
        engine.dispose()
    except:
        msg = my_div({"margin-left": "30%"}, "", html.H6("Datos Erroneos"))
    return msg