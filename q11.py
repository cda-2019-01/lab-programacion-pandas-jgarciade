##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c5a
## y _c5b (unidos por ':') de la tabla tbl2.tsv
##

import pandas as pd


def main(file_path, sep='\t'):
    file_to_process = pd.read_csv(file_path, sep=sep)
    file_to_process['lista'] = file_to_process['_c5a'] + ':' + file_to_process['_c5b'].astype('str')
    grouped_list = file_to_process.groupby('_c0')['lista'].apply(list)

    df = pd.DataFrame()
    df['_c0'] = grouped_list.keys()
    df['lista'] = [val for val in grouped_list]
    df['lista'] = [','.join(str(v) for v in sorted(x)) for x in df['lista']]

    return df


if __name__ == "__main__":
    result = main('tbl2.tsv')
    print(result)
