from dash import dcc, html

from my_dash.my_dbc.my_button import my_button
from my_dash.my_dcc.my_dropdown import my_dropdown
from my_dash.my_html.my_div import my_div
from pages.dataframe_pages.data_pages.load_data_button.load_data_button_callbacks import *
from pages.dataframe_pages.data_pages.load_data_button.load_data_button_css import *

id_page = "load_data"

layout = my_div(style_div_main, "",
                [my_div(style_div_titles, "",                        
                        [
                         my_button(f"{id_page}_archivos", "Archivos",
                                   style_boton_files,
                                   className="btn btn-outline-primary",
                                   color="black"
                         ),   
                         my_button(f"{id_page}_up_file", "Up File from Local",
                                   style_boton_files,
                                   className="btn btn-outline-primary",
                                   color="black"
                         ),       
                         my_button(f"{id_page}_database", "Up File from DataBase",
                                   style_boton_files,
                                   className="btn btn-outline-primary",
                                   color="black"
                         ),  
                         html.A("Documentacion",
                                 href="https://pandas.pydata.org/docs/reference/io.html",
                                 style=style_A,
                                 target="_blank"),
                        ]),
                 my_div(style_div_dropdown_archivos, f"{id_page}_div_archivos",
                        [
                         my_div(style_selector, "",
                                my_dropdown(f"{id_page}_drop_file",
                                            {"background": background_in_dropdown}),
                         ),
                         my_button(f"{id_page}_aceptar", "Aceptar",
                                   style_boton_aceptar,
                                   className="btn btn-outline-warning",
                                   color="black"),    
                        ], hidden=True,
                 ),        
                 my_div(style_div_dropdown_db, f"{id_page}_div_db",
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
                        ], hidden=True,
                 ),          
                 my_div({}, f"{id_page}_content")
                ]
         )
