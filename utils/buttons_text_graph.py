from dash import html
import dash_bootstrap_components as dbc


class ButtonsTextGraph:
    """
    A class representing buttons for text and graph.

    Parameters:
    - id_page (str): The ID of the page.

    Attributes:
    - id_page (str): The ID of the page.
    - style_div_buttons (dict): The CSS styles for the container div of the buttons.
    - style_button (dict): The CSS styles for the buttons.

    Methods:
    - buttons_text_graph(): Returns the HTML representation of the text and
      graph buttons.
    """

    def __init__(self, id_page):
        """
        Initializes a new instance of the ButtonsTextGraph class.

        Parameters:
        - id_page (str): The ID of the page.
        """
        self.id_page = id_page
        self.style_div_buttons = {
            "margin-left": "2%",
            "margin-top": "8%",
            "width": "96%",
            "height": "10%",
        }        

    def buttons_text_graph(self):
        """
        Returns the HTML representation of the text and graph buttons.

        Returns:
        - html.Div: The container div containing the buttons.
        """
        return html.Div(
            [
                dbc.Button(
                    "Text",
                    f"{self.id_page}_text",
                    n_clicks=1,
                    className="btn-on",
                ),
                dbc.Button(
                    "Graph",
                    f"{self.id_page}_graph",
                    className="btn-text",
                ),
            ],
            style=self.style_div_buttons,
        )
