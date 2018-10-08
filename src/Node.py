import src.stateUtils as stateUtils

class Node:
    def __init__(self, state):
        self.hash = stateUtils.getStateHash(state)
        self.state = state
        self.moves = []
        self.nodes = []
        self.visited = False
    
    def __str__(self):
        strResult = "****************** NODE *******************\n"
        strResult += stateUtils.printState(self.state)
        strResult += "\n"
        strResult = "~~~~~~Moves ~~~~~~~\n"
        for move in self.moves:
            strResult = str(move) + "\n"
        return strResult

    def addNode(self, node):
        self.nodes.append(node)

    def setMoves(self, moves):
        self.moves = moves

    
            