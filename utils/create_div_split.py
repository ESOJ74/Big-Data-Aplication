import dash_bootstrap_components as dbc
from dash import dcc, html

style_div_input_split = {
    "float": "left",
    "margin-left": "3%",
    "margin-top": "0.5%",
    "height": "45%",
}

style_params_split = {
    "float": "left",
    "color": "white",
    "font-size": "0.9em",
    "font-family": "var(--bs-body-font-family)",
}

style_input_split = {
    "float": "left",
    "margin-left": "2%",
    "width": "12%",
    "font-size": "0.8em",
    "text-align": "right",
    "color": "black",
}

style_div_button_start = {
    "margin-left": "5%",
    "margin-top": "2%",
    "width": "25%",
    "height": "20%",
}


def create_div(id_page, title, id_input, value=None):
    return html.Div(
        [
            html.Div(title, style=style_params_split),
            dcc.Input(
                id=id_input,
                style=style_input_split,
                value=value,
            ),
        ],
        style=style_div_input_split,
    )


def create_div_split(id_page):
    return html.Div(
        [
            html.Div(
                "train_test_split",
                className="title-split",
            ),
            html.Div(
                [
                    create_div(id_page, "test_size", f"{id_page}_test_size", 20),
                    create_div(
                        id_page, "random_state", f"{id_page}_random_state_split", 42
                    ),
                ],
                className="panel-creates",
            ),
            html.Div(
                dbc.Button(
                    "Start Training",
                    f"{id_page}_button_start",
                    class_name="btn-start",
                ),
                style=style_div_button_start,
            ),
        ],
        f"{id_page}_div_split",
        className="panel-split",
    )
