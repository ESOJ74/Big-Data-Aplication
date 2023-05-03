from dash import html

from assets.common_css import *
from assets.my_dash.my_html.my_div import my_div

from ..common_css import *

id_page = "test_models"


def pred_model(model, X_test):
    return model.predict(X_test)


def results_linear_regresion(model, X_train, y_train, X_test, y_test):
        return my_div(style_div_test_result, "",
                      [
                       html.P(f"coef: {[round(x,4) for x in model.coef_]}",
                            style=style_test_result),
                       html.P(f"rank: {model.rank_}",
                            style=style_test_result),   
                       html.P(f"singular: {[round(x,4) for x in model.singular_]}",
                            style=style_test_result),
                       html.P(f"intercept: {round(model.intercept_, 4)}",
                            style=style_test_result),
                       html.P(f"n_features_in: {model.n_features_in_}",
                            style=style_test_result),                       
                       html.P(f"Score train: {round(model.score(X_train, y_train),3)}",
                              style=style_test_result),
                       html.P(f"Score test: {round(model.score(X_test, y_test),3)}",
                              style=style_test_result),
                      ])


def results_logistic_regresion(model, X_train, y_train, X_test, y_test):     
        return my_div(style_div_test_result, "",
                    [
                    html.P(f"Classes: {model.classes_}",
                            style=style_test_result),
                    html.P(f"coef: {[round(y,4) for x in model.coef_ for y in x]}",
                            style=style_test_result),
                    html.P(f"Independent term: {[round(x,4) for x in model.intercept_]}",
                            style=style_test_result),
                    html.P(f"n_features_in: {model.n_features_in_}",
                            style=style_test_result),
                    html.P(f"n_iter_: {model.n_iter_}",
                            style=style_test_result),
                    html.P(f"Score train: {round(model.score(X_train, y_train),3)}",
                            style=style_test_result),
                    html.P(f"Score test: {round(model.score(X_test, y_test),3)}",
                            style=style_test_result),
                    ]) 