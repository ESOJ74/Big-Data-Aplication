from dash import html
import dash_bootstrap_components as dbc
from callbacks.load_data import *  # noqa: F403

id_page = "load_data"

content_up = html.Div(        
        [
            dbc.Button(
                 "Archivos", 
                f"{id_page}_archivos",
                className="button-panel-load"                            
            ),
            dbc.Button(
                "Up File from Local",
                f"{id_page}_up_file",
                className="button-panel-load"
            ),
            dbc.Button(
                "Up File from DataBase",
                f"{id_page}_database",
                className="button-panel-load"               
            ),
            html.A(
                "Documentación",
                href="https://pandas.pydata.org/docs/reference/io.html",
                target="_blank",
                className="doc-panel-data"
            ),
        ],
        className="panel-tittles-data"
    )

content_down = html.Div(
    id=f"{id_page}_content_down",
)
params = [html.Div(className="no-params")]
