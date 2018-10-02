from Move import Move
import csv


def readGameState(path):
    matrix = []
    newRow = []
    with open(path) as gameStateCSV:
        readCSV = csv.reader(gameStateCSV, delimiter=',')
        
        for row in readCSV:
            # Last element of each row is empty
            row.pop()
            newRow = []
            for item in row:
                item = int(item)
                newRow.append(item)

            matrix.append(newRow)
            
    return matrix

# Print the state of the game from matrix
def printState(state):
    for row in state:
        line = ''
        for item in row:
            line = line  + str(item) + ', '
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
            if item == -1:
                return False
    return True

# def getMoves(state, index):
#     moveList = []
#     i = 1
#     rowMax = len(state)
#     j = 0

#     while i < rowMax:
#         columnMax = state[i]
#         while j < columnMax:
#             if checkUpValid(state, state[i][j]):
#                 moveList.append('u')
#             if checkDownValid(state, state[i][j]):
#                 moveList.append('d')
#             if checkRightValid(state, state[i][j]):
#                 moveList.append('r')
#             if checkLeftValid(state, state[i][j]):
#                 moveList.append('l')
#         i += 1
#         j = 0
#     return moveList

def normalizeState(state):
    nextIdx = 3
    w = state[0][0]
    h = state[0][1]
    #print("h: " + str(h))
    i = 2
    j = 1
    while i < h:
        #print("w: " + str(w))
        j = 1
        while j < w:
            #print("nextIdx: " + str(nextIdx))
            #print("state[i][j]: " + str(state[i][j]))
            if state[i][j] == nextIdx:
                #print("NOT SWAPPING")
                nextIdx += 1
            elif state[i][j] > nextIdx:
                #print("SWAPPING")
                state = swapIdx(nextIdx, state[i][j], state)
                #print("Swapped State:")
                #printState(state)
                nextIdx += 1
            j += 1
        i += 1
    return state

def swapIdx(idx1, idx2, state):
    #print("idx1: " + str(idx1))
    #print("idx2: " + str(idx2))
    #printState(state)
    w = state[0][0]
    h = state[0][1]
    #print("h: " + str(h))
    i = 2
    j = 1
    while i < h:
        #print("i: " + str(i))
        j = 1
        while j < w:
            #print("j: " + str(j))
            
            if (state[i][j] == idx1):
                #print("SWAP: " + str(idx2))
                state[i][j] = idx2
            elif (state[i][j] == idx2):
                #print("SWAP: " + str(idx1))
                state[i][j] = idx1
            j += 1
        i += 1
    return state

# Currently this loops through all ids to see which ones
# to add to the "moves" list. A better way might be to find
# the zeros and work from there

# In order for this method to work properly the 
# state must be normalized
def getValidMoves(state):
    moves = []
    nextIdx = 3
    w = state[0][0]
    h = state[0][1]
    #print("h: " + str(h))
    i = 2
    j = 1
    while i < h:
        j = 1
        while  j < w and state[i][j] != nextIdx:        
            j += 1
        while j < w:
            if state[i][j] == nextIdx:
                
                # Check If Right Move Is Valid
                rightValid = checkRightValid(i,j,state,nextIdx)
                if (rightValid): 
                    move = Move(nextIdx, 'r')
                    moves.append(move)
                
                # Check If Left Move Is Valid
                leftValid = checkLeftValid(i,j,state,nextIdx)
                if (leftValid): 
                    move = Move(nextIdx, 'l')
                    moves.append(move)
                
                # Check If Down Move Is Valid
                downValid = checkDownValid(i,j,state,nextIdx)
                if (downValid): 
                    move = Move(nextIdx, 'd')
                    moves.append(move)
                
                # Check If Up Move Is Valid
                upValid = checkUpValid(i,j,state,nextIdx)
                if (upValid): 
                    move = Move(nextIdx, 'u')
                    moves.append(move)

            nextIdx += 1
            while  j < w and state[i][j] != nextIdx:        
                j += 1
        i += 1

    return moves


# These calls should be consolidated to only one nested loop
def checkUpValid(i,j, state, id):
    w = state[0][0]
    h = state[0][1]
    horzCursor = 0
    vertCursor = 0
    valid = True

    while state[i+ vertCursor][j + horzCursor] == id and j < w and i > 1:
        while (state[i+ vertCursor][j] == id) and (i + vertCursor > 1):
            vertCursor -= 1
        
        if state[i+ vertCursor][j + horzCursor] != 0:
            valid = False
            vertCursor = 0
        horzCursor += 1

    return valid

def checkDownValid(i,j, state, id):
    w = state[0][0]
    h = state[0][1]
    horzCursor = 0
    vertCursor = 0
    valid = True

    while state[i+ vertCursor][j + horzCursor] == id and j < w and i < h:
        while (state[i+ vertCursor][j] == id) and (i + vertCursor < h):
            vertCursor += 1
        
        if state[i+ vertCursor][j + horzCursor] != 0:
            valid = False
            vertCursor = 0
        horzCursor += 1

    return valid

def checkRightValid(i,j, state, id):
    w = state[0][0]
    h = state[0][1]
    horzCursor = 0
    vertCursor = 0
    valid = True

    while (state[i+ vertCursor][j] == id) and (i + vertCursor < h):
        while state[i+ vertCursor][j + horzCursor] == id and j < w and i < h:
            horzCursor += 1
        
        if state[i+ vertCursor][j + horzCursor] != 0:
            valid = False
            horzCursor = 0
        vertCursor += 1

    return valid

    

def checkLeftValid(i,j, state, id):
    w = state[0][0]
    h = state[0][1]
    horzCursor = 0
    vertCursor = 0
    valid = True

    while (state[i+ vertCursor][j] == id) and (i + vertCursor > 1):
        while state[i+ vertCursor][j + horzCursor] == id and j > 1 and i > 1:
            horzCursor -= 1
        
        if state[i+ vertCursor][j + horzCursor] != 0:
            valid = False
            horzCursor = 0
        vertCursor += 1

    return valid