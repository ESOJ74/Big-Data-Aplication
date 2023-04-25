import plotly.express as px
from dash import callback, dcc, html
from dash.dependencies import Input, Output, State
from pandas import read_json
from plotly.colors import sequential

from assets.templates import template_visualizations
from common_functions.common_div_utils import (color_options,
                                               hover_data_options,
                                               refresh_button)
from common_functions.create_callback_button_cover import \
    create_callback_button_cover
from my_dash.my_html.my_div import my_div
from pages.visualization_pages.boxplot_button.boxplot_button_css import *

id_page = "boxplot_button"


# Panel content_up (dropdown)
@callback(Output(f"{id_page}_content_up", "children"),
          Input("boxplot_button", "n_clicks"),
          State('main_page_store', 'data'),
          prevent_initial_call=True)
def display_page(n_clicks, data):   
    df = read_json(data["df"])
    columns = df.columns  
    categoric_columns = [col for col in columns if df[col].dtype == "object"]
    
    return my_div(style_div_selectors, "",
                  [         
                   my_div({"float": "left", "width": "50%"}, "",
                          [          
                           html.H6("x-axis:", style={"font-weight": "bold"}),
                           dcc.Checklist(
                               id=f"{id_page}_x-axis", 
                               options=categoric_columns,
                               inline=True,
                               style={"color": "white", "font-weight": "bold"},
                           ),
                          ],
                   ),
                   my_div({"float": "left", "width": "50%"}, "",
                          [          
                           html.H6("y-axis:", style={"font-weight": "bold"}),
                           dcc.RadioItems(
                               id=f"{id_page}_y-axis", 
                               options=columns,
                               inline=True,
                               style={"color": "white", "font-weight": "bold"},
                           ),
                          ],
                   ),
                  ]         
           )


# Panel content_middle
@callback([
           Output(f"{id_page}_content_middle", "children"),   
           Output(f"{id_page}_visualizations_loading", "children", allow_duplicate=True),
          ],
          [
           Input(f"{id_page}_x-axis", "value"),         
           Input(f"{id_page}_y-axis", "value"),  
           Input(f"{id_page}_refresh", "n_clicks"),
          ],
          [
           State('main_page_store', 'data'),
           State(f"{id_page}_x-axis", "value"),
           State(f"{id_page}_y-axis", "value"),
           State(f"{id_page}_points", 'value'),
           State(f"{id_page}_color", 'value'),
           State(f"{id_page}_quartilemethod", 'value'),
           State(f"{id_page}_notched", 'value'),
           State(f"{id_page}_hover_data", 'value'),
          ],
          prevent_initial_call=True)
def display_page(
    x_axis,
    y_axist,
    n_clicks,
    data,
    x_axis_state,
    y_axis_state,
    points_state,
    color_state,
    quartilemethod_state,
    notched_state,
    hover_data_state,
    ):

    obj = ["", ""]

    if points_state == "false": points_state = False

    if color_state is not None and len(color_state) < 1 or color_state == " ":
        color_state = None 
    notched = True
    if notched_state == "false":
        notched = False
    if hover_data_state is not None and len(hover_data_state) < 1 or hover_data_state == " ":
        hover_data_state = None    

    if y_axis_state and len(y_axis_state) > 0:
        
        df = read_json(data["df"])

        if x_axis_state and len(x_axis_state) > 0:
            fig = px.box(
                      df,
                      template=template_visualizations,
                      x=x_axis_state,
                      y=y_axis_state,
                      height=550,
                      points=points_state,
                      color=color_state,
                      notched=notched,
                      hover_data=hover_data_state,
                      color_discrete_sequence=sequential.Blugrn,
            ).update_layout(legend={"title_font_color": "#acf4ed"})

            fig.update_traces(quartilemethod=quartilemethod_state)
        else:
            fig = px.box(
                      df,
                      template=template_visualizations,
                      y=y_axis_state,
                      height=550,
                      points=points_state,
                      color=color_state,
                      notched=notched,
                      hover_data=hover_data_state,
                      color_discrete_sequence=sequential.Blugrn,
            ).update_layout(legend={"title_font_color": "#acf4ed"})

            fig.update_traces(quartilemethod=quartilemethod_state)
        obj = [dcc.Graph(figure=fig)]               

    return [obj, ""]

       

# color options
color_options(id_page)


# refresh button
refresh_button(id_page)


# hover data options 
hover_data_options(id_page)


create_callback_button_cover(id_page, f"{id_page}_content_middle")
