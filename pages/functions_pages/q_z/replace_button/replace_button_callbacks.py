from dash import Input, Output, State, callback, html
from dash.exceptions import PreventUpdate
from pandas import DataFrame, concat, read_json

from assets.my_dash.my_html.my_div import my_div
from utils.create_agGrid import create_adgrid
from utils.create_callback_button_cover import create_callback_button_cover
from utils.create_callback_button_save import create_callback_button_save

from ...common_css import *

id_page = "replace"


create_callback_button_cover(id_page, f"{id_page}_content_down")
create_callback_button_save(id_page)


@callback(Output(f"{id_page}_content_up", "children"), 
          Input("replace_button", "n_clicks"), 
          prevent_initial_call=True,)
def second_callback(n_clicks):    
    return my_div(style_div_title, "",
                  [
                   html.H5("DataFrame.replace()",
                           style=style_title),
                   html.A("Documentacion",
                          href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.replace.html",
                          target="_blank")
                  ])

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
      State(f"{id_page}_to_replace", "value"),
      State(f"{id_page}_value", "value"),
      State(f"{id_page}_limit", "value"),
      State(f"{id_page}_regex", "value"),
    ],
    prevent_initial_call=True,)
def add_data_to_fig(refresh, data, to_replace, value, limit, regex):    
    if refresh:        
        try:
            try:
                to_replace = float(to_replace) if "." in to_replace else int(to_replace)
            except:
                pass

            try:
                value = float(value) if "." in value else int(value)
            except:
                pass
            
            limit = None if limit == " " else int(limit)            
            regex = True if regex == "True" else False
            
            cod1 = f"""df.replace(to_replace="{to_replace}", """
            cod2 = f"value={value}, "
            cod3 = f"limit={limit}, regex={regex})"

            if regex == True:
                import re
                to_replace = re.compile(to_replace)
                cod1 = f"""df.replace(to_replace={to_replace}, """                
            if value:
                cod2 = f"""value="{value}", """                   
            cod = cod1 + cod2 + cod3

            df = read_json(data["df"]).replace(to_replace=to_replace,
                                               value=value, limit=limit,
                                               regex=regex)  
            
            data["prov_df"] = df.to_json(orient="columns")
            
            df_codigo = DataFrame(
                           {"codigo": [cod]}
                        )
            data["prov_cod"] = concat([read_json(data["pipeline"]),
                                       df_codigo]
                               ).reset_index(drop=True).to_json(orient="columns")

            content = [
                       my_div(style_div_table, "",
                              create_adgrid(f"{id_page}_ag-table", df.head(9))
                       ),
                       html.H6(cod, style=style_div_code),
                      ]
            save_disabled = False
        except (KeyError, ValueError, TypeError) as err:
            content = html.H6(err.__str__(), style={"color": color_code}),
            save_disabled = True
    else:
        raise PreventUpdate
    return [content, data, "", save_disabled]
