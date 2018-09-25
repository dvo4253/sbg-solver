import csv

matrix = []

def readGameState(path):
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

state = readGameState('../state/SBP-bricks-level1.txt')
stateAdd = "Original State Address" + hex(id(state))
newState = cloneState(state)
newStateAdd = "New State Address " + hex(id(newState))
print("ORIGINAL")
print(stateAdd)
printState(state)
print("NEW")
print(newStateAdd)
printState(newState)

inGoal = "In Goal? " + str(inGoalCheck(state))
print(inGoal)