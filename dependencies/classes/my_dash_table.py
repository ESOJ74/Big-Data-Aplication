from dash import dash_table


class MyDashTable:
    """
    Clase que define métodos para crear tablas interactivas con Dash.

    """

    @staticmethod
    def my_dash_table(
        df,
        style_table,
        style_data,
        style_header,
        style_cell,
        style_data_conditional=None,
        page_size=15,
    ):
        """
        Crea una tabla interactiva con los datos proporcionados.

        Args:
            df (pd.DataFrame): DataFrame con los datos de la tabla.
            style_table (dict): Estilos CSS para la tabla.
            style_data (dict): Estilos CSS para los datos de la tabla.
            style_header (dict): Estilos CSS para el encabezado de la tabla.
            style_cell (dict): Estilos CSS para las celdas de la tabla.

        Returns:
            dash_table.DataTable: Tabla interactiva.

        """
        if style_data_conditional is None:
            style_data_conditional = []
        return dash_table.DataTable(
            data=df.to_dict("records"),
            columns=[{"name": col, "id": col} for col in df.columns],
            page_size=page_size,
            selected_rows=[],
            style_table=style_table,
            style_data=style_data,
            style_header={
                "position": "sticky",
                "top": "0",
                "zIndex": "1",
                "textOverflow": "ellipsis",
                "overflow": "hidden",
                "whiteSpace": "nowrap",
            }
            | style_header,
            style_cell=style_cell,
            style_data_conditional=style_data_conditional,
            fixed_rows={"data": 0},
        )

    @staticmethod
    def my_dash_table_groupby(
        df,
        columns_grouped,
        style_table,
        style_data,
        style_header,
        style_cell,
        style_data_conditional=None,
    ):
        """
        Crea una tabla interactiva con datos agrupados según las columnas especificadas.

        Args:
            df (pd.DataFrame): DataFrame con los datos de la tabla.
            columns_grouped (int): Número de columnas a agrupar.
            style_table (dict): Estilos CSS para la tabla.
            style_data (dict): Estilos CSS para los datos de la tabla.
            style_header (dict): Estilos CSS para el encabezado de la tabla.
            style_cell (dict): Estilos CSS para las celdas de la tabla.

        Returns:
            dash_table.DataTable: Tabla interactiva con datos agrupados.

        """
        if style_data_conditional is None:
            style_data_conditional = []
        columns = [
            {"name": ["", col], "id": col} for col in df.columns[:columns_grouped]
        ]
        columns += [
            {"name": [col, ""], "id": col} for col in df.columns[columns_grouped:]
        ]

        return dash_table.DataTable(
            data=df.to_dict("records"),
            columns=columns,
            page_size=15,
            selected_rows=[],
            style_table=style_table,
            style_data=style_data,
            style_header=style_header,
            style_data_conditional=style_data_conditional,
            style_cell=style_cell,
            merge_duplicate_headers=True,
        )
