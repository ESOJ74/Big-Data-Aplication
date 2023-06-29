from importlib import import_module

import dash_bootstrap_components as dbc
from dash import callback, html
from dash.dependencies import Input, Output, State
from dash_iconify import DashIconify

from buttons_conf import list_of_buttons, no_apply
from dependencies.classes.template_creator import TemplateCreator

id_page = "main_page"


# ------------------- panel up -----------------------------
@callback(
    [
        Output(f"{id_page}_panel_up_left", "children"),
        Output(f"{id_page}_panel_up_right", "children"),
        Output(f"{id_page}_store", "data"),
    ],
    Input("initial_layout_url", "pathname"),
)
def update_panel_up(pathname):
    with open("user.txt", "r") as file:
        user = file.read()
    return [
        f"Usuario: {user}",
        html.A("Cerrar Sesión", href="/", className="close-sesion"),
        {"user": user},
    ]


# --------------------- middle panel ---------------------------
# button cover
@callback(
    [
        Output(f"{id_page}_button_cover", "children"),
        Output(f"{id_page}_panel_middle_left", "className"),
        Output(f"{id_page}_panel_middle_right", "className"),
    ],
    Input(f"{id_page}_button_cover", "n_clicks"),
    prevent_initial_call=True,
)
def button_cover(n_clicks):
    if n_clicks % 2 != 0:
        return [
            DashIconify(icon="ic:baseline-arrow-circle-right", className="icon-cover"),
            "panel-middle-left-cover",
            "panel-middle-right-cover",
        ]
    else:
        return [
            DashIconify(icon="ic:baseline-arrow-circle-left", className="icon-cover"),
            "panel-middle-left",
            "panel-middle-right",
        ]


# button data
@callback(
    [
        Output(f"{id_page}_panel_load_save", "hidden"),
    ],
    Input(f"{id_page}_button_data", "n_clicks"),
    State(f"{id_page}_panel_load_save", "hidden"),
    prevent_initial_call=True,
)
def button_data(n_clicks, panel_hidden):
    return [not panel_hidden]


# button save
@callback(
    [
        Output(f"{id_page}_save_data", "n_clicks"),
    ],
    Input(f"{id_page}save_data", "n_clicks"),
    prevent_initial_call=True,
)
def button_save(n_clicks):
    print(n_clicks)
    return [n_clicks]


# buttons
@callback(
    [
        Output(f"{id_page}_div_functions", "hidden"),
        Output(f"{id_page}_div_visualizations", "hidden"),
        Output(f"{id_page}_div_models", "hidden"),
        Output(f"{id_page}_div_workFlow", "hidden"),
        Output(f"{id_page}_button_show_functions", "n_clicks"),
        Output(f"{id_page}_button_show_visualizations", "n_clicks"),
        Output(f"{id_page}_button_show_models", "n_clicks"),
        Output(f"{id_page}_button_show_workflow", "n_clicks"),
    ],
    [
        Input(f"{id_page}_button_show_functions", "n_clicks"),
        Input(f"{id_page}_button_show_visualizations", "n_clicks"),
        Input(f"{id_page}_button_show_models", "n_clicks"),
        Input(f"{id_page}_button_show_workflow", "n_clicks"),
    ],
    [
        State(f"{id_page}_div_functions", "hidden"),
        State(f"{id_page}_div_visualizations", "hidden"),
        State(f"{id_page}_div_models", "hidden"),
        State(f"{id_page}_div_workFlow", "hidden"),
    ],
    prevent_initial_call=True,
)
def drop_buttons(
    c_funtions,
    c_visualizations,
    c_models,
    c_workflow,
    s_funtions,
    s_visualizations,
    s_models,
    s_workflow,
):
    if c_funtions:
        s_funtions = not s_funtions
    if c_visualizations:
        s_visualizations = not s_visualizations
    if c_models:
        s_models = not s_models
    if c_workflow:
        s_workflow = not s_workflow
    return [s_funtions, s_visualizations, s_models, s_workflow, 0, 0, 0, 0]


