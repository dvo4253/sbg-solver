from src.Move import Move, DIRECTION
import csv
__all__ = ["readGameState"]

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
            line = line  + str(item).rjust(3,' ') + ', '
        print(line)

# Gets string output of state
def strState(state):
    strResult = ""
    for row in state:
        line = ''
        for item in row:
            line = line  + str(item) + ', \n'
        strResult += line

    return strResult

    

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
    # I started with this value at 3. We need to have a separate function that checks of the goal
    # piece can move. Heuristically this is a special case that we want to track separately most likely.
    # This is a separte call as well because we keep the rest of the pieces normalized. The goal piece
    # always has an id of 2. Essentially we can have a separate function the gets goal moves and appends
    # this on to the moves list at the end. Or we can have a separate list for goal moves and if that
    # list is populated we choose one from that list first (hopefully towards to goal)
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
                    move = Move(nextIdx, DIRECTION.RIGHT)
                    moves.append(move)
                
                # Check If Left Move Is Valid
                leftValid = checkLeftValid(i,j,state,nextIdx)
                if (leftValid): 
                    move = Move(nextIdx, DIRECTION.LEFT)
                    moves.append(move)
                
                # Check If Down Move Is Valid
                downValid = checkDownValid(i,j,state,nextIdx)
                if (downValid): 
                    move = Move(nextIdx, DIRECTION.DOWN)
                    moves.append(move)
                
                # Check If Up Move Is Valid
                upValid = checkUpValid(i,j,state,nextIdx)
                if (upValid): 
                    move = Move(nextIdx, DIRECTION.UP)
                    moves.append(move)

            nextIdx += 1
            while  j < w and state[i][j] != nextIdx:        
                j += 1
        i += 1

    moves += getGoalMoves(state)

    return moves


def getGoalMoves(state):
    moves = []
    goalIdx = 2
    w = state[0][0]
    h = state[0][1]
    #print("h: " + str(h))
    i = 2
    j = 1

    goalFound = False
    while i < h:
        while j < w:
            # print("i: " + str(i))
            # print("j: " + str(j))
            
            # print("goalIdx: " + str(goalIdx))
            # print("state[i][j]: " + str(state[i][j]))
            if state[i][j] == goalIdx:
                goalFound = True
                # Check If Right Move Is Valid
                rightValid = checkRightValid(i,j,state,goalIdx)
                if (rightValid): 
                    move = Move(goalIdx, DIRECTION.RIGHT)
                    moves.append(move)
                
                # Check If Left Move Is Valid
                # print("Checking Goal Left")
                leftValid = checkLeftValid(i,j,state,goalIdx)
                if (leftValid): 
                    move = Move(goalIdx, DIRECTION.LEFT)
                    moves.append(move)
                
                # Check If Down Move Is Valid
                downValid = checkDownValid(i,j,state,goalIdx)
                if (downValid): 
                    move = Move(goalIdx, DIRECTION.DOWN)
                    moves.append(move)
                
                # Check If Up Move Is Valid
                upValid = checkUpValid(i,j,state,goalIdx)
                if (upValid): 
                    move = Move(goalIdx, DIRECTION.UP)
                    moves.append(move)
            j +=1
            if (goalFound):
                break
        if (goalFound):
            break
        j = 1
        i += 1

    #print("MOVES: ")
    # for move in moves:
    #     print(move)

    return moves

# These calls should be consolidated to only one nested loop
def checkUpValid(i,j, state, id):
    w = state[0][0]
    # h = state[0][1]
    horzCursor = 0
    #vertCursor = 0
    valid = True

    while state[i][j + horzCursor] == id and j + horzCursor < w:
        if((state[i -1][j + horzCursor] > 0) or (id != 2 and state[i -1][j + horzCursor] == -1)):
            valid = False
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
        
        if((state[i+ vertCursor][j + horzCursor] > 0) or (id != 2 and state[i+ vertCursor][j + horzCursor] == -1)):
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

    # print("i: " + str(i))
    # print("j: " + str(j))
    # print("id: " + str(id))

    while (state[i+ vertCursor][j] == id) and (i + vertCursor < h):
        # print("state[i+ vertCursor][j]: " + str(state[i+ vertCursor][j]))
        while state[i+ vertCursor][j + horzCursor] == id and j < w and i < h:
            horzCursor += 1
        # print("state[i+ vertCursor][j + horzCursor]: " + str(state[i+ vertCursor][j + horzCursor]))
        if((state[i+ vertCursor][j + horzCursor] > 0) or (id != 2 and state[i+ vertCursor][j + horzCursor] == -1)):
            valid = False
        
        horzCursor = 0
        vertCursor += 1
        # print("VALID: " + str(valid))
        
    # print("VALID2: " + str(valid))
    return valid

    

