import PySimpleGUIQt as sg


layout_room_changer = sg.Column(key='room_changer', layout=[
    [sg.Button('Room 1', key='room_changer_1', button_color=('#212121', '#69F0AE')),
     sg.Button('Room 2', key='room_changer_2', button_color=('#ffffff', '#212121')),
     sg.Button('Room 3', key='room_changer_3', button_color=('#ffffff', '#212121')),
     ]
])
