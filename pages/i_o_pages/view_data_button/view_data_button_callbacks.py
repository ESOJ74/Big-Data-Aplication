import dash_ag_grid as dag
from dash import Input, Output, Patch, State, callback, html
from pandas import read_json


@callback([
           Output('view_data_content', 'children'),
           Output('add-data-rows', 'disabled'),
          ],
          Input('view_data_button', 'n_clicks'),
          State('main_page_store', 'data'))
def view_data(n_clicks, data):

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
                defaultColDef=dict(resizable=True,),
            ))
        obj.append(False)
    except (TypeError, KeyError, ValueError):
        obj = [html.H6('No hay ningún DataFrame Cargado'), True]
    return obj


@callback([
           Output("ag-table", "rowData"),
           Output('add-data-rows', 'disabled', allow_duplicate=True),
          ],
          Input("add-data-rows", "n_clicks"),
          State('main_page_store', 'data'),
          prevent_initial_call=True,)
def add_data_to_fig(n_clicks, data):
    
    df = read_json(data["df"])[10:]
    patched_table = Patch()
    patched_table.extend(df.to_dict("records"))
    return [patched_table, True]


@callback(Output("main_page_div_button_cover", "hidden", allow_duplicate=True),
          Input("view_data_content", "children"),
          prevent_initial_call=True)
def display_page(values):
    return False