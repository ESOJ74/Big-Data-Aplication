import dash_bootstrap_components as dbc
from dash import dcc, html


style_res = {
    "position": "relative",
    "left": "0%",
    "top": "3%",
    "width": "100%",
    "color": "white",
    "font-size": "calc(0.1rem + 1vw)",
    "text-align": "center",
}


class UserLogin:
    """
    Represents a user login component in Dash.

    Args:
        id_page (str): The ID of the user login component.
        className (str): The class name of the user login component.

    Attributes:
        id_page (str): The ID of the user login component.
        className (str): The class name of the user login component.
        title (str): The title of the user login component.
        pathname (str): The pathname of the user login component.
        name_pathname (str): The name of the pathname of the user login component.

    Methods:
        set_title(title): Sets the title of the user login component.
        set_pathname(name_pathname, pathname): Sets the pathname and name of the user
        login component.
        create_input(msg, id_input): Creates an input field for the user login
        component.
        user_login(): Generates a `html.Div` element representing the user login
        component.

    Example usage:

    user_login = UserLogin(id_page="user-login", className="user-login-component")
    user_login.set_title("User Login")
    user_login.set_pathname("Register", "register")
    input_field = user_login.create_input("Username", "username-input")
    login_component = user_login.user_login()
    """

    def __init__(self, id_page, className):
        self.id_page = id_page
        self.className = className
        self.title = ""
        self.pathname = ""
        self.name_pathname = ""

    def set_title(self, title):
        """
        Set the title of the user login component.

        Args:
            title (str): The title of the user login component.
        """
        self.title = title

    def set_pathname(self, name_pathname, pathname):
        """
        Set the pathname and name of the user login component.

        Args:
            name_pathname (str): The name of the pathname of the user login component.
            pathname (str): The pathname of the user login component.
        """
        self.pathname = pathname
        self.name_pathname = name_pathname

    def create_input(self, msg, id_input):
        """
        Create an input field for the user login component.

        Args:
            msg (str): The placeholder message for the input field.
            id_input (str): The ID of the input field.

        Returns:
            dash_html_components.Div: The input field as a `html.Div` element.
        """
        return html.Div(
            children=[
                dcc.Input(
                    id=id_input,
                    placeholder=msg,
                    className="input-login",
                )
            ],
            className="row-100 input-login-container",
        )

    def user_login(self):
        """
        Generate a `html.Div` element representing the user login component.

        Returns:
            dash_html_components.Div: The user login component as a `html.Div` element.
        """
        return html.Div(
            [
                html.Div(
                    html.Div(self.title, className="title-login"),
                    className="row-100 title-login-container",
                ),
                html.Div(
                    [
                        self.create_input("Usuario", f"{self.id_page}_reg_user"),
                        self.create_input("Contraseña", f"{self.id_page}_reg_pass"),
                    ],
                    style={"margin-top": "5%"},
                ),
                html.Div(
                    dbc.Button(
                        self.title,
                        f"{self.id_page}_reg_accept",
                        className="btn-login",
                    ),
                    className="row-100 btn-login-container",
                ),
                html.Div(
                    [
                        html.Div(
                            "Nuevo en Big Data App?",
                            className="msg-login",
                        ),
                         
                            html.A(
                                self.name_pathname,
                                href=f"/{self.pathname}",
                                className="a-login",
                            ),
                            
                       
                    ],
                    className="row-100 msg-login-container",
                ),
                html.Div(
                    "",
                    f"{self.id_page}_reg_answer",
                    style=style_res,
                ),
            ],
            className=self.className,
        )
