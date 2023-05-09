from dash import dcc

from assets.my_dash.my_dbc.my_button import my_button
from assets.my_dash.my_dcc.my_dropdown import my_dropdown
from assets.my_dash.my_html.my_div import my_div
from pages.dataframe_pages.data_pages.save_data_button.save_data_button_callbacks import *
from pages.dataframe_pages.data_pages.save_data_button.save_data_button_css import *

id_page = "save_data"


layout = my_div(
    style_div_main,
    "",
    [
        my_div(
            style_div_dropdown_save,
            "",
            [
                my_div(
                    style_selector,
                    "",
                    my_dropdown(
                        f"{id_page}_dropdown",
                        {"background": background_in_dropdown},
                        list_of_format,
                        value="To CSV",
                        placeholder="Select format",
                    ),
                ),
                my_div(
                    {"margin-top": "3%"},
                    "",
                    dcc.Input(
                        id=f"{id_page}_input",
                        placeholder="Nombre del archivo",
                        style=style_input,
                    ),
                ),
                my_div(
                    {"margin-top": "3%"},
                    "",
                    my_button(
                        f"{id_page}_aceptar",
                        "Aceptar",
                        style_boton_aceptar,
                        className="btn btn-outline-warning",
                        color="black",
                    ),
                ),
            ],
        ),
        my_div({}, f"{id_page}_content"),
    ],
)
