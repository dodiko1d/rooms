import PySimpleGUIQt as sg
from layouts import layout_main


window = sg.Window('Window Title', layout_main)


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    for index in range(1, 4):
        if event == f'room_changer_{index}':
            window[f'room_{index}'].update(visible=True)
            window[f'room_changer_{index}'].update(button_color=('#212121', '#69F0AE'))
            for other_index in list({1, 2, 3} - {index}):
                window[f'room_{other_index}'].update(visible=False)
                window[f'room_changer_{other_index}'].update(button_color=('#ffffff', '#212121'))
        if event




