##
## Imprima la suma de la _c2 por cada letra de la _c1
## de la tabla tbl0
##

import pandas as pd

def main(file_path, sep='\t'):
    file_to_process = pd.read_csv(file_path, sep=sep)
    return file_to_process.groupby('_c1').sum()['_c2']

if __name__ == "__main__":
    result = main('tbl0.tsv')
    print(result)
