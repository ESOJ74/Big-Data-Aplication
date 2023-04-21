
from pandas import DataFrame, read_csv, read_excel, read_json


def read_data(extension, path):    
    '''match extension:
        case "csv" | "txt":
            df = read_csv(path)
        case "json":
            df = read_json(path)
        case "xlsx":
            df = read_excel(path)
        case _:
            df = DataFrame()'''
    df=read_csv(path)
    return df.to_json(orient="columns")   
