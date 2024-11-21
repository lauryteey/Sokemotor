import PySimpleGUI as gui

# All the stuff inside your window.
layout = [  [gui.Text("What's your name?")],
            [gui.InputText()],
            [gui.Button('Ok'), gui.Button('Cancel')] ]

# Create the Window
window = gui.Window('Hello Example', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    # if user closes window or clicks cancel
    if event == gui.WIN_CLOSED or event == 'Cancel':
        break

    print('Hello', values[0], '!')

window.close()