# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import getopt
import os
import sys

import pandas as pd


def main(argv):
    opts, args = getopt.getopt(argv, "hd:c:o:", ["idir=", "icolumn=", "odir="])

    for opt, arg in opts:
        if opt == '-h':
            print('main.py -d <inputdirectory> -c <inputcolumn> -o <outputdirectory>')
            sys.exit()
        elif opt in ("-d", "--idir"):
            inputdirectory = arg
            print('Input directory is ', inputdirectory)
        elif opt in ("-c", "--icolumn"):
            inputcolumn = arg
            print('Input column is ', inputcolumn)
        elif opt in ("-o", "--odir"):
            output_dir = arg
            print('Output directory is ', output_dir)

    list_file_path = get_list_file_on_valid_path(inputdirectory)

    if len(list_file_path) > 0:
        df = get_rows_by_column(list_file_path, inputdirectory, inputcolumn)

    create_csv_file(output_dir, df)


def get_list_file_on_valid_path(inputdirectory):
    check_directory = os.path.exists(inputdirectory) and os.path.isdir(inputdirectory)
    if not check_directory:
        raise Exception('Path or file not valid!')

    return os.listdir(inputdirectory)


def get_rows_by_column(list_file_path, inputdirectory, column):
    df = pd.DataFrame()
    for file_path in list_file_path:
        if df.empty:
            df = pd.read_excel(inputdirectory + '/' + file_path)
        else:
            df = pd.concat([df, pd.read_excel(inputdirectory + '/' + file_path)], ignore_index=True)

    # Group by a specific column (e.g., 'Category') and perform an aggregation (e.g., sum)
    return df.groupby([column]).sum()


def create_csv_file(output_dir, df):
    # saving the dataframe
    df.to_csv(output_dir + '/' + 'result.csv')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(sys.argv[1:])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
