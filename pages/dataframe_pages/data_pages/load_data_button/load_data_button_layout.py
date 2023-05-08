from assets.layout_templates.main_page.content_layout import *

from .load_data_button_callbacks import *

id_page = "load_data"

content_up = my_div(
    style_div_content_up,
    f"{id_page}_content_up",
    my_div(
        style_div_titles,
        "",
        [
            my_button(
                f"{id_page}_archivos",
                "Archivos",
                style_boton_files,
                className="btn btn-outline-primary",
                color="black",
            ),
            my_div(
                style_div_up_load,
                "",
                [
                    dcc.Upload(
                        id="upload-data",
                        children=html.Div(
                            ["Drag and Drop or ", html.A("Select Files")]
                        ),
                        style=style_dcc_upload,
                        # Allow multiple files to be uploaded
                        multiple=True,
                    ),
                ],
            ),
            my_button(
                f"{id_page}_database",
                "Up File from DataBase",
                style_boton_files,
                className="btn btn-outline-primary",
                color="black",
            ),
            html.A(
                "Documentacion",
                href="https://pandas.pydata.org/docs/reference/io.html",
                style=style_A,
                target="_blank",
            ),
        ],
    ),
)


layout = create_content_layout(
    id_page,
    content_up,
    my_div(style_div_content_down, f"{id_page}_content_down"),
    my_div(style_div_params, ""),
)


"""style={
            "float": "left", 
    "margin-left": "1%",
    "width": "20%",
    "height": "10%",
    "font-size": "0.9vmax",
    "border": "2px solid",
    "font-family": font_family,
    "color": color_boton_1,            
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',            
        },"""
