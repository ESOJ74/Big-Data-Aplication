import base64
import os
import shutil
from tkinter import filedialog

import cv2
from dash import Input, Output, State, callback, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from common_functions.create_callback_button_cover import \
    create_callback_button_cover
from my_dash.my_html.my_div import my_div

id_page = "canny"


# botones
@callback([
           Output(f"{id_page}_div_fotos", "hidden"),
           Output(f"{id_page}_fotos", "n_clicks"),
           Output(f"{id_page}_content", "style"),
           Output(f"{id_page}_content", "children", allow_duplicate=True),
          ],
          [
           Input(f"{id_page}_fotos", "n_clicks"),
           Input(f"{id_page}_up_foto", "n_clicks"),
          ],
          prevent_initial_call=True)
def load_data(click_fotos, click_up):    
    hidden_arch = True
    style = {"margin-top": "5%", "margin-left": "15%"}
    style2 = {"margin-top": "7%", "margin-left": "3.5%"}

    if click_fotos:
        hidden_arch = False
        style = style2 
    return [hidden_arch, 0, style, ""]

            
#dropdown fotos
@callback([
           Output(f"{id_page}_drop_foto", "options"),
           Output(f"{id_page}_drop_foto", "value"),
          ],
          Input(f"{id_page}_fotos", "n_clicks"),
          State("main_page_store", "data"),
          prevent_initial_call=True)
def load_data(drop_dir, data):    
    foto = ""   
    list_dir = os.listdir(f"""users/{data["user"]}/fotos""")

    if len(list_dir) > 0:
        foto = list_dir[0]   
    return [list_dir, foto]
         
    
# content fotos
@callback(Output(f"{id_page}_content", "children"), 
          Input(f"{id_page}_aceptar", "n_clicks"),
          [
           State(f"{id_page}_drop_foto", "value"),        
           State("main_page_store", "data")
          ],
          prevent_initial_call=True)
def load_data(accept, input_value, data): 
    
    if accept:
        if input_value is not None and len(input_value) > 0:
            
            path = f"""users/{data["user"]}/fotos/{input_value}"""    
            
            img = cv2.imread(path)      
            # Convertir la imagen a escala de grises
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Aplicar el algoritmo Canny
            edges = cv2.Canny(gray, 100, 200)           
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
                                        my_div({"float":"left", 'width': '32vmax'}, "",
                                               html.Img(id="tag_id", src=img_data, alt="my image", style={'width': '100%'}, 
                                                        className="img_class")
                                        ),
                                        my_div({"float":"left", "margin-left": "2%", 'width': '32vmax'}, "",
                                               html.Img(id="tag_id", src=bordes, alt="my image", style={'width': '100%'}, 
                                                        className="img_class")
                                        ),
                                       ]
                                )   
        else:
            load_data_content = html.H6("No tiene fotos guardadas",
                                        style={"color": "#b0d8d3"}) 
    else:
        raise PreventUpdate   
    return load_data_content


#up_foto from local
@callback(Output(f"{id_page}_content", "children", allow_duplicate=True),      
          Input(f"{id_page}_up_foto", "n_clicks"),
          State("main_page_store", "data"),
          prevent_initial_call=True)
def load_data(n_clicks, data):
    
    archivo = filedialog.askopenfilename()

    if type(archivo) != tuple:
        filename = archivo.split('/')[-1]        
        shutil.copy(archivo, f"""users/{data["user"]}/fotos/{filename}""")    
        msg = html.H6("Archivo subido", 
                      style={"margin-top": "7%", "margin-left": "3vmax",
                             "color": "#b0d8d3"})    
    else:
        msg = ""
    return msg


create_callback_button_cover(id_page)
