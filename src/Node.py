import src.stateUtils as stateUtils

class Node:
    def __init__(self, state):
        self.hash = self.getStateHash(state)
        self.state = state
        self.moves = []
        self.distance = 0
       
    def __str__(self):
        strResult = "****************** NODE *******************\n"
        strResult += stateUtils.printState(self.state)
        strResult += "\n"
        strResult = "~~~~~~Moves ~~~~~~~\n"
        for move in self.moves:
            strResult = str(move) + "\n"
        return strResult

    def setMoves(self, moves):
        self.moves = moves
    



    def getStateHash(self, state):
        i = 1 
        j = 0
        w = state[0][0]
        h = state[0][1]
        #printState(state)
        string = ""
        while i < h:
            while j < w:
                string += str(i) + str(j) + str(state[i][j])
                j += 1
            i += 1
            j = 0
        # print(string)
        return hash(string)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            # print("SELF: " + str(self))
            return (self.hash == other.hash)
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ != other.__dict__
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.distance < other.distance
            
        else:
            return False
    def __le__(self, other):
        if isinstance(other, self.__class__):
            return self.distance <= other.distance
            
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.distance > other.distance
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, self.__class__):
            return self.distance >= other.distance
        else:
            return False
    
