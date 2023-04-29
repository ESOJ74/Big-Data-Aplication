from dash import html

def my_div(style, id="", children="", hidden=False, className=""):

    """
    La función my_div crea un elemento div de HTML utilizando la librería dash-html-components.

    Argumentos:

     style (dict): un diccionario que contiene las propiedades CSS que se aplicarán al elemento div.
     id (str): un identificador único para el elemento div.
     children (list): una lista de elementos de Dash que se colocarán dentro del elemento div.
     hidden (bool): si se establece en True, el elemento div se ocultará.

    Retorno:

     html.Div: el elemento div de HTML con las propiedades especificadas y los elementos secundarios.
    """
    return html.Div(
        style=style,
        children=children,
        id=id,
        hidden=hidden,
        className=className
    )
