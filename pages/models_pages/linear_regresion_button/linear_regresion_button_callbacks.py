from dash import callback, dcc
from dash.dependencies import Input, Output, State
from pandas import read_json
from my_dash.my_dcc.my_dropdown import my_dropdown
from my_dash.my_dbc.my_button import my_button
from my_dash.my_html.my_div import my_div
import plotly.express as px
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd



s_selector = {
    "float" : "left",
    "position": "relative",
    "top": "20%",
    "left": "2.4%",
    "width": "17.5%",
    "height": "48%",
    "border-radius": "7px 7px 5px 5px",
    "padding": "2px 2px 0px 2px",
    "font-size": "1em",
    "background": "#699B8F",
}

s_selector2 = {
    "float" : "left",
    "position": "relative",
    "top": "20%",
    "margin-left": "5%",
    "width": "17.5%",
    "height": "48%",
    "border-radius": "7px 7px 5px 5px",
    "padding": "2px 2px 0px 2px",
    "font-size": "1em",
    "background": "#699B8F",
}

s_content_down = {
    "position": "relative",    
    "top": "5%",
    "left": "2.4%",
    "width": "30%",
    "background": "white",
}

s_utils = {
    "position": "relative",    
    "top": "2%",
    "left": "5%",
    "width": "100%",
    "height": "100%",
}

style_input = {
    "font-family": "Roboto, Helvetica, Arial, sans-serif",
    "width": "10%"
}


id_page = "linear_regresion_button"


@callback(Output(f"{id_page}_content_up", "children"),
          Input("linear_regresion_button", "n_clicks"),
          State('main_page_store', 'data'),
          prevent_initial_call=True)
def display_page(n_clicks, data):          
     
    columns = read_json(data["df"]).columns
    
    obj = my_div({"width": "100%", "height": "100%"}, "",
                 [my_div({"position": "relative", "top": "2%", "width": "100%", "height": "7%"}, "",
                         [
                          my_div({"float": "left", "margin-left": "3%", "width": "20%", "height": "100%"}, "", "X"),
                          my_div({"float": "left", "width": "30%", "height": "100%"}, "", "Y"),
                         ]
                  ),
                  my_div(s_selector, "",
                         my_dropdown(f"{id_page}_dropdown_x",
                              {},
                              columns,
                              placeholder="Seleccione columna",
                              multi=True,
                         ),
                  ),
                  my_div(s_selector2, "",
                         my_dropdown(f"{id_page}_dropdown_y",
                              {},
                              placeholder="Seleccione columna"
                         ),
                  ),
                 ]
          )
    return obj


@callback(Output(f"{id_page}_dropdown_y", "options"),
          Input(f"{id_page}_dropdown_x", "value"),
          State('main_page_store', 'data'),
          prevent_initial_call=True)
def display_page(values, data):
    cols = []
    if values is not None:
        cols = list(read_json(data["df"]).columns)
        for value in values:
            cols.remove(value)    
    return cols


@callback(Output(f"{id_page}_content_down", "children"),
          Input(f"{id_page}_dropdown_y", "value"),
          [
           State(f"{id_page}_dropdown_x", "value"),
           State('main_page_store', 'data'),
          ],
          prevent_initial_call=True)
def display_page(value_y, value_x, data):
     
    
    try:
        df = read_json(data["df"])

        if len(value_x) == 1:

            dataX =df[[value_x[0]]]
            X_train = np.array(dataX)
            y_train = df[value_y].values    
            
            # Creamos el objeto de Regresión Linear
            regr = linear_model.LinearRegression()
    
            # Entrenamos nuestro modelo
            regr.fit(X_train, y_train)

            # Hacemos las predicciones que en definitiva una línea (en este caso, al ser 2D)
            y_pred = regr.predict(X_train)

            obj = f"Coefficients: \n {regr.coef_}"
            # Veamos los coeficienetes obtenidos, En nuestro caso, serán la Tangente
            print('Coefficients: \n', regr.coef_)
            # Este es el valor donde corta el eje Y (en X=0)
            print('Independent term: \n', regr.intercept_)
            # Error Cuadrado Medio
            print("Mean squared error: %.2f" % mean_squared_error(y_train, y_pred))
            # Puntaje de Varianza. El mejor puntaje es un 1.0
            print('Variance score: %.2f' % r2_score(y_train, y_pred))
        else:
            dataX2 =  pd.DataFrame()
            for x in value_x:
                dataX2[x] = df[x].fillna(0)
             
            XY_train = np.array(dataX2)
            z_train = df[value_y].values

            # Creamos un nuevo objeto de Regresión Lineal
            regr2 = linear_model.LinearRegression()
            
            # Entrenamos el modelo, esta vez, con 2 dimensiones
            # obtendremos 2 coeficientes, para graficar un plano
            regr2.fit(XY_train, z_train)
            
            # Hacemos la predicción con la que tendremos puntos sobre el plano hallado
            z_pred = regr2.predict(XY_train)
            
            # Los coeficientes
            print('Coefficients: \n', regr2.coef_)
            # Error cuadrático medio
            print("Mean squared error: %.2f" % mean_squared_error(z_train, z_pred))
            # Evaluamos el puntaje de varianza (siendo 1.0 el mejor posible)
            print('Variance score: %.2f' % r2_score(z_train, z_pred))

            obj = f"Coefficients: \n {regr2.coef_}"
    except KeyError:
        obj = ""
    return obj

