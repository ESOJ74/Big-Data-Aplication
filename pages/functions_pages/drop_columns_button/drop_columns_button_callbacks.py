from dash import Input, Output, State, callback
from pandas import read_json
from my_dash.my_dcc.my_dropdown import my_dropdown
from my_dash.my_dbc.my_button import my_button
from my_dash.my_html.my_div import my_div

id_page = "drop_columns_function"


@callback(
    [Output(f"{id_page}_div_dropdown", "children")],
    Input("drop_columns_function", "n_clicks"),
    State("store", "data"),
    prevent_initial_call=True,)
def add_data_to_fig(n_clicks, data):
    try:
        columns = read_json(data["df"]).columns
        content = my_dropdown(f"{id_page}_dropdown", {"width": "50%"},
                              options=columns, placeholder="Select Columns"),
    except (TypeError, KeyError):        
        content = "No hay ningún DataFrame Cargado"
    return [content]


@callback(
    [Output(f"{id_page}_content", "children", allow_duplicate=True),
     Output("store", "data", allow_duplicate=True),],
    Input(f"{id_page}_dropdown", "value"),
    State("store", "data"),
    prevent_initial_call=True,)
def add_data_to_fig(value, data):

    try:
        df = read_json(data["df"])
        data["df"] = df.to_json(orient="columns")
    except (TypeError, KeyError):
        data = {}

    obj = ""

    if len(value) > 0:
        df = df.drop([f"{value}"], axis=1)
        data["prov_df"] = df.to_json(orient="columns")
        obj = [f"df.drop([{value}], axis=1)",
               my_div({"margin-top": "1%"}, "",
                      [
                        my_button(f"{id_page}_accept",
                                  "Accept", {"float": "left"}),
                        my_button(f"{id_page}_cancel",
                                  "Cancel", {"float": "left"})
                      ])]
    return [obj, data]


@callback(
    [Output(f"{id_page}_content", "children", allow_duplicate=True),
     Output("store", "data", allow_duplicate=True),
     Output(f"{id_page}_accept", "n_clicks"),
     Output(f"{id_page}_cancel", "n_clicks"),],
    [Input(f"{id_page}_accept", "n_clicks"),
     Input(f"{id_page}_cancel", "n_clicks"),],
    [State("store", "data"),
     State(f"{id_page}_content", "children")],
    prevent_initial_call=True,)
def add_data_to_fig(accept, cancel, data, content):

    if accept:
        df = read_json(data["prov_df"])
        data["df"] = df.to_json(orient="columns")
        content = "The column has been dropped"
    if cancel:
        df = read_json(data["df"])
        data["df"] = df.to_json(orient="columns")
        content = "The operation has been canceled"
    return [content, data, 0, 0]