def checkLeftValid(i,j, state, id):
    w = state[0][0]
    h = state[0][1]
    horzCursor = 0
    vertCursor = 0
    valid = True

    # print("i: " + str(i))
    # print("j: " + str(j))
    # print("id: " + str(id))

    while (state[i+ vertCursor][j] == id) and (i + vertCursor < h):
        # print("vertCursor: " + str(vertCursor))
        # print("state[i+ vertCursor][j - 1]: " + str(state[i+ vertCursor][j - 1]))
        if((state[i+ vertCursor][j - 1] > 0) or (id != 2 and state[i+ vertCursor][j - 1] == -1)):
            valid = False
        vertCursor += 1


        # while state[i+ vertCursor][j + horzCursor] == id and j > 1 and i > 1:
        #     horzCursor -= 1
        
        # if state[i+ vertCursor][j + horzCursor] <= 0:
        #     valid = False
        #     horzCursor = 0
        # vertCursor += 1

    return valid

def isStateEqual(state1, state2):
    
    w1 = state1[0][0]
    h1 = state1[0][1]

    w2 = state2[0][0]
    h2 = state2[0][1]

    i = 1
    j = 0
    equalFlag = True

    # Verify the size is the same
    if (w1 != w2 or h1 != h2):
        return False

    h = h1
    w = w1

    #print("h: " + str(h))
    #print("w: " + str(w))
    while (i < h and equalFlag):

        while (j < w and equalFlag):
            #print("i: " + str(i))
            #print("j: " + str(j))
            if (state1[i][j] != state2[i][j]):
                equalFlag = False
            j += 1
        i += 1
        j = 0

    return equalFlag


def isInClosedSet(closedSet, state):

    isClosed = False
    for closedState in closedSet:
        isClosed = isStateEqual(closedState, state)
        if (isClosed):
            break

    return isClosed

def makeMove(currentState, move):
    nextState = []
    if(move.dir == DIRECTION.LEFT):
        nextState = moveLeft(currentState, move)
    elif(move.dir == DIRECTION.RIGHT):
        nextState = moveRight(currentState, move)
    elif(move.dir == DIRECTION.DOWN):
        nextState = moveDown(currentState, move)
    elif(move.dir == DIRECTION.UP):
        nextState = moveUp(currentState, move)
    else:
        nextState = cloneState(currentState)

    return nextState



def moveLeft(state, move):
    w = state[0][0]
    h = state[0][1]
    i = 1
    j = w - 1
    rightMost = True
    
    nextState = cloneState(state)
    
    while i < h:
        while j > 0:
            if (state[i][j] == move.id):
                nextState[i][j-1] = state[i][j]
                if (rightMost):
                    nextState[i][j] = 0
                    rightMost = False
            j -= 1
        i += 1
        j = w - 1
        rightMost = True
    
    return nextState


def moveRight(state, move):
    w = state[0][0]
    h = state[0][1]
    i = 1
    j = 0
    leftMost = True
    
    nextState = cloneState(state)
    
    while i < h:
        while j < w:
            if (state[i][j] == move.id):
                nextState[i][j+1] = state[i][j]
                if (leftMost):
                    nextState[i][j] = 0
                    leftMost = False
            j += 1
        i += 1
        j = 0
        leftMost = True
    
    return nextState

def moveUp(state, move):
    w = state[0][0]
    h = state[0][1]
    i = h-1
    j = 0
    bottomMost = True
    found = False
    nextState = cloneState(state)
    
    while i > 0:
        while j < w:
            if (state[i][j] == move.id):
                found = True
                nextState[i-1][j] = state[i][j]
                if (bottomMost):
                    nextState[i][j] = 0
            j += 1
        if (found):
            bottomMost = False
        i -= 1
        j = 0
        # bottomMost = True
    
    return nextState

def moveDown(state, move):
    w = state[0][0]
    h = state[0][1]
    i = 1
    j = 0
    topMost = True
    found = False
    nextState = cloneState(state)
    
    while i < h:
        while j < w:
            if (state[i][j] == move.id):
                found = True
                nextState[i+1][j] = state[i][j]
                if (topMost):
                    nextState[i][j] = 0
                    
            j += 1
        if (found):
            topMost = False
        i += 1
        j = 0
        # topMost = True
    
    return nextState

def getStateHash(state):
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
