import dash_table

def my_dash_table(df):
    return dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'name': col, 'id': col} for col in df.columns],
)