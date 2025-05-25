def pregunta_05():
    """
    Calcule el valor máximo de `c2` por cada letra en la columna `c1` del
    archivo `tbl0.tsv`.

    Rta/
    c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: c2, dtype: int64
    """
    import pandas as pd
    tbl0 = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    return tbl0.groupby("c1")["c2"].max()
print(pregunta_05())