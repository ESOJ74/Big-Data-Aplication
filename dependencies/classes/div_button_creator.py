import dash_bootstrap_components as dbc
from dash import html


class DivButtonCreator:
    """
    A class for creating a div element with buttons using Dash and Bootstrap.

    Attributes:
        classdiv (str): The CSS class name for the outer div element.
        button_list (list): A list of button configurations. Each button configuration
                            should be a tuple with two elements: the button label and
                            the button ID.
        hidden (bool): Indicates whether the div should be initially hidden or visible.
        id_div (str): The ID attribute for the outer div element.
        button_classname (str): The CSS class name for each button.
        div_button_classname (str): The CSS class name for each div containing a button.

    Methods:
        update_id_div: Updates the ID attribute for the outer div element.
        update_button_classname: Updates the CSS class name for each button.
        update_hidden: Updates the visibility state of the div.
        panel: Generates a div element with buttons based on the provided
               button configurations and assigned attributes.
    """

    def __init__(self, class_div, button_list):
        """
        Initializes an instance of the DivButtonCreator class.

        Args:
            class_div (str): The CSS class name for the outer div element.
            button_list (list): A list of button configurations.
        """
        self.classdiv = class_div
        self.button_list = button_list
        self.hidden = True
        self.id_div = ""
        self.button_classname = ""
        self.div_button_classname = ""

    def update_id_div(self, id_div):
        """
        Updates the ID attribute for the outer div element.

        Args:
            id_div (str): The new ID attribute for the outer div element.
        """
        self.id_div = id_div

    def update_div_button_classname(self, div_button_classname):
        """
        Updates the CSS class name for each div containing a button.

        Args:
            div_button_classname (str): The new CSS class name for each div containing
            a button.
        """
        self.div_button_classname = div_button_classname

    def update_button_classname(self, button_classname):
        """
        Updates the CSS class name for each button.

        Args:
            button_classname (str): The new CSS class name for each button.
        """
        self.button_classname = button_classname

    def update_hidden(self, hidden):
        """
        Updates the visibility state of the div.

        Args:
            hidden (bool): True if the div should be hidden, False if it should be
            visible.
        """
        self.hidden = hidden

    def panel(self):
        """
        Generates a div element with buttons.

        Returns:
            Div: A Dash Div element containing the buttons.
        """
        div_buttons = [
            html.Div(
                dbc.Button(
                    button[1],  # children of button
                    button[0],  # id of button
                    className=self.button_classname,
                ),
                className=self.div_button_classname,
            )
            for button in self.button_list
        ]
        return html.Div(
            div_buttons, self.id_div, className=self.classdiv, hidden=self.hidden
        )
