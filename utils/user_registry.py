from dash import dcc, html

from assets.layout_templates.main_page.common_css import *
from assets.my_dash.my_dbc.my_button import my_button
from assets.my_dash.my_html.my_div import my_div

style_div_login = {
    "position": "absolute",
    "top": "25%",
    "left": "40%",
    "width": "30%",
    "height": "10%"
}

style_div_input = {
    "margin-top": "6%",
    "width": "40%",
    "font-family": font_family,
}

style_button = {
    "margin-top": "1%",
    "margin-left": "7%",
    "width": "6em",
    "height": "35%",
    "font-size": "0.8vmax",
    "padding": "2px",
    "font-family": font_family,
    "color": color_boton_1,
    "border": "1.5px solid",
}

style_div_reg_answer = {
    "margin-top": "2%",
    "margin-left": "5%",
    "font-family": font_family,
}

style_div_register = {"margin-top": "3%", "width": "100%"}

style_div_answer = {
    "float": "left",
    "font-size": "0.9vmax",
    "color": color_boton_1,
}

style_div_A = {
    "float": "left",
    "margin-left": "2%",
    "width": "60%",
    "font-size": "0.9vmax",
}

style_input = {
    "width": "10em",
    "font-size": "1vmax",
    "background": background_light,
    "border": "1px solid #020d11",
    "color": "black",
}

style_div_page_registry = {
    "position": "absolute",
    "top": "0%",
    "left": "0%",
    "width": "100%",
    "height": "100%",
    "background": background_dark,
}


def insert_user(id_page):
    return my_div(
        style_div_input,
        "",
        [
            my_div(
                {"width": "10em"},
                "",
                dcc.Input(
                    id=f"{id_page}_reg_user",
                    placeholder="Usuario",
                    style=style_input,
                ),
            ),
            my_div(
                {"width": "10em"},
                "",
                dcc.Input(
                    id=f"{id_page}_reg_pass",
                    placeholder="Contraseña",
                    style=style_input,
                ),
            ),
        ],
    )


def user_login(id_page):
    return my_div(
        style_div_login,
        f"{id_page}_div_registry",
        [
            my_div(
                {"color": color_boton_1,},
                "",
                html.H2("Login"),
            ),
            insert_user(id_page),
            my_button(
                f"{id_page}_reg_accept",
                "Login",
                style_button,
                className="btn btn-outline-primary",
                color="black",
            ),
            my_div(style_div_reg_answer, f"{id_page}_reg_answer"),
            my_div(
                style_div_register,
                "",
                [
                    my_div(
                        style_div_answer,
                        "",
                        html.Label("Nuevo en Big Data App?"),
                    ),
                    my_div(
                        style_div_A,
                        "",
                        html.A("Register", href="/registro"),
                    ),
                ],
            ),
        ],
    )


def user_registry(id_page):
    return my_div(
        style_div_page_registry,
        "",
        my_div(
            style_div_login,
            f"{id_page}_div_registry",
            [
                my_div(
                    {},
                    "",
                    html.H2("Sign In"),
                ),
                insert_user(id_page),
                my_button(
                    f"{id_page}_reg_accept",
                    "Sing in",
                    style_button,
                    className="btn btn-outline-primary",
                    color="black",
                ),
                my_div(style_div_reg_answer, f"{id_page}_reg_answer"),
                my_div(
                    style_div_register,
                    "",
                    [
                        my_div(
                            style_div_answer,
                            "",
                            html.Label("Ir a Big Data App?"),
                        ),
                        my_div(
                            style_div_A,
                            "",
                            html.A("Login", href="/"),
                        ),
                    ],
                ),
            ],
        ),
    )
