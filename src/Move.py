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
        return "(" + str(self.id) + "," + str(self.dir.name) + ")"

    def __repr__(self):
        return repr((self.id, self.dir.name))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            # print("SELF: " + str(self))
            return (self.id == other.id) and (self.dir.name == other.dir.name)
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ != other.__dict__
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            if (self.id == other.id):
                return self.dir.name < other.dir.name
            return self.id < other.id
            
        else:
            return False
    def __le__(self, other):
        if isinstance(other, self.__class__):
            if (self.id == other.id):
                return self.dir.name <= other.dir.name
            return self.id <= other.id
            
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            if (self.id == other.id):
                return self.dir.name > other.dir.name
            return self.id > other.id
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, self.__class__):
            if (self.id == other.id):
                return self.dir.name >= other.dir.name
            return self.id >= other.id
        else:
            return False
    
