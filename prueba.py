from dash import Dash, dcc, html, Input, Output
from sklearn.model_selection import train_test_split
from sklearn import linear_model, tree, neighbors
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

app = Dash(__name__)

models = {'Regression': linear_model.LinearRegression,
          'Decision Tree': tree.DecisionTreeRegressor,
          'k-NN': neighbors.KNeighborsRegressor}

app.layout = html.Div([
    html.H4("Predicting restaurant's revenue"),
    html.P("Select model:"),
    dcc.Dropdown(
        id='dropdown',
        options=["Regression", "Decision Tree", "k-NN"],
        value='Regression',
        clearable=False
    ),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"), 
    Input('dropdown', "value"))
def train_and_display(name):
    df = px.data.tips() # replace with your own data source
    X = df.total_bill.values[:, None]
    X_train, X_test, y_train, y_test = train_test_split(
        X, df.tip, test_size=0.2, random_state=42)
    
    model = models[name]()
    model.fit(X_train, y_train)

    x_range_train = np.linspace(0, X_train.shape[0])    
    pred_train = model.predict(X_train.reshape(-1, 1))
    x_range_test = np.linspace(0, X_test.shape[0])    
    pred_test = model.predict(X_test.reshape(-1, 1))
    
    fig = go.Figure([
        go.Scatter(x=x_range_train, y=y_train, 
                   name='train', mode='markers'),
        go.Scatter(x=x_range_train, y=pred_train, 
                   name='pred_train'),
        go.Scatter(x=x_range_test, y=y_test, 
                   name='test', mode='markers'),
        go.Scatter(x=x_range_test, y=pred_test, 
                   name='pred_test')
    ])
    
    return fig

app.run_server(debug=True)