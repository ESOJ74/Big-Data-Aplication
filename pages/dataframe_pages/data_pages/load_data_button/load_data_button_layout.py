
from assets.layout_templates.main_page.content_layout import *


from .load_data_button_callbacks import *


id_page = "load_data"

content_up = my_div(style_div_content_up,
                    f"{id_page}_content_up",
                    my_div(style_div_titles, "",                        
                           [
                            my_button(f"{id_page}_archivos",
                                      "Archivos",
                                      style_boton_files,
                                      className="btn btn-outline-primary",
                                      color="black"
                            ),   
                            my_button(f"{id_page}_up_file",
                                      "Up File from Local",
                                      style_boton_files,
                                      className="btn btn-outline-primary",
                                      color="black"
                            ),       
                            my_button(f"{id_page}_database",
                                      "Up File from DataBase",
                                      style_boton_files,
                                      className="btn btn-outline-primary",
                                      color="black"
                            ),  
                            html.A("Documentacion",
                                   href="https://pandas.pydata.org/docs/reference/io.html",
                                   style=style_A,
                                   target="_blank"),
                           ]))


layout = create_content_layout(id_page,
                               content_up,
                               my_div(style_div_content_down,
                                      f"{id_page}_content_down"),
                               my_div(style_div_params, ""))


