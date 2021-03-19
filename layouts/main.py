import PySimpleGUIQt as sg
from .room_1 import layout_room_1
from .room_2 import layout_room_2
from .room_3 import layout_room_3
from .room_5 import layout_room_5
from .room_8 import layout_room_8
from .room_changer import layout_room_changer


layout_main = [
    [layout_room_1],
    [layout_room_2],
    [layout_room_3],
    [layout_room_5],
    [layout_room_8],
    [layout_room_changer]
]
