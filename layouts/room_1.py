import PySimpleGUIQt as sg


layout_room_1 = sg.Column(key='room_1', layout=[
    [sg.Button(key='room_1_light', button_color=('#212121', '#212121'), size_px=(400, 200))],
    [sg.Button('Turn On', key='room_1_turn_on', button_color=('#212121', '#69F0AE')),
     sg.Button('Turn Off', key='room_1_turn_off', button_color=('#212121', '#EF5350'))],
])
