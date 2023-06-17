import plotly.figure_factory as ff

from dash import Input, Output, State, callback
from pandas import read_json

from assets.template import list_of_squential, template_visualizations
from utils.selector_options import selector_options
from utils.utils_visualizations import create_result, error

id_page = "timeline"

selector_options(id_page, f"{id_page}_index_col")


@callback(
    [
        Output(f"{id_page}_content_down", "children"),
        Output("loading", "children", allow_duplicate=True),
        Output(f"{id_page}_refresh", "children"),
        Output(f"{id_page}_refresh", "n_clicks"),
    ],
    [
        Input(f"{id_page}_refresh", "n_clicks"),
        Input(f"{id_page}_index_col", "value"),
        Input(f"{id_page}_show_colorbar", "value"),
        Input(f"{id_page}_group_tasks", "value"),
        Input(f"{id_page}_template", "value"),
    ],
    [
        State("main_page_store", "data"),
        State(f"{id_page}_index_col", "value"),
        State(f"{id_page}_show_colorbar", "value"),
        State(f"{id_page}_group_tasks", "value"),
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
    data,
    state_index_col,
    state_show_colorbar,
    state_group_tasks,
    state_template,
    name_button,
):
    if state_show_colorbar == "True":
        state_show_colorbar = True
    else:
        state_show_colorbar = False

    if state_group_tasks == "True":
        state_group_tasks = True
    else:
        state_group_tasks = False
    new_name_button = "Apply"
    content = ""
    try:
        df = read_json(data["df"])
        fig = ff.create_gantt(
            df,
            colors={},
            index_col=state_index_col,
            show_colorbar=state_show_colorbar,
            group_tasks=state_group_tasks,
        )
        if n_clicks:
            new_name_button, content = create_result(name_button, fig, id_page)
    except Exception as msg:
        content = error(msg)

    return [content, "", new_name_button, 0]
