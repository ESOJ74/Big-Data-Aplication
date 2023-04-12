import dash_bootstrap_components as dbc


def my_button(id, children, style, color="secondary", className="btn btn-outline-success", hidden=False, disabled=False, n_clicks=0):
    """
    La función my_button crea un botón de HTML utilizando la librería dash-html-components.

    Argumentos:

     id (str): un identificador único para el botón.
     nombre (str o elementos de dash): el texto o elementos de Dash que se mostrarán en el botón.
     style (dict): un diccionario que contiene las propiedades CSS que se aplicarán al botón.
     hidden (bool): si se establece en True, el botón se ocultará.
     disabled (bool): si se establece en True, el botón se deshabilitará.
     n_clicks (int): el número de veces que se ha hecho clic en el botón.

    Retorno:

     html.Button: el botón de HTML con las propiedades especificadas."""
    
    return dbc.Button(
        children=children,
        id=id,
        color=color,
        className=className,
        style=style,
        n_clicks=n_clicks,               
        disabled=disabled,
    )