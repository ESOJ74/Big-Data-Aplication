from dash import Input, Output, callback


def create_callback_text_graph(id_page):
    @callback(
        [
            Output(f"{id_page}_text", "className"),
            Output(f"{id_page}_graph", "className"),
            Output(f"{id_page}_text", "n_clicks"),
            Output(f"{id_page}_graph", "n_clicks"),
        ],
        [
            Input(f"{id_page}_text", "n_clicks"),
            Input(f"{id_page}_graph", "n_clicks"),
        ],
        prevent_initial_call=True,
    )
    def first_callback(n_clicks_text, n_click_graph):
        button_text = "btn-on"
        button_graph = "btn-text"
        if n_click_graph:
            button_text = "btn-text"
            button_graph = "btn-on"
        return [button_text, button_graph, 0, 0]
