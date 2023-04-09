from dash import Input, Output, State, callback
from pandas import read_json

id_page = "save_data"


@callback(Output(f"{id_page}_content", "children"),
          Input(f"{id_page}_aceptar", "n_clicks"),
          [
            State(f"{id_page}_input", "value"),
            State(f"{id_page}_dropdown", "value"),
            State("main_page_store", "data"),
          ],
          prevent_initial_call=True,)
def save_data(n_clicks, input_value, drop_value, data):
    """
    Función que guarda un DataFrame en un archivo local en uno de los
    formatos disponibles.

    Args:
        n_clicks (int): Número de veces que se ha hecho click en el
                        botón "Aceptar".
        file_name (str): Nombre del archivo.
        file_format (str): Formato en el que se desea guardar
                           el DataFrame.
        data (dict): Datos actualizados que se almacenarán en el componente
                     Store de la página principal.

    Returns:
        str: Mensaje indicando si se ha guardado el archivo correctamente
             o si ha ocurrido un error.
    """
    load_data_content = "Introduzca el nombre para el archivo"
    if input_value is not None:
        load_data_content = "DataFrame Guardado"
        try:
            df = read_json(data["df"])
            match drop_value:
                case "To CSV":
                    df.to_csv(f"Data/csv/{input_value}.csv", index=False)
                case "To JSON":
                    pass
        except (TypeError, KeyError):
            load_data_content = "No hay DataFrame cargado"   
    return load_data_content
