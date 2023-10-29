import json
import os

import PySimpleGUI as sg
from gui import BrowseSelector as bs
from menu import ThemeDisplay as td
from gui import MainWindow as mw


def main_window_events(window):
    while True:
        event, values = window.read()
        print('Event', event)
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        # Folder name was filled in, make a list of files in the folder
        elif event == "-FOLDER-":
            window["-FILE LIST-"].update(bs.get_files_from_folder(values["-FOLDER-"]))
        elif event == "-FILE-":
            window["-FILE LIST-"].update(bs.add_file_to_list(window["-FILE LIST-"].Values, values["-FILE-"]))
        elif event == "Theme":
            print("[LOG] Clicked About!")
            theme = td.theme_main()
            window.close()
            window = mw.create_window(theme)
