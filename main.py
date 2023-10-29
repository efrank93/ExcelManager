# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import PySimpleGUI as sg
from gui import MainWindow as mw
from controller import MainEvents as me


def main():
    sg.theme('Dark')
    window = mw.create_window(sg.theme())
    me.main_window_events(window)

    window.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
