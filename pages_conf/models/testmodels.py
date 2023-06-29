from dash import dcc, html

from callbacks.models.testmodels import *  # noqa: F403

id_page = "test_models"


content_down = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            "Model Type",
                            className="panel-title-test-models",
                        ),
                        dcc.Dropdown(
                            id=f"{id_page}_test_left",
                            className="select_dropdown",
                        ),
                    ],
                    className="panel-test-model",
                ),
                html.Div(
                    [
                        html.Div(
                            "Model",
                            className="panel-title-test-models",
                        ),
                        html.Div(
                            dcc.Dropdown(
                                id=f"{id_page}_test_right",
                                className="select_dropdown",
                            ),
                        ),
                    ],
                    className="panel-test-model2",
                ),
            ],
            style={"margin-top": "2%", "height": "15%"},
        ),
        html.Div(
            id=f"{id_page}_div_result",
            style={"margin-top": "0%", "height": "80%"},
        ),
    ],
    f"{id_page}_div_test_left",
    style={"margin-left": "2%", "height": "95%", "width": "100%"},
)
content_up = None
params = [html.Div("", f"{id_page}_div_params", className="no-params")]
