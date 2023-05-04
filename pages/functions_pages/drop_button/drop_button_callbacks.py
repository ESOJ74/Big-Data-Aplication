from dash import Input, Output, State, callback, html
from dash.exceptions import PreventUpdate
from pandas import read_json

from assets.my_dash.my_html.my_div import my_div
from utils.create_agGrid import create_adgrid
from utils.create_callback_button_cover import create_callback_button_cover
from utils.create_callback_button_save import (
    create_callback_button_save, create_callback_updates_button_save)

from ..common_css import *

id_page = "drop"


create_callback_button_cover(id_page, f"{id_page}_content_down")
create_callback_button_save(id_page)
create_callback_updates_button_save(id_page, "labels")


@callback(Output(f"{id_page}_content_up", "children"), 
          Input("drop_button", "n_clicks"), 
          prevent_initial_call=True,)
def second_callback(n_clicks):    
    return my_div(style_div_title, "",
                  [
                   html.H5("DataFrame.drop()",
                           style=style_title),
                   html.A("Documentacion",
                          href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html",
                          target="_blank")
                  ])


@callback([
           Output(f"{id_page}_labels", "options"),
           Output(f"{id_page}_div_graph", "children", allow_duplicate=True),
          ],
          Input(f"{id_page}_axis", "value"), 
          State('main_page_store', 'data'),
          prevent_initial_call=True,)
def display_page(axis, data):
    try:
        df = read_json(data["df"])
    except Exception:
        return [[], html.H6("No ha cargado ningún fichero", style={"color": "#31EDF0"})]
    if axis:
        return [df.columns, ""]
    else:
        return [df.index, ""]    
    

@callback(
    [
      Output(f"{id_page}_div_graph", "children"),
      Output("main_page_store", "data", allow_duplicate=True),
      Output(f"{id_page}_loading", "children"),
      Output(f"{id_page}_save", "disabled"),
    ],
    Input(f"{id_page}_refresh", "n_clicks"),
    [ 
      State("main_page_store", "data"),
      State(f"{id_page}_labels", "value"),
      State(f"{id_page}_axis", "value"),
    ],
    prevent_initial_call=True,)
def add_data_to_fig(refresh, data, labels, state_axis):    
    if refresh:        
        try:
            df = read_json(data["df"]).drop(labels, axis=state_axis)  
            data["prov_df"] = df.to_json(orient="columns")
            content = [
                       my_div(style_div_table, "",
                              create_adgrid(f"{id_page}_ag-table", df.head(9))
                       ),
                       html.H6(f"df.drop(labels={labels}, axis={state_axis})",
                               style=style_div_code),
                       ]
            save_disabled = False
        except KeyError:
            content = html.H6("No ha cargado ningún fichero", style={"color": "#31EDF0"})
            save_disabled = True
        except ValueError as err:
            content = html.H6(err.__str__(), style={"color": color_code}),
            save_disabled = True
    else:
        raise PreventUpdate
    return [content, data, "", save_disabled]
