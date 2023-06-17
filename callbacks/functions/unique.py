from dash import Input, Output, State, callback, html
from pandas import read_json

id_page = "unique"


@callback(
    Output(f"{id_page}_content_down", "children"),
    Input("unique", "n_clicks"),
    State("main_page_store", "data"),
    prevent_initial_call=True,
)
def add_data_to_fig(n_clicks, data):
    return html.Pre(read_json(data["df"]).apply(lambda x: len(x.unique())).__str__(),
                    className="panel-funtions-text",)