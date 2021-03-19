import PySimpleGUIQt as sg


layout_room_5 = sg.Column(key='room_5', visible=False, layout=[
    [sg.Button(key='room_5_light', button_color=('#212121', '#212121'), size_px=(400, 200))],
    [sg.Button('Turn On', key='room_5_turn_on', button_color=('#212121', '#69F0AE')),
     sg.Button('Turn Off', key='room_5_turn_off', button_color=('#212121', '#EF5350'))],
])
