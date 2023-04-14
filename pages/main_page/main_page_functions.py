from importlib import import_module

from dash import callback
from dash.dependencies import Input, Output

from my_dash.my_dbc.my_button import my_button
from my_dash.my_html.my_div import my_div


def create_div_buttons(style_div: dict, tittle: str, style_button, button_list: list, color="dark", className="btn btn-outline-success") -> dict:
    """
    Crea y devuelve un elemento div que contiene un título y una lista de botones.

    Args:
        style_div (dict): Diccionario que contiene las propiedades CSS para aplicar al elemento div.
        tittle (str): El texto del título que se mostrará en el elemento div.
        button_list (list): Una lista de tuplas que contienen la información necesaria para crear cada botón.

    Returns:
        dict: Un elemento div que contiene un título y una lista de botones.

    Comportamiento:
        La función toma los argumentos de entrada y utiliza la función my_div y my_button para crear el elemento div.
        El título se muestra en un elemento div con un margen izquierdo del 10%, mientras que los botones se muestran
        en una lista de elementos div con un margen superior del 1%. La lista de botones se crea utilizando una comprensión de lista.
        Cada botón se crea utilizando la función my_button y se agrega a la lista de elementos div.
    """

    return my_div(style_div, "",
                  [
                    my_div({"margin-left": "10%"}, "", tittle),
                    *[my_div({"margin-top": "1%", "width": "90%"}, "",
                             my_button(button[0],
                                       button[1],
                                       style_button,
                                       color="dark",
                                       className=className)
                      ) for button in button_list]
                   ]
           )


def create_callback(buttons_list: list, module: str, button_name: str = "") -> None:
    """
    Esta función crea un callback para mostrar el contenido de las páginas de la aplicación.

    Args:
    - buttons_list (list): Lista de tuplas con la información de los botones. Cada tupla debe contener los siguientes elementos:
        - El ID del botón (str).
        - El nombre del botón (str).
        - El estilo del botón (dict).
    - module (str): El nombre del módulo que contiene las páginas.
    - button_name (str, opcional): El tipo de botón.

    Returns:
    - None    
    """ 
    @callback(
        [Output("main_page_page_content", "children", allow_duplicate=True)] +
        list(map(lambda x: Output(x[0], "n_clicks"), buttons_list)),
        list(map(lambda x: Input(x[0], "n_clicks"), buttons_list)),
        prevent_initial_call=True)
    def display_page(*args):
        button = buttons_list[list(args).index(1)][0]
        try:
            cont = [import_module(f'pages.{module}.{button}.{button}_layout').layout]
        except ModuleNotFoundError:
            cont = [f"{button_name} no implementada"]
        return cont + [0 for x in buttons_list]
