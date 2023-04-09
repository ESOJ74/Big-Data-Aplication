import dash_ag_grid as dag
from dash import Input, Output, Patch, State, callback
from pandas import read_json


@callback([
           Output('view_data_content', 'children'),
           Output('add-data-rows', 'disabled'),
          ],
          Input('view_data_button', 'n_clicks'),
          State('main_page_store', 'data'))
def view_data(n_clicks, data):

    """
    Callback que muestra los datos del DataFrame en un objeto AgGrid y
    habilita el botón para añadir filas.

    Args:
        n_clicks (int): Número de clicks en el botón 'Ver datos'.
        data (dict): Datos actualizados que se almacenarán en el
                     componente Store de la página principal.

    Returns:
        list: Lista con el objeto AgGrid y el estado del botón para añadir
              filas. Si no hay ningún DataFrame cargado, devuelve un mensaje
              y el botón se deshabilita.
    """
    obj = []                    #ag-theme-alpine, ag-theme-alpine-dark, ag-theme-balham, ag-theme-balham-dark, ag-theme-material, ag-theme-bootstrap
    try:        
        df = read_json(data["df"])[0:10]
        obj.append(
            dag.AgGrid(
                id="ag-table",
                className="ag-theme-alpine-dark",
                columnDefs=[{"headerName": x, "field": x} for x in df.columns],
                rowData=df.to_dict("records"),
                columnSize="sizeToFit",
                dashGridOptions={"pagination": True},
                defaultColDef=dict(resizable=True,)
            ))
        obj.append(False)
    except (TypeError, KeyError):
        obj = ['No hay ningún DataFrame Cargado', True]
    return obj


@callback(
    [
     Output("ag-table", "rowData"),
     Output('add-data-rows', 'disabled', allow_duplicate=True),
    ],
    Input("add-data-rows", "n_clicks"),
    State('main_page_store', 'data'),
    prevent_initial_call=True,
)
def add_data_to_fig(n_clicks, data):
    """
    Actualiza los datos de la tabla y habilita el botón de añadir filas de datos.
    
    Parámetros:
    -----------
    n_clicks : int
        Número de veces que se ha hecho clic en el botón 'add-data-rows'.
    data : dict
        Datos almacenados en 'main_page_store'.
        
    Retorna:
    --------
    patched_table : Patch
        Nuevos datos de la tabla.
    True : bool
        Deshabilita el botón de añadir filas de datos.
    """
    df = read_json(data["df"])[10:]
    patched_table = Patch()
    patched_table.extend(df.to_dict("records"))
    return [patched_table, True]
