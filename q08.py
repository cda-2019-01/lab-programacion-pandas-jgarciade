##
## Agregue el año como una columna a la tabla tbl0.tsv
##

import pandas as pd

def main(file_path, sep='\t'):
    file_to_process = pd.read_csv(file_path, sep=sep)
    file_to_process['ano'] = file_to_process['_c3'].map(lambda x:x.split('-')[0])
    return file_to_process

if __name__ == "__main__":
    result = main('tbl0.tsv')
    print(result)
