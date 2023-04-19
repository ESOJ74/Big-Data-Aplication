from dash import Input, Output, State, callback, dcc, html
from pandas import read_json

from my_dash.my_html.my_div import my_div

style_div_content = {
    "position": "relative",
    "top": "10%",
    "left": "30%",
    "width": "25%",
    "font-size": "1.2em",
    "font-weight": "bold",
    "background": "#C5F4FD",
    "color": "#03353E",
}

id_page = "info"

layout = [
          dcc.Loading(
              id="loading-2",
              children=[my_div({"margin-top": "10%"}, f"{id_page}_info_loading")],
              type="default",
              fullscreen=False,
          ),
          my_div(style_div_content, f"{id_page}_content")
]
       


@callback(
        [
         Output(f"{id_page}_content", "children"),
         Output(f"{id_page}_info_loading", "children", allow_duplicate=True),
        ],
        Input("info_button", "n_clicks"),
        State("main_page_store", "data"),
        prevent_initial_call=True,)
def add_data_to_fig(n_clicks, data): 
     
    df = read_json(data["df"])   
    
    stop = df.shape[0]
    columns = list(df.columns)
    list_index = list(range(len(columns)))
    list_non_null = df.isnull().sum()
    list_non_null = [f"{stop - list_non_null[column]} non-null" for column in list_non_null]
    list_dtype = [df[column].dtype for column in columns]
    list_dtypes = dict((i, list_dtype.count(i)) for i in list_dtype)
    maxi = len(max(columns, key=len))
         
    
    texto = "<class 'pandas.core.frame.DataFrame'>" + "\n" +\
            f"RangeIndex: {stop} entries, 0 to {stop - 1}" + "\n" +\
            f"Data Columns (total {len(columns)} columns)" + "\n" +\
            f" #   Column{' '*(maxi - 4)}Non-Null Count  Dtype" + "\n" +\
            f"---  ------{' '*(maxi - 4)}--------------  ----- "         
    for x in zip(list_index, columns, list_non_null, list_dtype):
        texto += "\n" + f" {x[0]}   {x[1]}{' '*(maxi + 2 - len(x[1]))}{x[2]}  {x[3]}"
    
    texto +=  "\n" + f"dtypes: {', '.join([f'{key}({list_dtypes[key]})' for key in  list_dtypes])}" +\
              "\n" + f"memory usage: {df.memory_usage(index=False).sum() / 1000} KB"
    return [my_div({"margin-left": "2%"}, "",
                  html.Pre(texto)), ""]