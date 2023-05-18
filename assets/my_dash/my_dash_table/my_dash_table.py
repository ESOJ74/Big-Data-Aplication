from dash import dash_table
from .my_dash_table_css import *




def my_dash_table(
    df,
    style_table=style_table,
    style_data=style_data,
    style_header=style_header,
    style_cell=style_cell,
):
    return dash_table.DataTable(
        data=df.to_dict("records"),
        columns=[{"name": col, "id": col} for col in df.columns],
        page_size=15,
        selected_rows=[],
        style_table=style_table,
        style_data=style_data,
        style_header=style_header,
        style_cell=style_cell,
    )

def my_dash_table_groupby(    
    df,
    columns_grouped,
    style_table=style_table,
    style_data=style_data,
    style_header=style_header,
    style_cell=style_cell,
):
    columns = [{"name": ["", col], "id": col} for col in df.columns[0:columns_grouped]]
    columns += [{"name": [col, ""], "id": col} for col in df.columns[columns_grouped:]]
    
    return dash_table.DataTable(
        data=df.to_dict("records"),
        columns=columns,
        page_size=15,
        selected_rows=[],
        style_table=style_table,
        style_data=style_data,
        style_header=style_header,
        style_cell=style_cell,
        merge_duplicate_headers=True
    )
