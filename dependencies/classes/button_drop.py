import dash_bootstrap_components as dbc
from dash import html
from dash_iconify import DashIconify


class ButtonDropCreator:
    """
    A class for creating a dropdown button with a name and icon using Dash and Bootstrap.

    Attributes:
        style_div (dict): The CSS styles for the name container div.
        style_icon (dict): The CSS styles for the icon container.

    Methods:
        button_drop: Creates a dropdown button with a name and icon.
    """

    style_div = {
        "float": "left",
        "margin-left": "16%",
        "margin-top": "1%",
        "width": "69%",
    }
    
    def __init__(self, name_button, id_button, class_button):
        """
        Initializes an instance of the ButtonDropCreator class.

        Args:
            name_button (str or dash component): The name displayed in the button.
            id_button (str): The ID attribute for the button.
            class_button (str): The CSS class name for the button.
        """
        self.name_button = name_button
        self.id_button = id_button
        self.class_button = class_button
        self.style_icon = {"float": "left", "width": "15%", "height": "100%"}

    def panel(self):
        """
        Creates a dropdown button with a name and icon.

        Returns:
            dbc.Button: The created dropdown button.
        """
        name = html.Div(self.name_button, style=self.style_div)
        icon = DashIconify(
            id=f"icon_{self.id_button}",
            icon="carbon:caret-sort-down",
            style=self.style_icon,
        )
        return dbc.Button(
            [name, icon],
            self.id_button,
            className=self.class_button,
        )
