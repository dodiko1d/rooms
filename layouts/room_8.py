import PySimpleGUIQt as sg


layout_room_8 = sg.Column(key='room_8', visible=False, layout=[
    [sg.Button(key='room_8_light', button_color=('#212121', '#212121'), size_px=(400, 200))],
    [sg.Button('Turn On', key='room_8_turn_on', button_color=('#212121', '#69F0AE')),
     sg.Button('Turn Off', key='room_8_turn_off', button_color=('#212121', '#EF5350'))],
])