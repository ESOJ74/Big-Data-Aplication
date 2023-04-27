from dash import Input, Output, State, callback, html
from pandas import read_json

from common_functions.create_functions_layout import create_functions_layout
from my_dash.my_html.my_div import my_div

style_div_content ={    
    "height": "80%",
    "width": "50%",
    "background": "#acf4ed"
}

style_div_title = {
    "text-align": "center",
    "background": "radial-gradient(circle farthest-side at bottom left, #347eb7 0%, #204765 30%, #04212c 95%)"
}

style_title = {
    "font-weight": "bold",
    "color": "#acf4ed"
}

style_div_obj = {
    "margin-left": "5%",
    "width": "95%",
    "height": "87%",
    
}

id_page = "info"

layout = create_functions_layout(id_page)

@callback(
        [
         Output(f"{id_page}_content", "children"),
         Output(f"{id_page}_loading", "children", allow_duplicate=True),
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
    return [
            my_div(style_div_content, "",
                   [
                    my_div(style_div_title, "",
                           [
                            html.H5("DataFrame.info()",
                                   style=style_title),
                            html.A("Documentacion",  href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html",
                                   target="_blank", style={"overflow": "auto"})
                           ],
                    ),
                    my_div(style_div_obj, "", html.Pre(texto, style={'width': '100%', 'height': '100%'})),
                   ],
            ), ""]
