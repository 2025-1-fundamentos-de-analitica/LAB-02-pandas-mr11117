def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna `c1` del
    archivo `tbl0.tsv`?

    Rta/
    c1
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: count, dtype: int64

    """
    import pandas as pd
    tbl0 = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    return tbl0["c1"].value_counts().sort_index()
print(pregunta_03())