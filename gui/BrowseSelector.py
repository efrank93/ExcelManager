import os

import PySimpleGUI as sg

from controller import ConfigManager as cm


def file_selection():
    layout = [
        [sg.Text('Select a single xls/csv file or a folder with this files', size=(40, 3),
                 auto_size_text=True)],
        [sg.In(size=(24, 1), enable_events=True, key="-FILE-", visible=False),
         sg.FilesBrowse("Select a file", size=(15, 1)),
         sg.In(size=(24, 1), enable_events=True, key="-FOLDER-", visible=False),
         sg.FolderBrowse("Select a folder", size=(15, 1))],
        [sg.Listbox(values=[], enable_events=True, size=(40, 15),
                    key="-FILELIST-", pad=((0, 0), (5, 30)),
                    no_scrollbar=True
                    )],
    ]

    return layout


def get_files_from_folder(folder):
    try:
        # Get list of files in folder with abs path
        file_list = abs_file_path(folder)
    except:
        file_list = []

    # check if given files are valid and have one of the following extensions (.csv, .xls, .xlsx)
    extensions = cm.read_config()['extensions']
    valid_file = []
    for file in file_list:
        name, extension = os.path.splitext(file)
        if extension in extensions and os.path.isfile(file):
            valid_file.append(file)

    return valid_file


def add_file_to_list(file_list, file):
    # check if given files are valid and have one of the following extensions (.csv, .xls, .xlsx)
    extensions = cm.read_config()['extensions']
    name, extension = os.path.splitext(file)
    if extension in extensions and os.path.isfile(file):
        file_list.append(file)
    else:
        sg.popup_error('invalid file type')  # Shows red error button

    return file_list


def abs_file_path(directory):
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))
