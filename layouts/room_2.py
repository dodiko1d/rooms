import PySimpleGUIQt as sg


layout_room_2 = sg.Column(key='room_2', layout=[
    [sg.Button(key='room_2_light', button_color=('#212121', '#212121'), size_px=(400, 200))],
    [sg.Button('Turn On', key='room_2_turn_on', button_color=('#212121', '#69F0AE')),
     sg.Button('Turn Off', key='room_2_turn_off', button_color=('#212121', '#EF5350'))],
])
