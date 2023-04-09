import dash
from flask import Flask

from pages.main_page import main_page_layout

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
server = Flask(__name__)
app = dash.Dash(server=server)
app.config.suppress_callback_exceptions = True

app.layout = main_page_layout.layout

if __name__ == "__main__":
    app.run_server(debug=True)
