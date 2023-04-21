
from pandas import DataFrame, read_csv, read_excel, read_json


def read_data(extension, path):    
    
    df=read_csv(path)
    return df.to_json(orient="columns")   
