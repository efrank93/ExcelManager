import PySimpleGUI as sg
from functions import matrix as mx
import pandas as pd


def create_table():
    headings = ['HEADER 1', 'HEADER 2', 'HEADER 3', 'HEADER 4', 'HEADER 5']
    values = [['VALUE 1', 'VALUE 2', 'VALUE 3', 'VALUE 4', 'VALUE 5']]
    layout = [[sg.Table(values=values,
                        headings=headings,
                        auto_size_columns=True,
                        hide_vertical_scroll=True,
                        justification='center',
                        key='-MATRIX-')]]
    return layout


def populate_table(file_list):
    df = mx.read_file_into_matrix(file_list)
    headings = df.columns.tolist()
    data = df.values.tolist()
    layout = [[sg.Table(data, headings=headings, justification='left', key='-TABLE-')], ]

    return layout
