import plotly.express as px
from dash import Input, Output, State, callback
from pandas import read_json

from assets.template import list_of_squential, template_visualizations
from utils.selector_options import selector_options
from utils.utils_visualizations import create_result, error

id_page = "line3d"

selector_options(id_page, f"{id_page}_X", False)
selector_options(id_page, f"{id_page}_Y", False)
selector_options(id_page, f"{id_page}_Z", False)
selector_options(id_page, f"{id_page}_color")
selector_options(id_page, f"{id_page}_symbol")


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
        Input(f"{id_page}_Z", "value"),
        Input(f"{id_page}_color", "value"),
        Input(f"{id_page}_symbol", "value"),
        Input(f"{id_page}_markers", "value"),
        Input(f"{id_page}_log_x", "value"),
        Input(f"{id_page}_log_y", "value"),
        Input(f"{id_page}_log_z", "value"),
        Input(f"{id_page}_template", "value"),
    ],
    [
        State("main_page_store", "data"),
        State(f"{id_page}_X", "value"),
        State(f"{id_page}_Y", "value"),
        State(f"{id_page}_Z", "value"),
        State(f"{id_page}_color", "value"),
        State(f"{id_page}_symbol", "value"),
        State(f"{id_page}_markers", "value"),
        State(f"{id_page}_log_x", "value"),
        State(f"{id_page}_log_y", "value"),
        State(f"{id_page}_log_z", "value"),
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
    click7,
    click8,
    click11,
    data,
    state_X,
    state_Y,
    state_Z,
    state_color,
    state_symbol,
    state_markers,
    state_log_x,
    state_log_y,
    state_log_z,
    state_template,
    name_button,
):
    if state_color is not None and len(state_color) < 1 or state_color == " ":
        state_color = None

    if state_symbol is not None and len(state_symbol) < 1 or state_symbol == " ":
        state_symbol = None

    state_markers = state_markers != "False"
    state_log_x = state_log_x != "False"
    state_log_y = state_log_y != "False"
    state_log_z = state_log_z != "False"

    new_name_button = "Apply"
    content = ""

    try:
        df = read_json(data["df"])
        fig = (
            px.line_3d(
                df,
                x=state_X,
                y=state_Y,
                z=state_Z,
                color=state_color,
                symbol=state_symbol,
                markers=state_markers,
                log_x=state_log_x,
                log_y=state_log_y,
                log_z=state_log_z,
                template=template_visualizations,
                color_discrete_sequence=list_of_squential[state_template],
            )
            .update_layout(
                margin=dict(l=25, r=30, t=35, b=25),
                scene=dict(
                    aspectratio={"x": 0.9, "y": 0.8, "z": 1},
                ),
            )
            .update_traces(
                marker=dict(line=dict(width=0.05, color="Black")),
                selector=dict(mode="markers"),
            )
        )
        if n_clicks:
            new_name_button, content = create_result(name_button, fig, id_page)
    except Exception as msg:
        content = error(msg)

    return [content, "", new_name_button, 0]
