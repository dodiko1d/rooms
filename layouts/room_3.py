import PySimpleGUIQt as sg


layout_room_3 = sg.Column(key='room_3', layout=[
    [sg.Button(key='room_3_light', button_color=('#212121', '#212121'), size_px=(400, 200))],
    [sg.Button('Turn On', key='room_3_turn_on', button_color=('#212121', '#69F0AE')),
     sg.Button('Turn Off', key='room_3_turn_off', button_color=('#212121', '#EF5350'))],
])
