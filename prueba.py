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



import tkinter as tk
from tkinter import filedialog



archivo = filedialog.askopenfilename()
