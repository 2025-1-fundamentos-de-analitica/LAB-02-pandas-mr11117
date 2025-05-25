import pandas as pd

def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    tbl0 = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    return tbl0.shape[1]
print(pregunta_02())
