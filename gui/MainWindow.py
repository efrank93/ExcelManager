import PySimpleGUI as sg

from gui import BrowseSelector as bs
from gui import MatrixViewer as mv

file_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABU0lEQVQ4y52TzStEURiHn' \
            b'/ecc6XG54JSdlMkNhYWsiILS0lsJaUsLW2Mv8CfIDtr2VtbY4GUEvmIZnKbZsY977Uwt2HcyW1+dTZvt6fn9557BGB' \
            b'+aaNQKBR2ifkbgWR+cX13ubO1svz++niVTA1ArDHDg91UahHFsMxbKWycYsjze4muTsP64vT43v7hSf/A0FgdjQPQWAmco68nB+T' \
            b'+SFSqNUQgcIbN1bn8Z3RwvL22MAvcu8TACFgrpMVZ4aUYcn77BMDkxGgemAGOHIBXxRjBWZMKoCPA2h6qEUSRR2MF6GxUUMUaIUgBCNTnAcm3H2G5YQfgvccYIXAtDH7FoKq/AaqKlbrBj2trFVXfBPAea4SOIIsBeN9kkCwxsNkAqRWy7+B7Z00G3xVc2wZeMSI4S7sVYkSk5Z/4PyBWROqvox3A28PN2cjUwinQC9QyckKALxj4kv2auK0xAAAAAElFTkSuQmCC '

treeData = sg.TreeData()


def create_window(theme):
    if not theme:
        theme = sg.OFFICIAL_PYSIMPLEGUI_THEME
    sg.theme(theme)

    # layout = [[sg.Menu(ma.menu_sections(), key='-MENU-')]]

    layout = [[
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

    window = sg.Window("Excel Manager", layout, size=(1000, 550), resizable=True).Finalize()

    return window
