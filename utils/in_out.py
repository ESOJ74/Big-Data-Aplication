import json

import numpy as np
from pandas import DataFrame, read_csv, read_excel, read_json


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NumpyEncoder, self).default(obj)

def save_panel(fig, name_panel):
    with open(f"figures/{name_panel}.json", "w") as file:
        json.dump(fig.to_dict(), file, cls=NumpyEncoder)


def read_data(extension, path):    
    match extension:
        case "csv" | "txt":
            df = read_csv(path)
        case "json":
            df = read_json(path)
        case "xlsx":
            df = read_excel(path)
        case _:
            df = DataFrame()
    return df.to_json(orient="columns") 


def save_function(data):
    df = read_json(data["prov_df"])
    data["df"] = df.to_json(orient="columns")
    return df