##
## Agregue una columna  con la suma de _c0 y _c2 a la tabla tbl0.tsv
##

import pandas as pd

def main(file_path, sep='\t'):
    file_to_process = pd.read_csv(file_path, sep=sep)
    file_to_process['suma'] = file_to_process['_c0'] + file_to_process['_c2']
    return file_to_process

if __name__ == "__main__":
    result = main('tbl0.tsv')
    print(result)
