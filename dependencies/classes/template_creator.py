from dash import html, dcc


class TemplateCreator:
    """
    A class for creating templates using Dash HTML components.

    The TemplateCreator class provides methods for creating the content, parameters, and the overall template structure
    using the Dash HTML components.

    Attributes:
    - id_page (str): The ID of the page.
    - content_up (str): The content for the upper section of the template.
    - content_down (str): The content for the lower section of the template.
    - params (str): The parameters for the template.

    Methods:
    - __init__(self, id_page): Initializes a TemplateCreator object with the given ID.
    - create_content_up(content, className): Creates the content for the upper section of the template.
    - create_content_down(content, className): Creates the content for the lower section of the template.
    - create_params(content, className): Creates the parameters for the template.
    - create_template(): Creates the final template structure.
    """
    def __init__(self, id_page):
        """
        Initializes a TemplateCreator object.

        Parameters:
        - id_page (str): The ID of the page.
        """
        self.id_page = id_page
        self.content_up = ""
        self.content_down = ""
        self.params = ""

    def create_content_up(self, content, className):
        """
        Creates the content for the upper section of the template.

        Parameters:
        - content (str): The content for the upper section.
        - className (str): The class name for the content.

        Returns:
        None
        """
        self.content_up = html.Div(
            content, f"{self.id_page}_content_up", className=className
        )

    def create_content_down(self, content, className):
        """
        Creates the content for the lower section of the template.

        Parameters:
        - content (str): The content for the lower section.
        - className (str): The class name for the content.

        Returns:
        None
        """
        self.content_down = html.Div(
            content, f"{self.id_page}_content_down", className=className
            )

    def create_params(self, content, className):
        """
        Creates the parameters for the template.

        Parameters:
        - content (str): The parameters content.
        - className (str): The class name for the parameters.

        Returns:
        None
        """
        self.params = html.Div(
            content, f"{self.id_page}_params", className=className
            )

    def create_template(self):
        """
        Creates the template.

        Returns:
        html.Div: The template as an HTML div element.
        """
        loading = dcc.Loading(
                id="loading-2",
                children=html.Div(id="loading"),
                type="cube",
                fullscreen=False,
                color="#20c997",
                className="panel-loading",
            )
        return html.Div(
            [self.content_up, loading, self.content_down, self.params], className="panel-creator"
            )
    #"graph","cube","circle","dot","default"