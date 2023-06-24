"""
This script creates a Dash application for a web-based interface with multiple pages.

The module imports necessary modules and defines page layouts for login, registry, and
the main page of the application. It sets up a Dash application instance, configures
the application, and defines the layout structure. The script handles URL changes and
redirects users to the appropriate pages based on their actions.

Modules and Packages:
- contextlib: A module providing utilities for working with context managers.
- os: A module providing functions for interacting with the operating system.
- Dash: The main Dash class for creating Dash applications.
- callback: A decorator for defining callbacks in Dash applications.
- dcc: The Dash Core Components module for interactive UI components.
- html: The Dash HTML Components module for HTML elements.
- Input, Output: Classes from the dash.dependencies module for specifying input and
  output components in Dash callbacks.
- pages: A package containing modules for different page layouts.
- pages.login_layout: A module defining the layout for the login page.
- pages.registry_layout: A module defining the layout for the registry page.
- pages_conf.main_page: A module defining the configuration and layout for the
  main page.

Variables and Configurations:
- ID_PAGE: A string representing the ID for the main page layout.
- app: The Dash application instance.
- app.config.suppress_callback_exceptions: Configuration option to handle missing
  callbacks gracefully.

Application Layout:
- The application layout is defined using HTML and Dash components. It includes a
 `dcc.Location` component to track the current URL and a `Div` element to display the
  page content dynamically.

Callback Function:
- The script defines a callback function that is triggered by changes in the URL. The
  function retrieves the corresponding layout function for the selected page and updates
  the content dynamically. It also handles file operations and redirects the user to
  the appropriate page if necessary.

Application Execution:
- The script runs the Dash application server using `app.run_server(debug=True)`,
  starting the server and running the application in debug mode.

Note: This script provides the foundation for a multi-page Dash application and can be
      extended to include additional pages or functionality as needed.
"""

import contextlib
import os

from dash import Dash, callback, dcc, html
from dash.dependencies import Input, Output

from pages import login_layout, registry_layout
from pages_conf.main_page import main_page_conf

ID_PAGE = "initial_layout"

app = Dash(__name__)
app.config.suppress_callback_exceptions = True

app.layout = html.Div(
    [
        dcc.Location(id=f"{ID_PAGE}_url"),
        html.Div("", f"{ID_PAGE}_content", className="panel-content-app"),
    ],
    className="panel-app",
)


# Update page content
@callback(Output(f"{ID_PAGE}_content", "children"), Input(f"{ID_PAGE}_url", "pathname"))
def display_page(pathname):
    """
    Callback function to display the appropriate page layout based on the URL pathname.

    Args:
        pathname (str): The URL pathname triggering the callback.

    Returns:
        children: The layout of the selected page as the children property of the
                  component.

    The function takes the pathname as an input and returns the corresponding page
    layout.
    It checks the value of the pathname and retrieves the layout function from the
    `pages_list` dictionary.

    The pages_list dictionary contains mappings between different pathnames and their
    corresponding page layouts. If the pathname is "/", indicating the login page, the
    function attempts to remove a file named "user.txt" using `os.remove` to handle a
    possible `OSError`.

    If the pathname is "/app" and the "user.txt" file does not exist, the function
    updates the pathname to "/" to redirect the user back to the login page.

    Finally, the function returns the layout function corresponding to the pathname
    from the `pages_list` dictionary. If the pathname is not found in the dictionary,
    it returns an empty string.
    """
    pages_list = {
        "/": login_layout.layout,
        "/registro": registry_layout.layout,
        "/app": main_page_conf.layout,
    }

    if pathname == "/":
        with contextlib.suppress(OSError):
            os.remove("user.txt")
    if pathname == "/app" and not os.path.exists("user.txt"):
        pathname = "/"

    return pages_list.get(pathname, "")


if __name__ == "__main__":
    app.run_server(debug=True)
