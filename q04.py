##
## Imprima los valores unicos e la columna _c4 de
## de la tabla tbl1 en mayusculas
##


import pandas as pd

def main(file_path, sep='\t'):
    file_to_process = pd.read_csv(file_path, sep=sep)
    values = file_to_process['_c4']
    values = values.map(lambda x:x.upper())
    unique_values = values.unique()
    unique_values.sort()
    return unique_values

if __name__ == "__main__":
    result = main('tbl1.tsv')
    print(result)
