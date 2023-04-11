import dash
from dash import dcc
from flask import Flask

from app_callbacks import *
from my_dash.my_html.my_div import my_div

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
server = Flask(__name__)
app = dash.Dash(server=server)
app.config.suppress_callback_exceptions = True

app.layout = my_div({"width": "100%", "height": "100%"}, "", 
                    [
                     dcc.Location(id="url"),
                     my_div({"width": "100%", "height": "100%"},
                            "app_content")
                    ]
             )

if __name__ == "__main__":
    app.run_server(debug=True)




