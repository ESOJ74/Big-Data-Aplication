import pandas as pd
df = pd.read_csv("price.csv")
df.drop(['carat'], axis=1)
df.groupby(['color'], axis=0).sum()
