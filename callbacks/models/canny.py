import base64
import os
import shutil
from tkinter import filedialog

import cv2
from dash import Input, Output, State, callback, html
from dash.exceptions import PreventUpdate


id_page = "canny"


# dropdown fotos
@callback(
    [
        Output(f"{id_page}_drop_foto", "options"),
        Output(f"{id_page}_drop_foto", "value"),
    ],
    Input("canny", "n_clicks"),
    State("main_page_store", "data"),
    prevent_initial_call=True,
)
def button_canny(drop_dir, data):
    list_dir = os.listdir(f"""users/{data["user"]}/fotos""")
    foto = list_dir[0] if len(list_dir) > 0 else ""
    return [list_dir, foto]


# up_foto from local
@callback(
    [
        Output("canny", "n_clicks", allow_duplicate=True),
        Output(f"{id_page}_up_foto", "n_clicks"),
    ],
    Input(f"{id_page}_up_foto", "n_clicks"),
    State("main_page_store", "data"),
    prevent_initial_call=True,
)
def button_up_foto(n_clicks, data):
    if not n_clicks:
        raise PreventUpdate
    try:
        archivo = filedialog.askopenfilename()
        filename = archivo.split("/")[-1]
        shutil.copy(archivo, f"""users/{data["user"]}/fotos/{filename}""")
        return [1, 0]
    except AttributeError as e:
        raise PreventUpdate from e


# content fotos
@callback(
    [
        Output(f"{id_page}_div_result", "children"),
        Output("loading", "children", allow_duplicate=True),
    ],
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
        State("main_page_store", "data"),
    ],
    prevent_initial_call=True,
)
def results(
    accept,
    refresh,
    input_value,
    threshold1,
    threshold2,
    aperture_size,
    l2gradient,
    data,
):
    if accept:
        try:
            if input_value is not None and len(input_value) > 0:
                l2gradient = l2gradient == "True"
                threshold1 = int(threshold1)
                threshold2 = int(threshold2)
                aperture_size = int(aperture_size)

                path = f"""users/{data["user"]}/fotos/{input_value}"""
                img = cv2.imread(path)
                # Redimensionar la imagen (por ejemplo, a 300x300 píxeles)
                resized_img = cv2.resize(img, (300, 300))
                # Codificar la imagen redimensionada en formato JPG y luego en base64
                jpg_img = cv2.imencode(".jpg", resized_img)
                b64_string = base64.b64encode(jpg_img[1]).decode("utf-8")
                # Añadir el prefijo para la representación de datos
                img_data = f"data:image/jpg;base64, {b64_string}"
                # Foto Bordes

                # Canny
                # Convertir la imagen a escala de grises
                gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
                # Aplicar el algoritmo Canny
                edges = cv2.Canny(
                    image=gray,
                    threshold1=threshold1,
                    threshold2=threshold2,
                    apertureSize=aperture_size,
                    L2gradient=l2gradient,
                )
                # Codificar la imagen redimensionada en formato JPG y luego en base64
                jpg_img = cv2.imencode(".jpg", edges)
                b64_string = base64.b64encode(jpg_img[1]).decode("utf-8")
                # Añadir el prefijo para la representación de datos
                bordes = f"data:image/jpg;base64, {b64_string}"
                # Foto Bordes

                load_data_content =  [
                        html.Div(
                            html.Img(
                                id="tag_id",
                                src=img_data,
                                alt="my image",
                                style={"width": "100%"},
                                className="img_class",
                            ),
                            style={"float": "left", "margin-top": "2%",
                                   "width": "45%"},
                        ),
                        html.Div(
                            html.Img(
                                id="tag_id",
                                src=bordes,
                                alt="my image",
                                style={"margin-left": "10%", "width": "100%"},
                                className="img_class",
                            ),
                            style={"float": "left", "margin-top": "2%",
                                   "margin-left": "1%",
                                   "width": "45%"},
                        ),
                    ]
            else:
                load_data_content = html.H6(
                    "No tiene fotos guardadas", style={"color": "#b0d8d3"}
                )
        except Exception as err:
            return err.__str__()
    else:
        raise PreventUpdate
    return [load_data_content, ""]
