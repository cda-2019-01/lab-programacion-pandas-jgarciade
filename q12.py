##
## Si la columna _c0 es la clave en las tablas tbl0.tsv
## y tbl2.tsv, compute la suma de tbl2._c5b por cada
## valor en tbl0._c1.
##

import pandas as pd


def main(file_path, sep='\t'):
    file_to_process = pd.read_csv(file_path, sep=sep)
    result = file_to_process.groupby('_c5a')['_c5b'].sum()

    return result


if __name__ == "__main__":
    result = main('tbl2.tsv')
    print(result)
