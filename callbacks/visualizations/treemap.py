import plotly.express as px
from dash import Input, Output, State, callback

from assets.template import list_of_squential
from utils.utils_visualizations import create_result, error

id_page = "treemap"


@callback(
    [
        Output(f"{id_page}_content_down", "children"),
        Output("loading", "children", allow_duplicate=True),
        Output(f"{id_page}_refresh", "children"),
        Output(f"{id_page}_refresh", "n_clicks"),
    ],
    [
        Input(f"{id_page}_refresh", "n_clicks"),
        Input(f"{id_page}_template", "value"),
    ],
    [
        State("main_page_store", "data"),
        State(f"{id_page}_template", "value"),
        State(f"{id_page}_refresh", "children"),
    ],
    prevent_initial_call=True,
)
def display_page(n_clicks, click, data, state_template, name_button):
    new_name_button = "Apply"
    content = ""

    try:
        fig = px.treemap(
            names=[
                "Eve",
                "Cain",
                "Seth",
                "Enos",
                "Noam",
                "Abel",
                "Awan",
                "Enoch",
                "Azura",
            ],
            parents=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"],
            color_discrete_sequence=list_of_squential[state_template],
            color_continuous_scale=list_of_squential[state_template],
        )
        fig.update_traces(root_color="lightgrey")
        if n_clicks:
            new_name_button, content = create_result(name_button, fig, id_page)
    except Exception as msg:
        content = error(msg)

    return [content, "", new_name_button, 0]
