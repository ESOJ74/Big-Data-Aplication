import plotly.express as px
from dash import callback, dcc
from dash.dependencies import Input, Output, State
from pandas import read_json
from plotly.colors import sequential

from assets.templates_plotly import template_visualizations
from common_functions.common_div_utils import color_options, refresh_button
from common_functions.create_callback_button_cover import \
    create_callback_button_cover
from common_functions.create_content_up import create_double_dropdown

id_page = "scatter_button"

# content_up
create_double_dropdown(id_page)
# color options
color_options(id_page)
# refresh button
refresh_button(id_page)

create_callback_button_cover(id_page, f"{id_page}_content_middle")


# Panel content_middle
@callback([
           Output(f"{id_page}_content_middle", "children"),
           Output(f"{id_page}_visualizations_loading", "children", allow_duplicate=True),
          ],
          [
           Input(f"{id_page}_drop_left", "value"),         
           Input(f"{id_page}_drop_right", "value"),
           Input(f"{id_page}_refresh", "n_clicks"),
          ],
          [
           State('main_page_store', 'data'),
           State(f"{id_page}_drop_left", "value"),
           State(f"{id_page}_drop_right", "value"),
           State(f"{id_page}_color", 'value'),
          ],
          prevent_initial_call=True)
def display_page(
    drop_left_value,
    drop_left_right,
    n_clicks,
    data,
    drop_left_state,
    drop_right_state,
    color_state
    ):     

    obj = ["", ""]

    if color_state is not None and len(color_state) < 1 or color_state == " ":
        color_state = None         
    
    if drop_left_state and drop_right_state:

        df = read_json(data["df"])
        
        fig = px.scatter(
            df,
            template=template_visualizations,
            x=drop_left_state,
            y=drop_right_state,
            height=550,
            color=color_state,     
            color_discrete_sequence=sequential.Plasma,  
        ).update_layout(legend={"title_font_color": "#acf4ed"})        

        obj = [dcc.Graph(figure=fig)]               
    return [obj, ""]
