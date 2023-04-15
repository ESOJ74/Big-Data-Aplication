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



import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Login'),
    html.Div([
        html.Label('Username:'),
        dcc.Input(
            placeholder='Enter your username',
            type='text',
            value=''
        ),
        html.Label('Password:'),
        dcc.Input(
            placeholder='Enter your password',
            type='password',
            value=''
        ),
        html.Button('Submit', id='button'),
        html.Div(id='output-state'),
        html.Br(),
        html.A('Register', href='/register')
    ])
])

@app.callback(
    dash.dependencies.Output('output-state', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('username', 'value'),
     dash.dependencies.State('password', 'value')])
def update_output(n_clicks, username, password):
    if n_clicks is not None:
        if username == 'admin' and password == 'password':
            return 'Logged in successfully!'
        else:
            return 'Invalid login credentials.'

if __name__ == '__main__':
    app.run_server(debug=True)