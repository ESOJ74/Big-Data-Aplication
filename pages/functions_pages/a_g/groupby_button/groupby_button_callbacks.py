from dash import Input, Output, State, callback, html
from pandas import read_json

from assets.my_dash.my_html.my_div import my_div
from utils.button_apply import button_apply, button_save
from utils.create_callback_button_cover import create_callback_button_cover
from utils.select_labels import select_labels

from ...common_css import *

id_page = "groupby"


create_callback_button_cover(id_page)


@callback(Output(f"{id_page}_content_up", "children"), 
          Input("groupby_button", "n_clicks"), 
          prevent_initial_call=True,)
def second_callback(n_clicks):    
    return my_div(style_div_title, "",
                  [
                   html.H5("DataFrame.groupby()",
                           style=style_title),
                   html.A("Documentacion",
                          href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html",
                          target="_blank")
                  ])


@callback(Output(f"{id_page}_by", "options"),
          Input(f"{id_page}_axis", "value"), 
          State('main_page_store', 'data'),)
def display_page(axis, data):
    df = read_json(data["df"])
    return select_labels(df, axis, True)
    

@callback(
    [
      Output(f"{id_page}_div_graph", "children"),
      Output("main_page_store", "data", allow_duplicate=True),
      Output(f"{id_page}_loading", "children"),         
      Output(f"{id_page}_refresh", "children"),
      Output(f"{id_page}_refresh", "n_clicks"),
      Output(f"{id_page}_by", "options", allow_duplicate=True)
    ],
    [
      Input(f"{id_page}_refresh", "n_clicks"),
      Input(f"{id_page}_by", "value"),
    ],
    [ 
      State("main_page_store", "data"),
      State(f"{id_page}_by", "value"),
      State(f"{id_page}_axis", "value"),
      State(f"{id_page}_refresh", "children"),     
    ],
    prevent_initial_call=True,)
def add_data_to_fig(clicks_button, click, data, state_by, state_axis, name_button):       
    action = f"""df = df.groupby({state_by}, axis={state_axis}).sum()"""
    if clicks_button:
        if name_button == "Apply":        
            try:
                df = read_json(data["df"]).groupby(state_by,
                                                   axis=state_axis).sum()           
                df = df.reset_index()
                data["prov_df"] = df.to_json(orient="columns")
                msg = html.H6(f"df.groupby({state_by}).sum()",
                               style=style_div_code)
                name_button, content = button_apply(id_page, df, msg)
                state_by = select_labels(df, state_axis, True)            
            except (KeyError, ValueError) as err:
                content = html.H6(err.__str__(), style={"color": color_code}),
        else:            
            df = read_json(data["prov_df"])
            data["df"] = df.to_json(orient="columns")
            name_button, content = button_save(f"""users/{data["user"]}/workflow.txt""",
                                               ["", action])    
            state_by = select_labels(df, state_axis, True)
    else:
        df = read_json(data["df"])
        state_by = select_labels(df, state_axis, True) 
        content = ""
        name_button = "Apply"    
    return [content, data, "", name_button, 0, state_by]
   