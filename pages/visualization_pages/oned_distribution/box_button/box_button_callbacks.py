import plotly.express as px
from dash import Input, Output, State, callback, dcc, html
from pandas import read_json

from assets.my_dash.my_html.my_div import my_div
from assets.templates_plotly import template_visualizations
from utils.common_div_utils import selector_options
from utils.create_callback_button_cover import create_callback_button_cover

from ...common_css import *

id_page = "box"


create_callback_button_cover(id_page, f"{id_page}_content_down")
selector_options(id_page, f"{id_page}_X", False)
selector_options(id_page, f"{id_page}_Y")
selector_options(id_page, f"{id_page}_color")
selector_options(id_page, f"{id_page}_hover_data")


@callback(Output(f"{id_page}_content_up", "children"), 
          Input("box_button", "n_clicks"), 
          prevent_initial_call=True,)
def second_callback(n_clicks):    
    return my_div(style_div_title, "",
                  [
                   html.H5("plotly.express.box()",
                           style=style_title),
                   html.A("Documentacion",
                          href="https://plotly.com/python/box-plots/",
                          target="_blank")
                  ])


@callback([
           Output(f"{id_page}_content_down", "children"),   
           Output(f"{id_page}_loading", "children",
                  allow_duplicate=True),           
          ],
          Input(f"{id_page}_refresh", "n_clicks"),
          [
           State("main_page_store", "data"),
           State(f"{id_page}_X", "value"),
           State(f"{id_page}_Y", "value"),
           State(f"{id_page}_points", "value"),
           State(f"{id_page}_color", "value"),
           State(f"{id_page}_quartilemethod", "value"),
           State(f"{id_page}_notched", "value"),
           State(f"{id_page}_hover_data", "value"),
          ],
          prevent_initial_call=True)
def display_page(
    n_clicks,
    data,
    state_X,
    state_Y,
    state_points,
    state_color,
    state_quartilemethod,
    state_notched,
    state_hover_data
    ):     
    
    if state_color is not None and len(state_color) < 1\
        or state_color == " ":
        state_color = None   

    if state_Y is not None and len(state_Y) < 1 or state_Y == " ":
        state_Y = None  

    if state_hover_data is not None and len(state_hover_data) < 1\
        or state_hover_data == " ":
        state_hover_data = None 
    if state_points == "False":
        state_points = False
    state_notched = True if state_notched == "True" else False
    
    if state_X:

        df = read_json(data["df"])

        fig = px.box(
            df,
            template=template_visualizations,
            x=state_X,
            y=state_Y,
            height=550,
            points=state_points,
            color=state_color, 
            notched=state_notched,
            hover_data=state_hover_data,
            color_discrete_sequence=sequential.Plasma,  
        ).update_layout(legend={"title_font_color": color_boton_1}) 
        fig.update_traces(quartilemethod=state_quartilemethod)  
        return [dcc.Graph(figure=fig), ""]
    else:
        return[html.H6("X", style=style_msg), ""]
