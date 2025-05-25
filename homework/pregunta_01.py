
import pandas as pd

def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    tbl0 = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    return tbl0.shape[0]
print(pregunta_01())
