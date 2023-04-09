from dash import Input, Output, State, callback
from pandas import read_csv, read_json

id_page = "load_data"


from dash.dependencies import Input, Output, State
from pandas import read_csv

@callback(
    [
        Output("main_page_store", "data"),
        Output(f"{id_page}_content", "children"),
        Output(f"main_page_div_functions", "hidden")
    ],
    [
        Input(f"{id_page}_aceptar", "n_clicks")
    ],
    [
        State(f"{id_page}_input", "value"),
        State("load_data_dropdown", "value"),
        State("main_page_store", "data")
    ],
    prevent_initial_call=True
)
def load_data(n_clicks, input_value, drop_value, data):

    """
    Callback que se encarga de cargar los datos del archivo seleccionado
    por el usuario en la página 'Load Data'. 

    Parámetros:
    -----------
    n_clicks: int
        Número de veces que se ha hecho clic en el botón de 'Aceptar'.
    input_value: str
        Ruta del archivo seleccionado por el usuario.
    drop_value: str
        Valor seleccionado en el dropdown que indica el formato
        del archivo (CSV, JSON).
    data: dict
        Datos almacenados en el componente Store de la página principal.

    Devuelve:
    ---------
    list
        Lista con los siguientes elementos:
        - data: dict
            Datos actualizados que se almacenarán en el componente Store
            de la página principal.
        - load_data_content: str
            Mensaje que se mostrará en la sección de carga de datos indicando
            el resultado de la operación.
        - hidden: bool
            Indicador de si se mostrará o no la sección de funciones de
            la página principal.
    """
    data = {}
    load_data_content = ""
    hidden = True
    if input_value is not None:
        path = input_value
        if drop_value == "From CSV":
            try:
                df = read_csv(path)
                data["df"] = df.to_json(orient="columns")
                load_data_content = "DataFrame Cargado"
                hidden = False
            except FileNotFoundError:
                load_data_content = f"No such file or directory: {input_value}"
        elif drop_value == "From JSON":
            load_data_content = "Función no implementada"
    return [data, load_data_content, hidden]
