from dash import Dash, dcc
from flask import Flask
import streamlit as st

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

def render_dashboard():
    return app.index()

st.write("My Dashboard")
st.write("Below is my dashboard:")
st.write(render_dashboard(), unsafe_allow_html=True)
