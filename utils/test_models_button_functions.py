from dash import html

id_page = "test_models"

style_test_result = {"font-size": "calc(0.1rem + .8vw)", "color": "white"}


def results_linear_regresion(model, X_train, y_train, X_test, y_test):
    return html.Div(
        [
            html.Div(
                f"coef: {[round(x,4) for x in model.coef_]}", style=style_test_result
            ),
            html.Div(f"rank: {model.rank_}", style=style_test_result),
            html.Div(
                f"singular: {[round(x,4) for x in model.singular_]}",
                style=style_test_result,
            ),
            html.Div(
                f"intercept: {round(model.intercept_, 4)}", style=style_test_result
            ),
            html.Div(f"n_features_in: {model.n_features_in_}", style=style_test_result),
            html.Div(
                f"Score train: {round(model.score(X_train, y_train),3)}",
                style=style_test_result,
            ),
            html.Div(
                f"Score test: {round(model.score(X_test, y_test),3)}",
                style=style_test_result,
            ),
        ],
        style={"position": "relative", "left": "9%", "top": "25%", "width": "90%"},
    )


def results_logistic_regresion(model, X_train, y_train, X_test, y_test):
    return html.Div(
        [
            html.Div(f"Classes: {model.classes_}", style=style_test_result),
            html.Div(
                f"coef: {[round(y,4) for x in model.coef_ for y in x]}",
                style=style_test_result,
            ),
            html.Div(
                f"Independent term: {[round(x,4) for x in model.intercept_]}",
                style=style_test_result,
            ),
            html.Div(f"n_features_in: {model.n_features_in_}", style=style_test_result),
            html.Div(f"n_iter_: {model.n_iter_}", style=style_test_result),
            html.Div(
                f"Score train: {round(model.score(X_train, y_train),3)}",
                style=style_test_result,
            ),
            html.Div(
                f"Score test: {round(model.score(X_test, y_test),3)}",
                style=style_test_result,
            ),
        ],
        style={"position": "relative", "left": "9%", "top": "25%", "width": "90%"},
    )
