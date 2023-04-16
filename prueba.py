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


def conec():
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
engine.dispose()


'''cur = conn.cursor()
cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE'")
tabla_nombres = cur.fetchall()

for tabla in tabla_nombres:
    print("---")
    print(tabla[0])

# Cerrar cursor y conexión
cur.close()
conn.close()'''