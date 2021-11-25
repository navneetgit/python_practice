from enum import Enum

class light(Enum):
    RED = 0
    GREEN = 1


class light:
    _state = RED

def set_color(color):
    _state = color
    