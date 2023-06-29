import plotly.express as px
from dash import Input, Output, State, callback
from pandas import read_json

from assets.template import list_of_squential, template_visualizations
from utils.selector_options import selector_options
from utils.utils_visualizations import create_result, error

id_page = "strip"

selector_options(id_page, f"{id_page}_X", False)
selector_options(id_page, f"{id_page}_Y", False)
selector_options(id_page, f"{id_page}_color")
selector_options(id_page, f"{id_page}_hover_data")
selector_options(id_page, f"{id_page}_facet_col")


@callback(
    [
        Output(f"{id_page}_content_down", "children"),
        Output("loading", "children", allow_duplicate=True),
        Output(f"{id_page}_refresh", "children"),
        Output(f"{id_page}_refresh", "n_clicks"),
    ],
    [
        Input(f"{id_page}_refresh", "n_clicks"),
        Input(f"{id_page}_X", "value"),
        Input(f"{id_page}_Y", "value"),
        Input(f"{id_page}_stripmode", "value"),
        Input(f"{id_page}_color", "value"),
        Input(f"{id_page}_hover_data", "value"),
        Input(f"{id_page}_facet_col", "value"),
        Input(f"{id_page}_template", "value"),
    ],
    [
        State("main_page_store", "data"),
        State(f"{id_page}_X", "value"),
        State(f"{id_page}_Y", "value"),
        State(f"{id_page}_stripmode", "value"),
        State(f"{id_page}_color", "value"),
        State(f"{id_page}_hover_data", "value"),
        State(f"{id_page}_facet_col", "value"),
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
    click3,
    click4,
    click5,
    click6,
    data,
    state_X,
    state_Y,
    state_stripmode,
    state_color,
    state_hover_data,
    state_facet_col,
    state_template,
    name_button,
):
    if state_color is not None and len(state_color) < 1 or state_color == " ":
        state_color = None
    if (
        state_hover_data is not None
        and len(state_hover_data) < 1
        or state_hover_data == " "
    ):
        state_hover_data = None
    if (
        state_facet_col is not None
        and len(state_facet_col) < 1
        or state_facet_col == " "
    ):
        state_facet_col = None

    new_name_button = "Apply"
    content = ""

    try:
        df = read_json(data["df"])
        fig = px.strip(
            df,
            template=template_visualizations,
            x=state_X,
            y=state_Y,
            hover_data=state_hover_data,
            stripmode=state_stripmode,
            color=state_color,
            facet_col=state_facet_col,
            color_discrete_sequence=list_of_squential[state_template],
        )
        if n_clicks:
            new_name_button, content = create_result(name_button, fig, id_page)
    except Exception as msg:
        content = error(msg)

    return [content, "", new_name_button, 0]