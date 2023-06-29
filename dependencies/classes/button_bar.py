import dash_bootstrap_components as dbc
from dash import html
from dash_iconify import DashIconify

class BarWithIconCreator:
    """
    A class for creating a bar with an icon and text using Dash and Bootstrap.

    Attributes:
        style_title (dict): The CSS styles for the title container.
        style_icon (dict): The CSS styles for the icon container.

    Methods:
        create_bar_with_icon: Creates a bar with an icon and text.
    """

    style_title = {
        "float": "left",
        "width": "89%",
        "height": "70%",        
        "text-align": "left",
    }
    style_icon = {
        "float": "left",
        "width": "11%",
        "height": "10%",
        "background": "transparent",
    }

    def __init__(self, name_button, id_button, class_button):
        """
        Initializes an instance of the BarWithIconCreator class.

        Args:
            name_button (str or dash component): The text displayed in the bar.
            id_button (str): The ID attribute for the bar.
            class_button (str): The CSS class name for the bar button.
        """
        self.name_button = name_button
        self.id_button = id_button
        self.class_button = class_button

    def create_bar_with_icon(self):
        """
        Creates a bar with an icon and text.

        Returns:
            dbc.Button: The created bar button.
        """
        return dbc.Button(
            children=[
                html.Div(self.name_button, "", style=self.style_title),
                DashIconify(icon="ic:baseline-list", style=self.style_icon),
            ],
            id=self.id_button,
            className=self.class_button,
        )