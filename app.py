from dash import Dash, dcc
from flask import Flask

from app_callbacks import *
from my_dash.my_html.my_div import my_div

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
BS = ["https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"]


app = Dash(__name__)
app.config.suppress_callback_exceptions = True

app.layout = my_div({"width": "100%", "height": "100%"}, "", 
                    [
                     dcc.Location(id="url"),
                     my_div({"width": "100%", "height": "100%"},
                            "app_content")
                    ]
             )
import os
#port=os.environ["PORT"]
  
if __name__ == "__main__":
    #app.run('0.0.0.0',int(port), debug=True)
    app.run_server(debug=True)
