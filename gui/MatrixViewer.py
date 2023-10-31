import PySimpleGUI as sg

from controller import ConfigManager as cm
from functions import matrix as mx

COL_HEADINGS = ['HEADER 1', 'HEADER 2', 'HEADER 3', 'HEADER 4', 'HEADER 5']
ROW_VALUES = [['VALUE 1', 'VALUE 2', 'VALUE 3', 'VALUE 4', 'VALUE 5']]


def create_table(key):
    data = cm.read_config()['table']
    font = (data['font-family'], data['font-size'])
    return [[sg.Table(values=ROW_VALUES,
                      headings=COL_HEADINGS,
                      max_col_width=data['max_col_width'],
                      num_rows=data['num_rows'],
                      justification=data['justification'],
                      font=font,
                      alternating_row_color=data['alternating_row_color'],
                      expand_x=data['expand_x'],
                      key=key)]]


def read_file_into_matrix(file_list):
    return mx.read_file_into_matrix(file_list)


def update_headings(table, headings):
    update_title(table, headings)


def update_title(table, headings):
    for cid, text in zip(COL_HEADINGS, headings):
        table.heading(cid, text=text)


def group_by_column(df, column):
    return mx.sum_row_by_column(df, column)


def create_csv(df, output_dir):
    mx.create_csv(df, output_dir)
