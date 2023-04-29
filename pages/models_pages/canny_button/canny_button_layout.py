from assets.my_dash.my_dbc.my_button import my_button
from assets.my_dash.my_dcc.my_dropdown import my_dropdown
from assets.my_dash.my_html.my_div import my_div
from pages.models_pages.canny_button.canny_button_callbacks import *
from pages.models_pages.canny_button.canny_button_css import *

id_page = "canny"

layout = my_div(style_div_main, "",
                [my_div(style_div_titles, "",                        
                        [
                         my_button(f"{id_page}_fotos", "Fotos",
                                   style_boton_files,
                                   className="btn btn-outline-primary",
                                   color="black"
                         ),   
                         my_button(f"{id_page}_up_foto", "Up Foto from Local",
                                   style_boton_files,
                                   className="btn btn-outline-primary",
                                   color="black"
                         ),                         
                        ]
                 ),
                 my_div(style_div_dropdown_archivos, f"{id_page}_div_fotos",
                        [
                         my_div(style_selector, "",
                                my_dropdown(f"{id_page}_drop_foto", {}),
                         ),
                         my_button(f"{id_page}_aceptar", "Aceptar",
                                   style_boton_aceptar,
                                   className="btn btn-outline-warning",
                                   color="black"),    
                        ], hidden=True,
                 ),    
                 my_div({"margin-top": "10%", "width": "100%", "height": "60%"},
                        f"{id_page}_content")
                ]
         )
