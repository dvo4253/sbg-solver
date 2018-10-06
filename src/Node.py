import src.stateUtils as stateUtils

class Node:
    def __init__(self, state, moves):
        self.state = state
        self.moves = moves
    
    def __str__(self):
        strResult = "****************** NODE *******************\n"
        strResult += stateUtils.printState(self.state)
        strResult += "\n"
        strResult = "~~~~~~Moves ~~~~~~~\n"
        for move in self.moves:
            strResult = str(move) + "\n"
        return strResult