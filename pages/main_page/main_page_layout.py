from dash import dcc

from my_dash.my_html.my_div import my_div
from pages.main_page.main_page_callbacks import *
from pages.main_page.main_page_css import *
from pages.main_page.main_page_functions import create_div_buttons
from pages.main_page.main_page_lists import (buttons, functions, models,
                                             visualizations)

"""
La variable layout es un diccionario que define el diseño de una página web. 
Se crea utilizando la función my_div, que es una función que crea un elemento 
div con las propiedades CSS y los elementos hijos especificados en los argumentos.

Argumentos:

style_div_main (dict): Un diccionario que contiene las propiedades CSS para aplicar
 al elemento div principal.
id_page (str): Un identificador único para la página web.
style_div_buttons (dict): Un diccionario que contiene las propiedades CSS para
 aplicar al panel de botones.
style_div_content (dict): Un diccionario que contiene las propiedades CSS para
 aplicar al panel de contenido.
style_div_1, style_div_2 (dict): Diccionarios que contienen las propiedades
 CSS para aplicar a los elementos div del panel de botones y el panel de contenido.
buttons, visualizations, functions, models (list): Listas de tuplas que contienen
 la información necesaria para crear los botones en el panel de botones.
Retorno:

layout (dict): Un diccionario que contiene el diseño de la página web.
"""

id_page = "main_page"

layout: dict = my_div(style_div_main, "",
                      [
                       dcc.Store(id=f"{id_page}_store"),                       
                       # Up Panel
                       my_div(style_up_panel, ""),
                       # Middle Panel
                       my_div({"width": "100%", "height": "92%", }, "",
                              [
                               # Left Panel
                               my_div(style_div_buttons, f"{id_page}_left",
                                      [
                                       # User panel
                                       my_div({"position": "relative", "top": "1%", "left": "2%"}, "", 
                                              dcc.Input(id=f"{id_page}_user",
                                                        placeholder="Usuario",
                                                        style={"width": "70%"},
                                                        debounce=True
                                              ),
                                       ),
                                       # DataFrame panel
                                       create_div_buttons(style_div_1, "DataFrame", buttons),
                                       # Div for Visualizations panel, Functions panel, Models panel
                                       my_div({"height": "80%"}, f"{id_page}_div_functions",
                                              [
                                               # Visualizations panel
                                               create_div_buttons(
                                                   style_div_2, "Visualizations", visualizations),
                                               # Functions panel
                                               create_div_buttons(
                                                   style_div_2, "Functions", functions),
                                               # Models panel
                                               create_div_buttons(
                                                   style_div_2, "Models", models),
                                              ],
                                              hidden=True,
                                       ),
                                     ],
                               ),
                               # Central Panel
                               my_div(style_div_content, f"{id_page}_page_content"),                               
                              ]
                       ),
                       # Down Panel
                       my_div(style_up_panel, ""),
                      ]
               )
