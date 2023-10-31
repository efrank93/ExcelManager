import PySimpleGUI as sg

from gui import BrowseSelector as bs
from gui import MainWindow as mw
from gui import MatrixViewer as mv
from menu import ThemeDisplay as td


def main_window_events(window):
    global df, df_sum
    while True:
        event, values = window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break
        # Folder name was filled in, make a list of files in the folder
        elif event == '-FOLDER-':
            window['-FILELIST-'].update(bs.get_files_from_folder(values['-FOLDER-']))
        elif event == '-FILE-':
            window['-FILELIST-'].update(bs.add_file_to_list(window['-FILELIST-'].Values, values['-FILE-']))
        elif event == 'Theme':
            window.close()
            window = mw.create_window()
        elif event == '-READFILE-':
            file_list = window['-FILELIST-'].Values
            df = mv.read_file_into_matrix(file_list)
            headings = df.columns.tolist()
            values = df.values.tolist()
            mv.update_headings(window['-MATRIXALL-'].Widget, headings)
            mv.update_headings(window['-MATRIXRESULT-'].Widget, headings)
            window['-MATRIXALL-'].update(values=values)
        elif event == '-GROUPBYCOL-':
            column = sg.popup_get_text('Column', 'Please insert column to apply group by and sum')
            file_list = window['-FILELIST-'].Values
            df = mv.read_file_into_matrix(file_list)
            df_sum = mv.group_by_column(df, column)
            window['-MATRIXRESULT-'].update(values=df_sum.values.tolist())
        elif event == '-EXPORTCSV-':
            output_dir = sg.popup_get_folder('Enter csv output directory')
            mv.create_csv(df_sum, output_dir)

