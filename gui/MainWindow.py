import PySimpleGUI as sg

from controller import ConfigManager as cm
from gui import BrowseSelector as bs
from gui import MatrixViewer as mv
from menu import MenuActions as ma


def create_window():
    data = cm.read_config()
    theme = data['theme']['color']
    if not theme:
        theme = sg.OFFICIAL_PYSIMPLEGUI_THEME
    sg.theme(theme)

    layout = [[sg.Menu(ma.menu_sections(), key='-MENU-')]]

    layout += [[
        mv.create_table('-MATRIXALL-'),
        mv.create_table('-MATRIXRESULT-'),
    ]]

    layout += [
        [
            sg.Column(bs.file_selection(), vertical_alignment='top'),
            sg.Button('Read file', key='-READFILE-'),
            sg.Button('Group values', key='-GROUPBYCOL-'),
            sg.Button('Export result', key='-EXPORTCSV-')
        ]
    ]
    main_window = data['main-window']
    size = (main_window['width'], main_window['height'])
    window = sg.Window(main_window['title'], layout, size=size, resizable=main_window['resizable']).Finalize()

    return window
