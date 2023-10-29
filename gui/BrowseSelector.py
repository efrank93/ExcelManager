import PySimpleGUI as sg
import os


def file_selection():

    layout = [
        [sg.Text('Select a single xls/csv file or a folder with this files', size=(40, 3),
                 auto_size_text=True)],
        [sg.In(size=(24, 1), enable_events=True, key="-FILE-"), sg.FilesBrowse("Select a file", size=(15, 1))],
        [sg.In(size=(24, 1), enable_events=True, key="-FOLDER-"),
         sg.FolderBrowse("Select a forlder", size=(15, 1))],
        [sg.Listbox(values=[], enable_events=True, size=(42, 15), key="-FILE LIST-", pad=((0, 0), (5, 30)))],
    ]

    return layout


def get_files_from_folder(folder):
    try:
        # Get list of files in folder with abs path
        file_list = abs_file_path(folder)
    except:
        file_list = []

    # check if given files are valid and have one of the following extensions (.csv, .xls, .xlsx)
    filenames = [
        f
        for f in file_list
        if os.path.isfile(f) and (
                f.lower().endswith('.xlsx') or
                f.lower().endswith('.xls') or
                f.lower().endswith('.csv'))
    ]

    return filenames


def add_file_to_list(file_list, file):
    if os.path.isfile(file) and (
            file.lower().endswith('.xlsx') or
            file.lower().endswith('.xls') or
            file.lower().endswith('.csv')):
        file_list.append(file)
    else:
        sg.popup_error('invalid file type')  # Shows red error button

    return file_list


def abs_file_path(directory):
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))
