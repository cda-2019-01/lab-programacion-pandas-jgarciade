##
## Imprima la cantidad de registros por cada letra
## de la columna _c1 de la tabla tbl0
##

import pandas as pd

def main(file_path, sep='\t'):
    file_to_process = pd.read_csv(file_path, sep=sep)
    grouped = file_to_process.groupby('_c1')
    return grouped.size()

if __name__ == "__main__":
    result = main('tbl0.tsv')
    print(result)
