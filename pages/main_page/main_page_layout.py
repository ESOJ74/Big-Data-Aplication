from dash import dcc

from common_functions.user_registry import user_login
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
                       user_login(id_page),               
                       # Up Panel
                       my_div(style_up_panel, "",
                              [
                                my_div({"float": "left", "width": "10%"}, "", 
                                       my_div({"margin-left": "15%", "margin-top": "5%"}, f"{id_page}_panel_up_left"),
                                ),
                                my_div({"float": "left", "width": "83%"}, "", 
                                       html.H5("Big Data App", style={"margin-left": "35%", "margin-top": "0.3%"})),
                                my_div({"float": "left", "width": "7%"}, "",
                                       my_div({"margin-top": "6%"}, f"{id_page}_panel_up_right"),
                                )
                              ]),
                       # Middle Panel
                       my_div({"margin-left": "1%", "margin-top": "0.5%", "width": "99%", "height": "92%"}, "",
                              [
                               # Left Panel
                               my_div(style_div_buttons, f"{id_page}_left",
                                      [
                                      # DataFrame panel
                                       create_div_buttons(
                                            style_div_1, "DataFrame",
                                            style_button, buttons,
                                            className="btn btn-outline-primary",
                                            color="#F7FAFA",
                                       ),
                                       # Div for Visualizations panel, Functions panel, Models panel
                                       my_div({"height": "70%"}, f"{id_page}_div_functions",
                                              [
                                               # Visualizations panel
                                               create_div_buttons(
                                                   style_div_2, "Visualizations",
                                                   style_button, visualizations,
                                                   className="btn btn-outline-primary",
                                                   color="#F7FAFA",
                                               ),
                                               # Functions panel
                                               create_div_buttons(
                                                   style_div_2, "Functions",
                                                   style_button, functions,
                                                   className="btn btn-outline-light"
                                               ),
                                               # Models panel
                                               create_div_buttons(
                                                   style_div_2, "Models",
                                                   style_button, models,
                                                   className="btn btn-outline-light"
                                               ),
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
