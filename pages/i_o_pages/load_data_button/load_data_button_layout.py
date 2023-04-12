from dash import dcc

from my_dash.my_dcc.my_dropdown import my_dropdown
from my_dash.my_dbc.my_button import my_button
from my_dash.my_html.my_div import my_div
from pages.i_o_pages.load_data_button.load_data_button_callbacks import *
from pages.i_o_pages.load_data_button.load_data_button_css import *
from pages.i_o_pages.load_data_button.load_data_button_lists import list_of_format

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
                [
                 my_div(style_div_dropdown, "",
                        [
                         my_div(s_selector, "",
                                my_dropdown(f"{id_page}_dropdown",
                                            {"background": "#555958"},
                                            list_of_format,
                                            value="From CSV",
                                            placeholder="Select format"
                                ),
                         ),
                         my_div(style_div_input, "",
                                dcc.Input(id=f"{id_page}_input",
                                          placeholder="Introduce la ruta del archivo",
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
