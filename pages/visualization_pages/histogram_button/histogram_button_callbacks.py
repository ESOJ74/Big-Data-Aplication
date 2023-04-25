import plotly.express as px
from dash import callback, dcc
from dash.dependencies import Input, Output, State
from pandas import read_json
from plotly.colors import sequential

from assets.templates import template_visualizations
from common_functions.common_div_utils import color_options, refresh_button
from common_functions.create_callback_button_cover import \
    create_callback_button_cover
from common_functions.create_content_up import create_single_dropdown
from pages.visualization_pages.histogram_button.histogram_button_css import *

id_page = "histogram"


# Panel content_up (dropdown)
create_single_dropdown(id_page, f"{id_page}_content_up", style_selector)


# Panel content_middle
@callback([
           Output(f"{id_page}_content_middle", "children"),           
           Output(f"{id_page}_visualizations_loading", "children", allow_duplicate=True),
          ],
          Input(f"{id_page}_dropdown", "value"),  
          Input(f"{id_page}_refresh", "n_clicks"),
          [
           State('main_page_store', 'data'),
           State(f"{id_page}_nbins", 'value'),
           State(f"{id_page}_color", 'value'),
          ],
          prevent_initial_call=True)
def display_page(
    dropdown_value,
    n_clicks,
    data,
    nbins_state,
    color_state):    

    obj = ["", ""]

    if color_state is not None and len(color_state) < 1 or color_state == " ":
        color_state = None          
    
    if dropdown_value:             
        df = read_json(data["df"])
        
        fig = px.histogram(
            df,
            template=template_visualizations,
            x=dropdown_value,
            height=550,
            color=color_state,
            nbins=int(nbins_state),     
            color_discrete_sequence=sequential.Blugrn,  
        ).update_layout(legend={"title_font_color": "#acf4ed"})         

        obj = [dcc.Graph(figure=fig)]    
                 
    return [obj, ""]


# color options
color_options(id_page)


# refresh button
refresh_button(id_page)


create_callback_button_cover(id_page, f"{id_page}_content_middle")
