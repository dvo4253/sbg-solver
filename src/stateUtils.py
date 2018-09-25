import csv

def readGameState(path):
    matrix = []
    with open(path) as gameStateCSV:
        readCSV = csv.reader(gameStateCSV, delimiter=',')
        
        for row in readCSV:
            # Last element of each row is empty
            row.pop()
            matrix.append(row)
            
    return matrix

# Print the state of the game from matrix
def printState(state):
    for row in state:
        line = ''
        for item in row:
            line = line  + item + ', '
        print(line)

def cloneState(state):
    newState = []
    for row in state:
        newStateRow = []
        for item in row:
            newStateRow.append(item)
        newState.append(newStateRow)
    return newState

def inGoalCheck(state):
    for row in state:
        for item in row:
            if item == "-1":
                return False
    return True
