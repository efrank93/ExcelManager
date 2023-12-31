import PySimpleGUI as sg

from controller import ConfigManager as cm


# Retrieve selected theme by user

def get_theme():
    """
    Get the theme to use for the program
    Value is in this program's user settings. If none set, then use PySimpleGUI's global default theme
    :return: The theme
    :rtype: str
    """
    # First get the current global theme for PySimpleGUI to use if none has been set for this program
    try:
        global_theme = sg.theme_global()
    except:
        global_theme = sg.theme()
    # Get theme from user settings for this program.  Use global theme if no entry found
    user_theme = sg.user_settings_get_entry('-THEME-', '')
    if user_theme == '':
        user_theme = global_theme
    return user_theme


def theme_window():
    theme_layout = [[sg.Text("See how elements look under different themes by choosing a different theme here!")],
                    [sg.Listbox(values=sg.theme_list(),
                                size=(20, 12),
                                key='-THEMELISTBOX-',
                                enable_events=True)],
                    [sg.Button("Set Theme")]]

    return sg.Window("Theme Manager", theme_layout, size=(500, 350), resizable=True).Finalize()


def get_theme_from_config():
    theme_color = cm.read_config()['theme']['color']
    return theme_color


def set_theme_in_config(theme):
    data = cm.read_config()
    data['theme']['color'] = theme
    cm.write_config(data)


def theme_main():
    window = theme_window()
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "Set Theme":
            theme_chosen = values['-THEMELISTBOX-'][0]
            set_theme_in_config(theme_chosen)
            window.close()
            return theme_chosen
