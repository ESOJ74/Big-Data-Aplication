from dash import Input, Output, State, callback, dash_table
from pandas import read_json
from my_dash.my_dcc.my_dropdown import my_dropdown
from my_dash.my_dbc.my_button import my_button
from my_dash.my_html.my_div import my_div
import dash_ag_grid as dag

id_page = "groupby_function"


@callback(
    [Output("dd", "children")],
    Input("groupby_function", "n_clicks"),
    State("store", "data"),
    prevent_initial_call=True,)
def add_data_to_fig(n_clicks, data):
    
    try:
        columns = read_json(data["df"]).columns        
        content = my_dropdown(f"{id_page}_dropdown", {"width": "50%"}, options=columns, placeholder="Select Columns", multi=True),
    except (TypeError, KeyError) as e:        
        content = "No hay ningún DataFrame Cargado"   
    return [content]


def create_data_table(df):
    """Create Dash datatable from Pandas DataFrame."""
    table = dash_table.DataTable(         #{‘dict’, ‘list’, ‘series’, ‘split’, ‘records’, ‘index’}
        id='database-table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        style_cell={'textAlign': 'center'},
        page_size=300
    )
    return table

@callback(
    Output(f"{id_page}_content", "children"),
    Input(f"{id_page}_dropdown", "value"),
    State("store", "data"),
    prevent_initial_call=True,)
def add_data_to_fig(value, data):
    content = ""
    try:
        df = read_json(data["df"])        
        df = df.groupby(value).mean().reset_index()
        
        content = [f"df.groupby({value}).mean()",
                   create_data_table(df)]
    except TypeError as e:
        content = str(e)
    except KeyError:
        pass

    return content
"""try:
        df = read_json(data["df"])        
        df = df.groupby(['Localización']).mean()
    except TypeError as e:
        content = str(e)"""