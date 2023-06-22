from dash import html


class Panel:
    """
    Represents a panel in Dash.

    Args:
        id_page (str, optional): The ID of the panel. Defaults to "".

    Attributes:
        id_page (str): The ID of the panel.
        className (str or None): The class name of the panel.
        children (list or None): The child elements of the panel.
        hidden (bool): Indicates whether the panel is hidden or not.

    Methods:
        update_id_page(id_page): Updates the ID of the panel.
        update_hidden(hidden): Updates the hidden status of the panel.
        update_panel(obj=[], className=None): Updates the child elements and class name of the panel.
        panel(): Generates a `html.Div` element representing the panel.

    Example usage:

    panel = Panel(id_page="my-panel")
    panel.update_hidden(True)
    panel.update_panel([html.H1("Panel Content")], className="panel-class")
    panel_element = panel.panel()
    """

    def __init__(self, id_page=""):
        self.id_page = id_page
        self.className = None
        self.children = None
        self.hidden = False

    def update_hidden(self, hidden):
        """
        Update the hidden status of the panel.

        Args:
            hidden (bool): Indicates whether the panel should be hidden or not.
        """
        self.hidden = hidden

    def update_panel(self, obj=None, className=None):
        """
        Update the child elements and class name of the panel.

        Args:
            obj (list, optional): The child elements of the panel. Defaults to an empty list.
            className (str, optional): The class name of the panel. Defaults to None.
        """
        if obj is None:
            obj = []
        self.children = obj
        self.className = className

    def panel(self):
        """
        Generate a `html.Div` element representing the panel.

        Returns:
            dash_html_components.Div: The panel as a `html.Div` element.
        """
        return html.Div(
            self.children, self.id_page, className=self.className, hidden=self.hidden
        )
