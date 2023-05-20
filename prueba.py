from dash import Dash, dcc
from assets.my_dash.my_dcc.my_dropdown import my_dropdown

# from app_callbacks import *
from assets.my_dash.my_html.my_div import my_div
from prueba_callbacks import *

app = Dash(__name__)
app.config.suppress_callback_exceptions = True


app.layout = my_div(
    {"position": "absolute", "width": "100%", "height": "100%", "background": "grey"},
    "ff",
    [
        dcc.Location(id="url_"),
        my_div({
            "position": "relative",
                "width": "99.5%",
                "height": "5%",
                "background": "red",
        }, "", my_dropdown("drop_", {}, ["hola"], multi=True)),
        my_div(
            {
                "position": "relative",
                "width": "99.5%",
                "height": "95%",
                "background": "black",
            },
            "app_content_prueba",
        ),
    ],
)


if __name__ == "__main__":
    app.run_server(debug=True)
    