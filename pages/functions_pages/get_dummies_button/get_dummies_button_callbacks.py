from dash import Input, Output, State, callback, html
from dash.exceptions import PreventUpdate
from pandas import DataFrame, concat, get_dummies, read_json

from assets.my_dash.my_html.my_div import my_div
from utils.common_div_utils import selector_options
from utils.create_agGrid import create_adgrid
from utils.create_callback_button_cover import create_callback_button_cover
from utils.create_callback_button_save import (
    create_callback_button_save, create_callback_updates_button_save)

from ..common_css import *

id_page = "get_dummies"


create_callback_button_cover(id_page, f"{id_page}_content_down")
create_callback_button_save(id_page)
create_callback_updates_button_save(id_page, "labels")
selector_options(id_page, f"{id_page}_prefix")
selector_options(id_page, f"{id_page}_columns")


@callback(Output(f"{id_page}_content_up", "children"), 
          Input("get_dummies_button", "n_clicks"), 
          prevent_initial_call=True,)
def second_callback(n_clicks):    
    return my_div(style_div_title, "",
                  [
                   html.H5("DataFrame.get_dummies()",
                           style=style_title),
                   html.A("Documentacion",
                          href="https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html",
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
      State(f"{id_page}_prefix", "value"),
      State(f"{id_page}_dummy_na", "value"),
      State(f"{id_page}_columns", "value"),
      State(f"{id_page}_sparse", "value"),
      State(f"{id_page}_drop_first", "value"),
      State(f"{id_page}_dtype", "value"),
    ],
    prevent_initial_call=True,)
def add_data_to_fig(refresh, data, state_prefix, state_dummy_na, state_columns, state_sparse, state_drop_first, state_dtype):    
    if refresh:        
        try:
            if state_prefix is not None and len(state_prefix) < 1 or state_prefix[0] == " ":
               state_prefix = None
            if state_columns is not None and len(state_columns) < 1 or state_columns[0] == " ":
               state_columns = None
            state_dummy_na = True if state_dummy_na == "True" else False
            state_sparse = True if state_sparse == "True" else False
            state_drop_first = True if state_drop_first == "True" else False
            match state_dtype:
                case "int":
                    state_dtype_2 = int
                case "float":
                    state_dtype_2 = float
                case "str":
                    state_dtype_2 = str
                case "bool":
                    state_dtype_2 = bool

            df = read_json(data["df"])
            df = get_dummies(df, prefix=state_prefix, dummy_na=state_dummy_na,
                                columns=state_columns, sparse=state_sparse,
                                drop_first=state_drop_first, dtype=state_dtype_2)  

            data["prov_df"] = df.to_json(orient="columns")

            cod1 = f"pd.get_dummies(df, prefix={state_prefix}, dummy_na={state_dummy_na},"
            cod2 = f" columns={state_columns}, sparse={state_sparse}, drop_first={state_drop_first},"
            cod3 = f" dtype={state_dtype})"
            df_codigo = DataFrame(
                           {"codigo": [f"{cod1}{cod2}{cod3}"]}
                        )

            data["prov_cod"] = concat([read_json(data["pipeline"]),
                                       df_codigo]
                               ).reset_index(drop=True).to_json(orient="columns")

            content = [
                       my_div(style_div_table, "",
                              create_adgrid(f"{id_page}_ag-table", df.head(9))
                       ),
                       html.H6(f"{cod1}{cod2}{cod3}", style=style_div_code),
                      ]
            save_disabled = False
        except (KeyError, ValueError) as err:
            content = html.H6(err.__str__(), style={"color": color_code}),
            save_disabled = True
    else:
        raise PreventUpdate
    return [content, data, "", save_disabled]
