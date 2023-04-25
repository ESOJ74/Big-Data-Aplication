import dash_ag_grid as dag


def create_adgrid(id, df):
    
    dashGridOptions={"pagination": False}
    match df.shape[0]:
        case 1|2|3|4:            
            style={"height": 250}
        case 5:
            style={"height": 280}
        case 6|7|8|9:
            style={"height": 500}
        case _:
            style={"height": 550}
            dashGridOptions={"pagination": True}

    return dag.AgGrid(
                      id=id,
                      className="ag-theme-alpine-dark",
                      columnDefs=[{"headerName": x, "field": x}
                                  for x in df.columns],
                      rowData=df.to_dict("records"),
                      columnSize="sizeToFit",
                      dashGridOptions=dashGridOptions,
                      style=style,
           )