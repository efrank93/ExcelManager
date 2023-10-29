import pandas as pd


def read_file_into_matrix(list_file_path):

    df = pd.DataFrame()
    for file_path in list_file_path:
        if df.empty:
            df = pd.read_excel(file_path)
        else:
            df = pd.concat([df, pd.read_excel(file_path)], ignore_index=True)

    print(df)

    return df


def sum_row_by_column(list_file_path):
    df = pd.DataFrame()
    for file_path in list_file_path:
        if df.empty:
            df = pd.read_excel(file_path)
        else:
            df = pd.concat([df, pd.read_excel(file_path)], ignore_index=True)

    print(df)

    # Group by a specific column (e.g., 'Category') and perform an aggregation (e.g., sum)
    df2 = df.groupby(['A']).sum()
    print(df2)

    return df2
