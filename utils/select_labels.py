def select_labels(df, axis, groupby=False):

    res = df.index
    if axis:
        res = df.columns

    if groupby:
        res = df.columns
        if axis:
            res = df.index  
    return res 