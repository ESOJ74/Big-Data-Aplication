from dash import Input, Output, State, callback, html
from pandas import read_json

id_page = "save_data"


def write_data(df, extension, path):     
    match extension:
        case "csv" | "txt":
            df.to_csv(path + ".csv", index=False)
        case "json":
            df.to_json(path + ".json")
        case "xlsx":
            df.to_excel(path + ".xlsx", index=False) 
        case _:
            pass
     

@callback(Output(f"{id_page}_content", "children"),
          Input(f"{id_page}_aceptar", "n_clicks"),
          [
            State(f"{id_page}_input", "value"),
            State(f"{id_page}_dropdown", "value"),
            State("main_page_store", "data"),
          ],
          prevent_initial_call=True,)
def save_data(n_clicks, input_value, drop_value, data):
    
    load_data_content = html.H6("Introduzca el nombre para el archivo",
                                style={"color": "#b0d8d3"})
    if input_value is not None:
        load_data_content = html.H6("DataFrame Guardado",
                                    style={"color": "#b0d8d3"})
        try:
            df = read_json(data["df"])
            path = f"""users/{data["user"]}/data/{input_value}"""

            match drop_value:
                case "To CSV":
                    write_data(df, "csv", path)
                case "To JSON":
                    write_data(df, "json", path)
                case "To EXCEL":
                    write_data(df, "xlsx", path)
        except (TypeError, KeyError, ValueError):
            load_data_content = html.H6("No hay DataFrame cargado",
                                        style={"color": "#b0d8d3"})
    return load_data_content
