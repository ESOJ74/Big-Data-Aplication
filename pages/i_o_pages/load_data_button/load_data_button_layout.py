from dash import dcc, html

from my_dash.my_dbc.my_button import my_button
from my_dash.my_dcc.my_dropdown import my_dropdown
from my_dash.my_html.my_div import my_div
from pages.i_o_pages.load_data_button.load_data_button_callbacks import *
from pages.i_o_pages.load_data_button.load_data_button_css import *
from pages.i_o_pages.load_data_button.load_data_button_lists import \
    list_of_format

"""
El código presentado define una variable layout que contiene la estructura visual de una
página web, utilizando la librería Dash de Python.

La página consiste en un div principal (my_div) con dos elementos hijos:
 -un div con un menú desplegable (my_dropdown) y un campo de entrada de texto (dcc.Input),
  y un botón (my_button) para aceptar la selección.
-También hay otro div para el contenido que se cargará en la página (my_div con id igual
 a "{id_page}_content").

Cada uno de los componentes visuales es personalizado a través de distintas variables de estilo
(style_div_main, style_div_dropdown, style_div_input, style_boton_aceptar y style_div_load_data_content).
"""

id_page = "load_data"

layout = my_div(style_div_main, "",
                [my_div(style_div_titles, "",
                        [my_button(f"{id_page}_archivos", "Archivos", style_boton_files,
                                   className="btn btn-outline-primary", color="black"),   
                         my_button(f"{id_page}_up_file", "Up File from Local", style_boton_files,
                                   className="btn btn-outline-primary", color="black"),       
                         my_button(f"{id_page}_database", "Up File from DataBase", style_boton_files,
                                   className="btn btn-outline-primary", color="black"),  
                        ]),
                 my_div(style_div_dropdown_archivos, f"{id_page}_div_archivos",
                        [
                         my_div(s_selector_arch, "",
                                my_dropdown(f"{id_page}_drop_file",
                                            {"background": "#B0B3B3"},
                                            placeholder="Select format"
                                ),
                         ),
                         my_button(f"{id_page}_aceptar", "Aceptar", style_boton_aceptar_load),    
                        ], hidden=True,
                 ),        
                 my_div(style_div_dropdown_db, f"{id_page}_div_db",
                        [
                         my_div(s_selector_db, "",
                                [
                                 html.H6("User"),
                                 dcc.Input(id=f"{id_page}_user",style={"width": "100%"}),
                                 my_div({"margin-top": "3%"}, "", html.H6("Password")),
                                 dcc.Input(id=f"{id_page}_password",style={"width": "100%"}),     
                                 my_div({"margin-top": "3%"}, "", html.H6("Host")),
                                 dcc.Input(id=f"{id_page}_host",style={"width": "100%"}), 
                                 my_div({"margin-top": "3%"}, "", html.H6("Port")),
                                 dcc.Input(id=f"{id_page}_port",style={"width": "100%"}), 
                                 my_div({"margin-top": "3%"}, "", html.H6("DataBase")),
                                 dcc.Input(id=f"{id_page}_bd",style={"width": "100%"}), 
                                 my_div({"margin-top": "3%"}, "", html.H6("Schema")),
                                 dcc.Input(id=f"{id_page}_schema",style={"width": "100%"}),
                                 my_div({"margin-top": "3%"}, "", html.H6("Table")),
                                 dcc.Input(id=f"{id_page}_table",style={"width": "100%"}),
                                ],
                         ),
                         my_button(f"{id_page}_aceptar_db", "Aceptar", style_boton_aceptar_up_file),    
                        ], hidden=True,
                 ),          
                 my_div({}, f"{id_page}_content")
                ]
         )
