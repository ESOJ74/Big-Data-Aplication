from dash import dcc


def my_dropdown(id, style, options=[], value="", placeholder="", multi=False):
    """
    La función my_dropdown crea un elemento dropdown de HTML utilizando la
    librería dash-core-components.

    Argumentos:

     id (str): un identificador único para el elemento dropdown.
     style (dict): un diccionario que contiene las propiedades CSS que se aplicarán
       al elemento dropdown.
     options (list): una lista de las opciones del elemento dropdown.
     value (str o list): el valor seleccionado en el elemento dropdown. Si multi es True,
       debe ser una lista de valores.
     placeholder (str): el texto que se mostrará en el elemento dropdown si no se ha
       seleccionado ningún valor.
     multi (bool): si se establece en True, el elemento dropdown permitirá la selección
       de múltiples valores.

    Retorno:

     dcc.Dropdown: el elemento dropdown de HTML con las propiedades especificadas.
    """
    return dcc.Dropdown(
        style=style,
        id=id,
        options=options,
        value=value,
        placeholder=placeholder,
        multi=multi
    )
