"""
Module Name: <module_name>

<Module Description>

This module contains the callback functions for updating the correlation analysis page
in the application.
The callbacks handle user interactions and update the correlation graph and content
based on the input values.

Functions:
- display_page(pathname): Callback function to display the appropriate page layout based
on the URL pathname.
- second_callback(...): Callback function to update the correlation analysis graph and
content based on user inputs.
"""

import plotly.express as px
from dash import Input, Output, State, callback
from pandas import read_json

from assets.template import list_of_squential
from utils.create_callback_text_graph import create_callback_text_graph
from utils.utils_functions import create_msg, create_obj

ID_PAGE = "corr"

create_callback_text_graph(ID_PAGE)


@callback(
    [
        Output(f"{ID_PAGE}_content_down", "children"),
        Output("loading", "children", allow_duplicate=True),
    ],
    [
        Input(f"{ID_PAGE}_text", "className"),
        Input(f"{ID_PAGE}_graph", "className"),
        Input(f"{ID_PAGE}_refresh", "n_clicks"),
    ],
    [
        State("main_page_store", "data"),
        State(f"{ID_PAGE}_text", "className"),
        State(f"{ID_PAGE}_graph", "className"),
        State(f"{ID_PAGE}_method", "value"),
        State(f"{ID_PAGE}_numeric_only", "value"),
        State(f"{ID_PAGE}_min_periods", "value"),
        State(f"{ID_PAGE}_template", "value"),
    ],
    prevent_initial_call=True,
)
def second_callback(
    click1,
    click2,
    click3,
    data,
    state_text,
    state_graph,
    state_method,
    state_numeric_only,
    state_min_periods,
    state_template,
):
    """
    Callback function to update the correlation analysis graph and content based on user
    inputs.

    Args:
        click1 (int): The number of clicks on the text input component triggering the
        callback.
        click2 (int): The number of clicks on the graph component triggering the
        callback.
        click3 (int): The number of clicks on the refresh button component triggering
        the callback.
        data (dict): The data stored in the "main_page_store" component.
        state_text (str): The className of the text input component.
        state_graph (str): The className of the graph component.
        state_method (str): The selected correlation method.
        state_numeric_only (str): The selected value for numeric_only option.
        state_min_periods (str): The selected value for min_periods option.
        state_template (str): The selected template for the correlation graph.

    Returns:
        list: A list containing the updated children for the content component and an
        empty string.
        The children can include a correlation analysis graph or an error message,
        based on the input values.

    The function is a callback triggered by changes in the input components
    (clicks, states) specified in the decorator.
    It retrieves the necessary input values and performs correlation analysis based on
    the provided data.

    The correlation analysis is performed using the Pandas DataFrame `corr` method with
    the specified options.
    If successful, a correlation heatmap is generated using Plotly Express (`px.imshow`)
    and returned as a figure.

    If any error occurs during the correlation analysis, the function catches the
    `ValueError` exception
    and returns an error message instead of the graph.

    The function returns the updated children for the content component, which can be a
    correlation analysis graph
    or an error message, depending on the success of the correlation analysis.
    An empty string is also returned as the loading component to remove any existing
    loading message.
    """
    try:
        state_min_periods = int(state_min_periods)
        state_numeric_only = state_numeric_only == "True"
        corr = read_json(data["df"]).corr(
            state_method, state_min_periods, state_numeric_only
        )
        fig = px.imshow(
            corr,
            # template=template_visualizations,
            color_continuous_scale=list_of_squential[state_template],
            contrast_rescaling="infer",
            aspect="auto",
        )
        return [create_obj(corr, fig, state_graph), ""]
    except ValueError as msg:
        return [create_msg(msg), ""]
