from pandas import read_json


def save_function(data):
    df = read_json(data["prov_df"])
    data["df"] = df.to_json(orient="columns")
    return df