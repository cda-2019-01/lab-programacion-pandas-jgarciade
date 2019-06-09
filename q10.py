##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c4
## de la tabla tbl1.tsv
##

import pandas as pd


def main(file_path, sep='\t'):
    file_to_process = pd.read_csv(file_path, sep=sep)
    grouped_list = file_to_process.groupby('_c0')['_c4'].apply(list)
    df = pd.DataFrame()
    df['_c0'] = grouped_list.keys()
    df['lista'] = [val for val in grouped_list]
    df['lista'] = [",".join(str(v) for v in sorted(x)) for x in df['lista']]

    return df


if __name__ == "__main__":
    result = main('tbl1.tsv')
    print(result)
