from dash import callback
from dash.dependencies import Input, Output

import pages

lista_de_paginas = {
    "/aplicacion": pages.main_page.main_page_layout.layout,
    "/registro": pages.users_registry.users_registry_layout.layout
}


# Update page content
@callback(Output("app_content", "children"),
          Input("url", "pathname"))
def display_page(pathname):
    if pathname in lista_de_paginas:
        return lista_de_paginas[pathname]
    
