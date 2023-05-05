import pandas as pd

df = pd.read_csv("price.csv")
df.drop(["carat"], axis=1)
df.drop(["cut"], axis=1)
df.drop(["depth", "table"], axis=1)
