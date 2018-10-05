from enum import Enum
class DIRECTION(Enum):
    UP = 'u'
    DOWN = 'd'
    LEFT = 'l'
    RIGHT =  'r'


class Move:
    def __init__(self, id, direction):
        self.id = id
        self.dir = direction
    
    def __str__(self):
        return "ID: " + str(self.id) + ", Dir: " + str(self.dir.name)
