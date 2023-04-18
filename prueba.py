"""import openai

# Configuramos las credenciales de API
openai.api_key = "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"

# Definimos nuestro prompt o texto de entrada
prompt = "Hola, ¿cómo estás?"

# Enviamos una solicitud al modelo para obtener una respuesta generada
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=5
)

# Imprimimos la respuesta generada por el modelo
print(response["choices"][0]["text"])"""


"""import seaborn as sns

df = sns.load_dataset('diamonds')
df.to_csv("diamonds.csv", index=False)"""

from sqlalchemy import create_engine
from pandas import read_sql
import psycopg2


"""def conec():
    '''    conn = psycopg2.connect(
        user = "postgres",
        password = "Iruelas2010",
        host = "localhost",
        database = "mi_bd",
        port = 5432
    )'''
    
     
     
    return create_engine("postgresql://postgres:Iruelas2010@localhost:5432/mi_bd")

engine = conec()
query = "select * from usuarios"
df = read_sql(query, conec())
print(df)
engine.dispose()"""


'''cur = conn.cursor()
cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE'")
tabla_nombres = cur.fetchall()

for tabla in tabla_nombres:
    print("---")
    print(tabla[0])

# Cerrar cursor y conexión
cur.close()
conn.close()'''

from sklearn.datasets import load_iris
df = load_iris()
X, y = load_iris(return_X_y=True)




import pandas as pd

df = pd.DataFrame(columns=["sepal length", "sepal width", "petal length", "petal width"])

"""for i, x in enumerate(X):
    print(i, x)
    df[i] = x

df["class"] = y"""

df = pd.DataFrame(X)
df.columns=["sepal length", "sepal width", "petal length", "petal width"]
df["class"] = y

index = df.index
print(index)
start = index.start
stop = index.stop


columns = list(df.columns)
list_index = list(range(len(columns)))
list_non_null = df.isnull().sum()
list_non_null = [f"{stop - list_non_null[column]} non-null" for column in list_non_null]
list_dtype = [df[column].dtype for column in columns]
list_dtypes = dict((i, list_dtype.count(i)) for i in list_dtype)


df.info()

line0 = "<class 'pandas.core.frame.DataFrame'>"
line1 = f"RangeIndex: {stop} entries, {start}, to {stop - 1}"
line2 = f"Data Columns (total {len(columns)} columns)"
max = len(max(columns, key=len))
max_2 = max + 3

print('------------------------------------')
print(line0)
print(line1)
print(line2)
print(f" #   Column{' '*(max - 4)}Non-Null Count  Dtype")
print(f"---  ------{' '*(max - 4)}--------------  ----- ")
for x in zip(list_index, columns, list_non_null, list_dtype):
    print(f" {x[0]}  {x[1]}{' '*(max_2 - len(x[1]))}{x[2]}    {x[3]}")

print(f"dtypes: {' '.join([f'{key}({list_dtypes[key]})' for key in  list_dtypes])}")
print(f"memory usage: {df.memory_usage(index=False).sum() / 1000} KB")