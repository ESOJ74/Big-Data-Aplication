import os
import shutil
from tkinter import filedialog

from dash import Input, Output, State, callback, dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from pandas import read_sql
from sqlalchemy import create_engine

from assets.layout_templates.main_page.common_css import *
from assets.my_dash.my_dbc.my_button import my_button
from assets.my_dash.my_dcc.my_dropdown import my_dropdown
from assets.my_dash.my_html.my_div import my_div
from utils.read_data import read_data

from .load_data_button_css import *

id_page = "load_data"


# botones
@callback(Output(f"{id_page}_content_down", "children"),
          Input(f"{id_page}_archivos", "n_clicks"),
          State("main_page_store", "data"),
          prevent_initial_call=True)
def load_data(n_clicks, data):    
    obj = html.H6("No tiene archivos",
                  style={"margin-left": "4%", "margin-top": "2%", "color": color_boton_1})    
    options = os.listdir(f"""users/{data["user"]}/data""")
    if len(options) > 0:
        obj = my_div({"width": "100%", "height": "90%"}, "",
                     my_div(style_div_dropdown_archivos, f"{id_page}_div_archivos",
                            [
                             my_div(style_selector, "",
                                    my_dropdown(f"{id_page}_drop_file",
                                                {"background": background_in_dropdown},
                                                options=options,
                                                value=options[0]
                                    ),
                             ),
                             my_button(f"{id_page}_aceptar", "Aceptar",
                                       style_boton_aceptar,
                                       className="btn btn-outline-warning",
                                       color="black"
                             ),    
                            ]))
    return obj
    

@callback([
           Output("main_page_store", "data", allow_duplicate=True),           
           Output(f"main_page_div_functions", "hidden"),    
           Output(f"main_page_div_data", "hidden", allow_duplicate=True),   
           Output(f"{id_page}_content_down", "children", allow_duplicate=True) 
          ],
          Input(f"{id_page}_aceptar", "n_clicks"),
          [
           State(f"{id_page}_drop_file", "value"),        
           State("main_page_store", "data")
          ],
          prevent_initial_call=True)
def load_data(accept, input_value, data):
    if accept:
        path = f"""users/{data["user"]}/data/{input_value}"""  
        data["df"] = read_data(input_value.split('.')[-1], path)      
        div_data_hidden = True  
    else:
        raise PreventUpdate   
    return [data, False, div_data_hidden,
            html.H6(f"DataFrame {input_value.split('.')[0]} preparado",
                    style=style_msg) ]


@callback(Output(f"{id_page}_content_down", "children", allow_duplicate=True),
          Input(f"{id_page}_database", "n_clicks"),
          State("main_page_store", "data"),
          prevent_initial_call=True)
def load_data(click_db, data):   
    return my_div(style_div_dropdown_db,
                  f"{id_page}_div_db",
                  [
                   my_div(s_selector_db, "",
                          [
                           html.H6("User", style=style_title_db),
                           dcc.Input(id=f"{id_page}_user",
                                     style=style_input),                                 
                           html.H6("Password", style=style_title_db),
                           dcc.Input(id=f"{id_page}_password",
                                     style=style_input),     
                           html.H6("Host", style=style_title_db),
                           dcc.Input(id=f"{id_page}_host",
                                     style=style_input),  
                           html.H6("Port", style=style_title_db),
                           dcc.Input(id=f"{id_page}_port",
                                     style=style_input),
                           html.H6("DataBase", style=style_title_db),
                           dcc.Input(id=f"{id_page}_bd",
                                     style=style_input), 
                           html.H6("Schema", style=style_title_db),
                           dcc.Input(id=f"{id_page}_schema",
                                     style=style_input),
                           html.H6("Table", style=style_title_db),
                           dcc.Input(id=f"{id_page}_table",
                                     style=style_input),
                         ],
                   ),
                   my_button(f"{id_page}_aceptar_db", "Aceptar",
                             style_boton_aceptar,
                             className="btn btn-outline-warning",
                             color="black"
                   ),    
                  ])


@callback(Output(f"{id_page}_content_down", "children", allow_duplicate=True),     
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
          prevent_initial_call=True)
def load_data(n_clicks, user, password, host, port, bd, schema, table, data):    
    if n_clicks:
        try:
            engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{bd}")
            query = f"select * from {table}"
            if schema:
                query = f"select * from {schema}.{table}"
            read_sql(query, engine).to_csv(f"""users/{data["user"]}/data/{table}.csv""")
            msg = my_div({"margin-left": "22vmax"}, "",
                        html.H6(f"Archivo guardado como {table}.csv",
                                style={"color": color_boton_1}))
            engine.dispose()
            msg = html.H6(f"Archivo guardardo como {table}.csv", style=style_msg)
        except:
            msg = html.H6("Datos Erroneos", style=style_msg)
        return msg
    else:
        raise PreventUpdate
    

#up_file from local
@callback(Output(f"{id_page}_content_down", "children", allow_duplicate=True),      
          Input(f"{id_page}_up_file", "n_clicks"),
          State("main_page_store", "data"),
          prevent_initial_call=True)
def load_data(n_clicks, data):    
    archivo = filedialog.askopenfilename()
    if type(archivo) != tuple:
        filename = archivo.split('/')[-1]        
        shutil.copy(archivo, f"""users/{data["user"]}/data/{filename}""")   
        msg = html.H6(f"Archivo guardardo como {filename}", style=style_msg)
    else:
        msg = ""
    return msg
