from dash import callback, dcc
from dash.dependencies import Input, Output, State
from pandas import read_json
from my_dash.my_dcc.my_dropdown import my_dropdown
from my_dash.my_dbc.my_button import my_button
from my_dash.my_html.my_div import my_div
import plotly.express as px

id_page = "histogram_button"

s_selector = {
    "position": "relative",
    "top": "20%",
    "left": "2.4%",
    "width": "17.5%",
    "height": "48%",
    "border-radius": "7px 7px 5px 5px",
    "padding": "2px 2px 0px 2px",
    "font-size": "1em",
    "background": "#699B8F",
}

s_content_down = {
    "position": "relative",    
    "top": "5%",
    "left": "2.4%",
    "width": "30%",
    "background": "white",
}

s_utils = {
    "position": "relative",    
    "top": "2%",
    "left": "5%",
    "width": "100%",
    "height": "100%",
}

style_input = {
    "font-family": "Roboto, Helvetica, Arial, sans-serif",
    "width": "10%"
}

@callback(Output(f"{id_page}_utils", "children"),          
          Input("histogram_button", "n_clicks"),
          prevent_initial_call=True)
def display_page(n_clicks):  

    obj = my_div(s_utils, "",
                 [
                   my_div({}, "", 
                          [
                           dcc.Input(id=f"{id_page}_nbins",
                                          placeholder="Introduce la ruta del archivo",
                                          style=style_input,
                                          value=20,
                                )
                          ]
                   ),
                   my_div({}, "", "f"),
                   my_div({}, "", "g"),
                   my_div({}, "", "e"),
                 ]
          )
    return obj


@callback([           
           Output(f"{id_page}_content_up", "children"),
          ],
          Input("histogram_button", "n_clicks"),
          State('main_page_store', 'data'),
          prevent_initial_call=True)
def display_page(n_clicks, data):          

    columns = read_json(data["df"]).columns

    return my_div(s_selector, "",
                  my_dropdown(f"{id_page}_dropdown",
                              {},
                              columns,
                              value=columns[0],
                              placeholder="Seleccione columna"
                  ),
           ),
    

@callback([
           Output(f"{id_page}_content_middle", "children"),           
           Output(f"{id_page}_content_down", "children"),
          ],
          [
           Input(f"{id_page}_dropdown", "value"),           
          ],
          [
           State('main_page_store', 'data'),
           State(f"{id_page}_nbins", 'value'),
          ],
          prevent_initial_call=True)
def display_page(
    dropdown_value,
    data,
    nbins_state):          
    
    obj = ["", ""]
    if dropdown_value:
        # content_middle
        df = read_json(data["df"])
        fig = px.histogram(
            df,
            x=dropdown_value,
            nbins=int(nbins_state))
        obj = [dcc.Graph(figure=fig)]
        # content_down

        obj.append(
            my_div(s_content_down, "", 
                   [
                     my_div({}, "", "import plotly.express as px"),
                     my_div({"margin-top": "2%"}, "", "fig = px.histogram(df,"),
                     my_div({"margin-left": "30%"}, "", f"     x=\"{dropdown_value}\","),
                     my_div({"margin-left": "30%"}, "", f"     nbins={int(nbins_state)})"),
                     my_div({}, "", "fig.show()")
                   ]
            )
        )
    return obj
