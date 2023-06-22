import plotly.express as px
from dash import Input, Output, State, callback
from pandas import read_json

from assets.template import list_of_squential, template_visualizations
from utils.selector_options import selector_options
from utils.utils_visualizations import create_result, error

id_page = "ecdf"

selector_options(id_page, f"{id_page}_X", False)
selector_options(id_page, f"{id_page}_Y")
selector_options(id_page, f"{id_page}_color")
selector_options(id_page, f"{id_page}_line_group")


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
        Input(f"{id_page}_color", "value"),
        Input(f"{id_page}_ecdfnorm", "value"),
        Input(f"{id_page}_ecdfmode", "value"),
        Input(f"{id_page}_markers", "value"),
        Input(f"{id_page}_template", "value"),
    ],
    [
        State("main_page_store", "data"),
        State(f"{id_page}_X", "value"),
        State(f"{id_page}_Y", "value"),
        State(f"{id_page}_color", "value"),
        State(f"{id_page}_ecdfnorm", "value"),
        State(f"{id_page}_ecdfmode", "value"),
        State(f"{id_page}_markers", "value"),
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
    state_color,
    state_ecdfnorm,
    state_ecdfmode,
    state_markers,
    state_template,
    name_button,
):
    if state_Y is not None and len(state_Y) < 1 or state_Y == " ":
        state_Y = None
    if state_ecdfnorm is not None and len(state_ecdfnorm) < 1 or state_ecdfnorm == " ":
        state_ecdfnorm = None
    if state_color is not None and len(state_color) < 1 or state_color == " ":
        state_color = None
    state_markers = state_markers != "False"

    new_name_button = "Apply"
    content = ""

    try:
        df = read_json(data["df"])
        fig = px.ecdf(
            df,
            template=template_visualizations,
            x=state_X,
            y=state_Y,
            color=state_color,
            ecdfnorm=state_ecdfnorm,
            ecdfmode=state_ecdfmode,
            markers=state_markers,
            color_discrete_sequence=list_of_squential[state_template],
        )
        if n_clicks:
            new_name_button, content = create_result(name_button, fig, id_page)
    except Exception as msg:
        content = error(msg)

    return [content, "", new_name_button, 0]
