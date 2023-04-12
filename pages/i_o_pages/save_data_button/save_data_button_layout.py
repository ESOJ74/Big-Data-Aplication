from dash import dcc

from my_dash.my_dcc.my_dropdown import my_dropdown
from my_dash.my_dbc.my_button import my_button
from my_dash.my_html.my_div import my_div
from pages.i_o_pages.load_data_button.load_data_button_css import *
from pages.i_o_pages.save_data_button.save_data_button_callbacks import *
from pages.i_o_pages.save_data_button.save_data_button_list import list_of_format

id_page = "save_data"

layout = my_div(style_div_main, "",
                [
                 my_div(style_div_dropdown, "",
                        [
                         my_div(s_selector, "",
                                my_dropdown(f"{id_page}_dropdown",
                                            {"background": "#555958"},
                                            list_of_format,
                                            value="To CSV",
                                            placeholder="Select format"
                                ),
                         ),
                         my_div(style_div_input, "",
                                dcc.Input(id=f"{id_page}_input",
                                          placeholder="Introduce el nombre del archivo",
                                          style=style_input,
                                          debounce=True
                                )
                         ),
                         my_button(f"{id_page}_aceptar", "Aceptar", style_boton_aceptar)
                        ]
                 ),
                 my_div(style_div_load_data_content, f"{id_page}_content")
                ]
         )