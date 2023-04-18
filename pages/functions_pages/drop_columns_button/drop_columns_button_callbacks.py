import dash_ag_grid as dag
from dash import Input, Output, State, callback, html
from dash.exceptions import PreventUpdate
from pandas import read_json

from my_dash.my_dbc.my_button import my_button
from my_dash.my_dcc.my_dropdown import my_dropdown
from my_dash.my_html.my_div import my_div
from pages.functions_pages.drop_columns_button.drop_columns_button_css import *

id_page = "drop_columns"


@callback(
    Output(f"{id_page}_div_dropdown", "children"),
    Input("drop_columns_button", "n_clicks"),
    State("main_page_store", "data"),
    prevent_initial_call=True,)
def add_data_to_fig(n_clicks, data):    
    columns = read_json(data["df"]).columns
    return my_div(s_selector, "",
                  my_dropdown(f"{id_page}_dropdown",
                              {},
                              columns,
                              value = columns[0],
                              placeholder="Seleccione columna"),)    


@callback(
    Output(f"{id_page}_content", "children", allow_duplicate=True),    
    Input(f"{id_page}_dropdown", "value"),
    State("main_page_store", "data"),
    prevent_initial_call=True,)
def add_data_to_fig(value, data):   
    return [html.H6(f"df.drop([{value}], axis=1)"),
            my_div({"margin-top": "1%"}, "",                  
                   my_button(f"{id_page}_accept",
                             "Accept", {"float": "left"},
                             color="black"
                   ),)]     


@callback(
    [
      Output(f"{id_page}_content", "children", allow_duplicate=True),
      Output("main_page_store", "data", allow_duplicate=True),
      Output(f"{id_page}_accept", "n_clicks"),
    ],
    Input(f"{id_page}_accept", "n_clicks"),
    [      
      State(f"{id_page}_dropdown", "value"),
      State("main_page_store", "data"),
    ],
    prevent_initial_call=True,)
def add_data_to_fig(accept, value, data):     
    if accept:        
        df = read_json(data["df"]).drop([f"{value}"], axis=1)  
        data["prov_df"] = df.to_json(orient="columns")
        content = [html.H6("The column has been dropped"),
                   dag.AgGrid(
                       id=f"{id_page}_ag-table",
                       className="ag-theme-alpine-dark",
                       columnDefs=[{"headerName": x, "field": x}
                                   for x in df.columns],
                       rowData=df.to_dict("records"),
                       columnSize="sizeToFit",
                       dashGridOptions={"pagination": True},
                       defaultColDef=dict(resizable=True,)
                   ),
                   my_div({"margin-top": "1%"}, "",                  
                          my_button(f"{id_page}_save",
                                   "Save", {},
                                   color="black"
                          ),
                   )]
    else:
        raise PreventUpdate
    return [content, data, 0]


@callback(
    [
      Output(f"{id_page}_dropdown", "options", allow_duplicate=True),
      Output(f"{id_page}_dropdown", "value", allow_duplicate=True),
      Output("main_page_store", "data", allow_duplicate=True),
      Output(f"{id_page}_save", "n_clicks"),
    ],
    Input(f"{id_page}_save", "n_clicks"),
    State("main_page_store", "data"),
    prevent_initial_call=True,)
def save_button(save, data):
    if save:
        df = read_json(data["prov_df"])
        data["df"] = df.to_json(orient="columns")
        columns = list(df.columns)
    else:
        raise PreventUpdate
    return [columns, columns[0], data, 0]
    