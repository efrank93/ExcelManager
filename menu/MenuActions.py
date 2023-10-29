import PySimpleGUI as sg


def menu_sections(theme):
    sg.theme(theme)

    layout = [['&Application', ['&Save', '&Exit']],
              ['&Edit', ['&Sum']],
              ['&Help', ['&About']],
              ['&Settings', ['&Theme']]]

    return layout
