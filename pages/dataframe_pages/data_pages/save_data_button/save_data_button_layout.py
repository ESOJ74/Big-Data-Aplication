from dash import dcc

from assets.my_dash.my_dbc.my_button import my_button
from assets.my_dash.my_dcc.my_dropdown import my_dropdown
from assets.my_dash.my_html.my_div import my_div
from pages.dataframe_pages.data_pages.save_data_button.save_data_button_callbacks import *
from pages.dataframe_pages.data_pages.save_data_button.save_data_button_list import \
    list_of_format

id_page = "save_data"

style_div_dropdown_save = {
    "position": "relative",
    "top": "8.5%",
    "left": "2%",
    "width": "16%",
    "height": "15%",
    "font-family": font_family,
}

style_selector = {        
    "margin-top": "2%",   
    "margin-left": "2%",
    "width": "11vmax",
    "height": "2.7em",
    "border-radius": "7px 7px 5px 5px",
    "padding": "2px 2px 0px 2px",
    "font-size": "1em",
    "color": "black",
    "background": background_dropdown,
}

style_input = {
    "width": "9em",
    "font-size": "1vmax",
    "background": background_light,
    "border": "1px solid #020d11"
}

style_boton_aceptar = {    
    "margin-top": "2%",
    "margin-left": "2%",
    "margin-bottom": "5%",
    "font-size": "75%",
    "font-family": font_family
}

layout = my_div(style_div_main, "",
                [
                 my_div(style_div_dropdown_save, "",
                        [
                         my_div(style_selector, "",
                                my_dropdown(f"{id_page}_dropdown",
                                            {"background": background_in_dropdown},
                                            list_of_format,
                                            value="To CSV",
                                            placeholder="Select format"
                                ),
                         ),
                         my_div({"margin-top": "3%"}, "",
                                dcc.Input(id=f"{id_page}_input",
                                          placeholder="Nombre del archivo",
                                          style=style_input
                                )
                         ),
                         my_div({"margin-top": "3%"}, "",
                             my_button(f"{id_page}_aceptar",
                                       "Aceptar",
                                       style_boton_aceptar,
                                       className="btn btn-outline-warning",
                                       color="black")
                         )
                        ]
                 ),
                 my_div({}, f"{id_page}_content")
                ]
         )