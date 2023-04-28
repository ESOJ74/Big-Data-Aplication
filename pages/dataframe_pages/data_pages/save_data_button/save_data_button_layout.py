from dash import dcc

from my_dash.my_dbc.my_button import my_button
from my_dash.my_dcc.my_dropdown import my_dropdown
from my_dash.my_html.my_div import my_div
from pages.dataframe_pages.data_pages.load_data_button.load_data_button_css import *
from pages.dataframe_pages.data_pages.save_data_button.save_data_button_callbacks import *
from pages.dataframe_pages.data_pages.save_data_button.save_data_button_list import \
    list_of_format

id_page = "save_data"

layout = my_div(style_div_main, "",
                [
                 my_div(style_div_dropdown_save, "",
                        [
                         my_div(style_selector, "",
                                my_dropdown(f"{id_page}_dropdown",
                                            {"background": "radial-gradient(circle farthest-side at bottom left, #6da9d8 0%, #204765 50%, #04212c 95%)"},
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
                 my_div(style_div_save_data_content, f"{id_page}_content")
                ]
         )