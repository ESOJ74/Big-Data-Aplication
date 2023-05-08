import base64
import io

from pandas import read_csv, read_excel


def parse_contents(contents, filename, data):
    _, content_string = contents.split(",")

    decoded = base64.b64decode(content_string)
    try:
        if "csv" in filename:
            # Assume that the user uploaded a CSV file
            df = read_csv(io.StringIO(decoded.decode("utf-8")))
        elif "xls" in filename:
            # Assume that the user uploaded an excel file
            df = read_excel(io.BytesIO(decoded))
        df.to_csv(f"""users/{data["user"]}/data/{filename}""")
    except Exception as e:
        return "There was an error processing this file."
    return "Archivo guardado"
