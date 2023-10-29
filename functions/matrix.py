import pandas as pd
import os.path


def sum_row_by_column():
    # Replace 'your_file.xlsx' with the path to your Excel file
    dir_path = '/home/dev/Desktop/file_excel'

    check_file = os.path.exists(dir_path) and os.path.isdir(dir_path)
    if not check_file:
        raise Exception('Path or file not valid!')

    list_file_path = os.listdir(dir_path)

    df = pd.DataFrame()
    for file_path in list_file_path:
        if df.empty:
            df = pd.read_excel(dir_path + '/' + file_path)
        else:
            df = pd.concat([df, pd.read_excel(dir_path + '/' + file_path)], ignore_index=True)

    print(df)

    # Group by a specific column (e.g., 'Category') and perform an aggregation (e.g., sum)
    df2 = df.groupby(['A']).sum()
    print(df2)

    return df2
