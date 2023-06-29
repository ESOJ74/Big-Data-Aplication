import plotly.express as px
from dash import Input, Output, State, callback
from pandas import read_json

from assets.template import list_of_squential, template_visualizations
from utils.selector_options import selector_options
from utils.utils_visualizations import create_result, error

id_page = "pie"

selector_options(id_page, f"{id_page}_values", False)
selector_options(id_page, f"{id_page}_names", False)


@callback(
    [
        Output(f"{id_page}_content_down", "children"),
        Output("loading", "children", allow_duplicate=True),
        Output(f"{id_page}_refresh", "children"),
        Output(f"{id_page}_refresh", "n_clicks"),
    ],
    [
        Input(f"{id_page}_refresh", "n_clicks"),
        Input(f"{id_page}_values", "value"),
        Input(f"{id_page}_names", "value"),
        Input(f"{id_page}_template", "value"),
    ],
    [
        State("main_page_store", "data"),
        State(f"{id_page}_values", "value"),
        State(f"{id_page}_names", "value"),
        State(f"{id_page}_template", "value"),
        State(f"{id_page}_refresh", "children"),
    ],
    prevent_initial_call=True,
)
def display_page(
    n_clicks,
    click,
    click1,
    click2,
    data,
    state_X,
    state_Y,
    state_template,
    name_button,
):
    new_name_button = "Apply"
    content = ""

    try:
        df = read_json(data["df"])
        fig = px.pie(
            df,
            template=template_visualizations,
            values=state_X,
            names=state_Y,
            color_discrete_sequence=list_of_squential[state_template],
        )
        fig.update_traces(textposition="inside", textinfo="percent+label")
        if n_clicks:
            new_name_button, content = create_result(name_button, fig, id_page)
    except Exception as msg:
        content = error(msg)

    return [content, "", new_name_button, 0]
