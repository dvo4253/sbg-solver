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

    # Simple hash created by concatenating the rows of the matix as a string and 
    # taking the has of the full string.
    def getStateHash(self, state):
        i = 1 
        j = 0
        w = state[0][0]
        h = state[0][1]
        string = ""
        while i < h:
            while j < w:
                string += str(i) + str(j) + str(state[i][j])
                j += 1
            i += 1
            j = 0
        
        return hash(string)

    # ***************************************************************
    # Compare hashes for equality
    # ***************************************************************
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.hash == other.hash)
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ != other.__dict__
        else:
            return False

    # ***************************************************************
    # These comparisons are used for sorting the priority queue if one
    # is used. Therefore these comparison functions define the heuristic
    # Currently the distance of the Master Node to the goal node
    # is the heuristic being used and should be assigned to the 
    # distance attribute of the node.
    # ***************************************************************
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
    
