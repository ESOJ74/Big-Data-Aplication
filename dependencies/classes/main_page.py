from dash import dcc, html
from pages_conf.main_page.panel_button_cover import panel_button_cover

class MainPage:
    """
    Represents a main page layout in Dash.

    Args:
        id_page (str): The ID of the main page.
        className (str): The class name of the main page.

    Attributes:
        id_page (str): The ID of the main page.
        className (str): The class name of the main page.
        panel_up (obj or None): The panel at the top of the main page.
        middle_panel (obj or None): The middle panel of the main page.
        panel_footer (obj or None): The panel at the bottom of the main page.

    Methods:
        update_panel_up(obj): Updates the panel at the top of the main page.
        update_middle_panel(obj): Updates the middle panel of the main page.
        update_panel_footer(obj): Updates the panel at the bottom of the main page.
        main_page(): Generates a `html.Div` element representing the main page layout.

    Example usage:

    main_page = MainPage(id_page="my-main-page", className="main-page")
    main_page.update_panel_up(html.Div([html.H1("Welcome to Dash!")]))
    main_page.update_middle_panel(html.Div([html.P("This is the content of the
                                                    main page.")]))
    main_page.update_panel_footer(html.Div([html.P("Footer content")]))
    main_page_layout = main_page.main_page()
    """

    def __init__(self, id_page, className):
        self.id_page = id_page
        self.className = className
        self.panel_up = None
        self.middle_panel = None
        self.panel_footer = None

    def update_panel_up(self, obj):
        """
        Update the panel at the top of the main page.

        Args:
            obj: The new panel at the top of the main page.
        """
        self.panel_up = obj

    def update_middle_panel(self, obj):
        """
        Update the middle panel of the main page.

        Args:
            obj: The new middle panel of the main page.
        """
        self.middle_panel = obj

    def update_panel_footer(self, obj):
        """
        Update the panel at the bottom of the main page.

        Args:
            obj: The new panel at the bottom of the main page.
        """
        self.panel_footer = obj

    def main_page(self):
        """
        Generate a `html.Div` element representing the main page layout.

        Returns:
            dash_html_components.Div: The main page layout as a `html.Div` element.
        """
        return html.Div(
            [
                dcc.Store(id=f"{self.id_page}_store"),
                self.panel_up,
                panel_button_cover,
                self.middle_panel,
                self.panel_footer,
            ],
            className=self.className,
        )
