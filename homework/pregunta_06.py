def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    import pandas as pd
    tbl1 = pd.read_csv("files/input/tbl1.tsv", sep="\t")
    return sorted(tbl1["c4"].str.upper().unique())
print(pregunta_06())