@callback(
    [
        Output(f"{id_page}_div_info", "hidden"),
        Output(f"{id_page}_div_a_g", "hidden"),
        Output(f"{id_page}_div_h_p", "hidden"),
        Output(f"{id_page}_div_q_z", "hidden"),
        Output(f"{id_page}_div_basic", "hidden"),
        Output(f"{id_page}_div_part_of_whole", "hidden"),
        Output(f"{id_page}_div_one_d", "hidden"),
        Output(f"{id_page}_div_two_d", "hidden"),
        Output(f"{id_page}_div_three_d", "hidden"),
        Output(f"{id_page}_div_supervised", "hidden"),
        Output(f"{id_page}_div_deep_learning", "hidden"),
        Output(f"{id_page}_div_existing_models", "hidden"),
        Output(f"{id_page}_button_info", "n_clicks"),
        Output(f"{id_page}_button_a_g", "n_clicks"),
        Output(f"{id_page}_button_h_p", "n_clicks"),
        Output(f"{id_page}_button_q_z", "n_clicks"),
        Output(f"{id_page}_button_basic", "n_clicks"),
        Output(f"{id_page}_button_part_of_whole", "n_clicks"),
        Output(f"{id_page}_button_one_d", "n_clicks"),
        Output(f"{id_page}_button_two_d", "n_clicks"),
        Output(f"{id_page}_button_three_d", "n_clicks"),
        Output(f"{id_page}_button_supervised", "n_clicks"),
        Output(f"{id_page}_button_deep_learning", "n_clicks"),
        Output(f"{id_page}_button_existing_models", "n_clicks"),
    ],
    [
        Input(f"{id_page}_button_info", "n_clicks"),
        Input(f"{id_page}_button_a_g", "n_clicks"),
        Input(f"{id_page}_button_h_p", "n_clicks"),
        Input(f"{id_page}_button_q_z", "n_clicks"),
        Input(f"{id_page}_button_basic", "n_clicks"),
        Input(f"{id_page}_button_part_of_whole", "n_clicks"),
        Input(f"{id_page}_button_one_d", "n_clicks"),
        Input(f"{id_page}_button_two_d", "n_clicks"),
        Input(f"{id_page}_button_three_d", "n_clicks"),
        Input(f"{id_page}_button_supervised", "n_clicks"),
        Input(f"{id_page}_button_deep_learning", "n_clicks"),
        Input(f"{id_page}_button_existing_models", "n_clicks"),
    ],
    [
        State(f"{id_page}_div_info", "hidden"),
        State(f"{id_page}_div_a_g", "hidden"),
        State(f"{id_page}_div_h_p", "hidden"),
        State(f"{id_page}_div_q_z", "hidden"),
        State(f"{id_page}_div_basic", "hidden"),
        State(f"{id_page}_div_part_of_whole", "hidden"),
        State(f"{id_page}_div_one_d", "hidden"),
        State(f"{id_page}_div_two_d", "hidden"),
        State(f"{id_page}_div_three_d", "hidden"),
        State(f"{id_page}_div_supervised", "hidden"),
        State(f"{id_page}_div_deep_learning", "hidden"),
        State(f"{id_page}_div_existing_models", "hidden"),
    ],
    prevent_initial_call=True,
)
def buttons(
    c_info,
    c_a_g,
    c_h_p,
    c_q_z,
    c_basic,
    c_part_of_whole,
    c_one_d,
    c_two_d,
    c_three_d,
    c_supervised,
    c_deep_learning,
    c_existing_models,
    s_info,
    s_a_g,
    s_h_p,
    s_q_z,
    s_basic,
    s_part_of_whole,
    s_one_d,
    s_two_d,
    s_three_d,
    s_supervised,
    s_deep_learning,
    s_existing_models,
):
    if c_info:
        s_info = not s_info
    if c_a_g:
        s_a_g = not s_a_g
    if c_h_p:
        s_h_p = not s_h_p
    if c_q_z:
        s_q_z = not s_q_z
    if c_basic:
        s_basic = not s_basic
    if c_part_of_whole:
        s_part_of_whole = not s_part_of_whole
    if c_one_d:
        s_one_d = not s_one_d
    if c_two_d:
        s_two_d = not s_two_d
    if c_three_d:
        s_three_d = not s_three_d
    if c_supervised:
        s_supervised = not s_supervised
    if c_deep_learning:
        s_deep_learning = not s_deep_learning
    if c_existing_models:
        s_existing_models = not s_existing_models
    return [
        s_info,
        s_a_g,
        s_h_p,
        s_q_z,
        s_basic,
        s_part_of_whole,
        s_one_d,
        s_two_d,
        s_three_d,
        s_supervised,
        s_deep_learning,
        s_existing_models,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ]


def create_callback_for_buttons(button):
    list_of_buttons[0]
    buttons_for_functions = list_of_buttons[1]
    buttons_for_visualizations = list_of_buttons[2]
    buttons_for_models = list_of_buttons[3]

    @callback(
        [
            Output(f"{id_page}_panel_middle_right", "children", allow_duplicate=True),
            Output(button, "n_clicks"),
        ],
        Input(button, "n_clicks"),
        prevent_initial_call=True,
    )
    def display_page(n_click):
        if button in buttons_for_functions:
            module = import_module(f"pages_conf.functions.{button}")
        elif button in buttons_for_visualizations:
            module = import_module(f"pages_conf.visualizations.{button}")
        elif button in buttons_for_models:
            module = import_module(f"pages_conf.models.{button}")
        else:
            module = import_module(f"pages_conf.{button}")
        params = module.params
        if button not in no_apply and len(params) > 0:
            params = params + [
                dbc.Button(
                    "Apply",
                    f"{button}_refresh",
                    className="btn-apply",
                )
            ]

        pan = TemplateCreator(button)
        pan.create_content_up(module.content_up, "panel-content-up")
        pan.create_content_down(module.content_down, "panel-content-down")
        pan.create_params(params, "panel-params")
        return [pan.create_template(), 0]


for button in (
    list_of_buttons[0] + list_of_buttons[1] + list_of_buttons[2] + list_of_buttons[3]
):
    create_callback_for_buttons(button)
