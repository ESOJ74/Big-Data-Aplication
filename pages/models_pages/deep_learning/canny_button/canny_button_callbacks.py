import base64
import os
import shutil
from tkinter import filedialog

import cv2
from dash import Input, Output, State, callback, html
from dash.exceptions import PreventUpdate

from assets.my_dash.my_html.my_div import my_div
from utils.create_callback_button_cover import create_callback_button_cover

from ...common_css import *

id_page = "canny"

create_callback_button_cover(id_page, f"{id_page}_div_result")


@callback(Output(f"{id_page}_content_up", "children"), 
          Input("canny_button", "n_clicks"), 
          prevent_initial_call=True,)
def second_callback(n_clicks):    
    return my_div(style_div_title, "",
                  [
                   html.H5("cv2.Canny()",
                           style=style_title),
                   html.A("Documentacion",
                          href="https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html",
                          target="_blank"),
                   html.A("Git Hub",
                          href="https://github.com/cynicphoenix/Canny-Edge-Detector",
                          target="_blank",
                          style={"margin-left": "3%"})
                  ])


#dropdown fotos
@callback([
           Output(f"{id_page}_drop_foto", "options"),
           Output(f"{id_page}_drop_foto", "value"),
          ],
          Input("canny_button", "n_clicks"),
          State("main_page_store", "data"),
          prevent_initial_call=True)
def load_data(drop_dir, data):    
    foto = ""   
    list_dir = os.listdir(f"""users/{data["user"]}/fotos""")
    if len(list_dir) > 0:
        foto = list_dir[0]   
    return [list_dir, foto]


# content fotos
@callback(Output(f"{id_page}_div_result", "children"), 
          [
           Input(f"{id_page}_drop_foto", "value"),
           Input(f"{id_page}_refresh", "n_clicks"),
          ],
          [
           State(f"{id_page}_drop_foto", "value"), 
           State(f"{id_page}_threshold1", "value"),
           State(f"{id_page}_threshold2", "value"),
           State(f"{id_page}_aperture_size", "value"),
           State(f"{id_page}_L2gradient", "value"),       
           State("main_page_store", "data")
          ],
          prevent_initial_call=True)
def load_data(accept, refresh, input_value, threshold1,
              threshold2, aperture_size, l2gradient, data): 
    
    if accept:
        try:
            if input_value is not None and len(input_value) > 0:

                l2gradient= True if l2gradient == "True" else False
                threshold1 = int(threshold1)
                threshold2 = int(threshold2)
                aperture_size = int(aperture_size)

                path = f"""users/{data["user"]}/fotos/{input_value}"""   
                img = cv2.imread(path)      
                # Convertir la imagen a escala de grises
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                # Aplicar el algoritmo Canny
                edges = cv2.Canny(image=gray, threshold1=threshold1,
                                  threshold2=threshold2, apertureSize=aperture_size,
                                  L2gradient=l2gradient)           
                #cv2.Canny()
                cv2.imwrite('bordes.jpg', edges)                   
                
                # Foto original
                with open(path, "rb") as image_file:
                    img_data = base64.b64encode(image_file.read())
                    img_data = img_data.decode()
                    img_data = "{}{}".format("data:image/jpg;base64, ", img_data)
                # Foto Bordes
                with open('bordes.jpg', "rb") as image_file:
                    bordes = base64.b64encode(image_file.read())
                    bordes = bordes.decode()
                    bordes = "{}{}".format("data:image/jpg;base64, ", bordes)
                os.remove("bordes.jpg")

                load_data_content = my_div({}, "",
                                           [
                                            my_div({"float":"left", 'width': '60vmin'}, "",
                                                   html.Img(id="tag_id", src=img_data,
                                                            alt="my image",
                                                            style={'width': '100%'}, 
                                                            className="img_class")
                                            ),
                                            my_div({"float":"left", "margin-left": "2%",
                                                    'width': '60vmin'}, "",
                                                   html.Img(id="tag_id", src=bordes,
                                                            alt="my image",
                                                            style={"margin-left": "10%",
                                                                   'width': '100%'}, 
                                                           className="img_class")
                                            ),
                                        ]
                                    )   
            else:
                load_data_content = html.H6("No tiene fotos guardadas",
                                            style={"color": "#b0d8d3"}) 
        except Exception as err:
            return err.__str__()
    else:
        raise PreventUpdate   
    return load_data_content


#up_foto from local
@callback([
           Output("canny_button", "n_clicks", allow_duplicate=True),   
           Output(f"{id_page}_up_foto", "n_clicks")
          ], 
          Input(f"{id_page}_up_foto", "n_clicks"),
          State("main_page_store", "data"),
          prevent_initial_call=True)
def load_data(n_clicks, data):    
    if n_clicks:
        try:
            archivo = filedialog.askopenfilename()
            filename = archivo.split('/')[-1]        
            shutil.copy(archivo, f"""users/{data["user"]}/fotos/{filename}""")             
            return [1, 0]
        except AttributeError:
            raise PreventUpdate
    else:
        raise PreventUpdate
