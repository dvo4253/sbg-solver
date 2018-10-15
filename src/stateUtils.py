from src.Move import Move, DIRECTION
import csv

def readGameState(path):
    matrix = []
    newRow = []
    with open(path) as gameStateCSV:
        readCSV = csv.reader(gameStateCSV, delimiter=',')
        
        # Create a 2 dimensional array to store the state read in from the file.
        for row in readCSV:
            # Last element of each row is empty
            row.pop()
            newRow = []
            for item in row:
                item = int(item)
                newRow.append(item)

            matrix.append(newRow)

    # The initial state will always be normalized.
    return normalizeState(matrix)

# Print the state of the game from matrix
def printState(state):
    for row in state:
        line = ''
        
        for item in row:
            line = line  + str(item) + ', '
        print(line)
    print()

# Gets string output of state
def strState(state):
    strResult = ""
    for row in state:
        line = ''
        for item in row:
            line = line  + str(item) + ', \n'
        strResult += line

    return strResult

# ******************************************************************************
# Create a new two-dimentional array to store a deep clone of the state passed
# in to the function.
# ******************************************************************************
def cloneState(state):
    newState = []
    for row in state:
        newStateRow = []
        for item in row:
            newStateRow.append(item)
        newState.append(newStateRow)
    return newState

# ******************************************************************************
# Simple check space by space check to see if the goal is met.
# If there are any rows/columns that contain a "-1" then the goal has not been met.
# ******************************************************************************
def inGoalCheck(state):
    for row in state:
        for item in row:
            if item == -1:
                return False
    return True

# ******************************************************************************
# Ensure that the state is normalized.
# A master block will always remain a '2'. Any block '3' or greater will be 
# re-labeled to be in a sorted order from top left to bottom right.
# ******************************************************************************
def normalizeState(state):
    # Start with 3 as the first label.
    nextIdx = 3

    w = state[0][0]
    h = state[0][1]
    i = 2
    j = 1

    # Loop through the rows
    while i < h:
        j = 1
        # Loop through the columns
        while j < w:
            # If the space already is labeld with the index of
            # nextIdx, then just increment the nextIdx as this
            # block already has the correcd label.
            if state[i][j] == nextIdx:
                nextIdx += 1
            # If the label on the space at state[i][j] is greater
            # than the nextIdx then we must swap it out and label
            # it with the value at nextIdx.
            elif state[i][j] > nextIdx:
                state = swapIdx(nextIdx, state[i][j], state)
                nextIdx += 1
            j += 1
        i += 1
    return state

# ******************************************************************************
#   Swaps all places with the label 'idx1' with the label 'idx2' in the state 
#   passed as the 3rd parameter
# ******************************************************************************
def swapIdx(idx1, idx2, state):
    w = state[0][0]
    h = state[0][1]
    i = 2
    j = 1
    
    while i < h:
        j = 1
        while j < w:
            # Swap in place if the value at state[i][j] is the value of 'idx1'
            if (state[i][j] == idx1):
                state[i][j] = idx2
            # Swap in place if the value at state[i][j] is the value of 'idx2'    
            elif (state[i][j] == idx2):
                state[i][j] = idx1
            j += 1
        i += 1
    return state

# ******************************************************************************
#   Description: Returns a list of "Move" objects specifying the valid moves
#                from the state passed in to the function
# 
# 
# NOTE: In order for this method to work properly the 
# state must be normalized
# ******************************************************************************
def getValidMoves(state):
    moves = []

    nextIdx = 3
    w = state[0][0]
    h = state[0][1]

    i = 2
    j = 1
    while i < h:
        j = 1
        while  j < w and state[i][j] != nextIdx:        
            j += 1
        while j < w:
            # If we have reached our next idex check if a RIGHT, LEFT, DOWN, or UP move
            # is valid in the current state.
            if state[i][j] == nextIdx:
                
                # Check If Right Move Is Valid
                rightValid = checkRightValid(i,j,state,nextIdx)
                # Add the move to the list if it is valid
                if (rightValid): 
                    move = Move(nextIdx, DIRECTION.RIGHT)
                    moves.append(move)
                
                # Check If Left Move Is Valid
                leftValid = checkLeftValid(i,j,state,nextIdx)
                # Add the move to the list if it is valid
                if (leftValid): 
                    move = Move(nextIdx, DIRECTION.LEFT)
                    moves.append(move)
                
                # Check If Down Move Is Valid
                downValid = checkDownValid(i,j,state,nextIdx)
                # Add the move to the list if it is valid
                if (downValid): 
                    move = Move(nextIdx, DIRECTION.DOWN)
                    moves.append(move)
                
                # Check If Up Move Is Valid
                upValid = checkUpValid(i,j,state,nextIdx)
                if (upValid): 
                    move = Move(nextIdx, DIRECTION.UP)
                    moves.append(move)

            nextIdx += 1
            # Move along to the next state.
            while  j < w and state[i][j] != nextIdx:        
                j += 1
        i += 1

    # There is a better way to do this but didn't have time to refactore
    # rigth now. Retrieves all valid moves for the Master block 
    moves += getGoalMoves(state)

    return moves

# ******************************************************************************
#   Description: Very similar to the getValidMoves function. This just reviews 
#                the goal node to see what the valid moves are for the Master Node
# 
# 
# NOTE: In order for this method to work properly the 
# state must be normalized. Also this is a lot of duplicate code. It should be
# refactored into the getValidMoves function
# ******************************************************************************
def getGoalMoves(state):
    moves = []
    goalIdx = 2
    w = state[0][0]
    h = state[0][1]

    i = 2
    j = 1

    goalFound = False
    while i < h:
        while j < w:

            if state[i][j] == goalIdx:
                goalFound = True
                # Check If Right Move Is Valid
                rightValid = checkRightValid(i,j,state,goalIdx)
                if (rightValid): 
                    # Add the move to the list if it is valid
                    move = Move(goalIdx, DIRECTION.RIGHT)
                    moves.append(move)
                
                # Check If Left Move Is Valid
                leftValid = checkLeftValid(i,j,state,goalIdx)
                if (leftValid): 
                    # Add the move to the list if it is valid
                    move = Move(goalIdx, DIRECTION.LEFT)
                    moves.append(move)
                
                # Check If Down Move Is Valid
                downValid = checkDownValid(i,j,state,goalIdx)
                if (downValid): 
                    # Add the move to the list if it is valid
                    move = Move(goalIdx, DIRECTION.DOWN)
                    moves.append(move)
                
                # Check If Up Move Is Valid
                upValid = checkUpValid(i,j,state,goalIdx)
                if (upValid): 
                    # Add the move to the list if it is valid
                    move = Move(goalIdx, DIRECTION.UP)
                    moves.append(move)
            j +=1
            if (goalFound):
                break
        if (goalFound):
            break
        j = 1
        i += 1

    return moves

# ******************************************************************************
#   Description -- The following four functions check a different direction to see if a move
#                  is valid. They take the following parameters
#   i --           row of the id to check
#   j --           colum of the id to check
#   state --       current state to check if the move is valid
#   id --          id of the piece to check for a valid move
#
#   checkUpValid, checkDownValid, checkRightValid, checkLeftValid
# ******************************************************************************
def checkUpValid(i,j, state, id):
    w = state[0][0]

    horzCursor = 0
    
    valid = True
    # Verify that all spaces above the piece specified by 'id'
    # are a 0 or -1 (if it's the master block)
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

    # Verify that all spaces below the piece specified by 'id'
    # are a 0 or -1 (if it's the master block)
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

    while (state[i+ vertCursor][j] == id) and (i + vertCursor < h):
        while state[i+ vertCursor][j + horzCursor] == id and j < w and i < h:
            # Get to the right-most space of the piece
            horzCursor += 1
        # Verify that all spaces to the right of the piece specified by 'id'
        # are a 0 or -1 (if it's the master block)
        if((state[i+ vertCursor][j + horzCursor] > 0) or (id != 2 and state[i+ vertCursor][j + horzCursor] == -1)):
            valid = False
        
        horzCursor = 0
        vertCursor += 1

    return valid

def checkLeftValid(i,j, state, id):
    h = state[0][1]
    vertCursor = 0
    valid = True

    while (state[i+ vertCursor][j] == id) and (i + vertCursor < h):
        # Verify that all spaces to the left of the piece specified by 'id'
        # are a 0 or -1 (if it's the master block)
        if((state[i+ vertCursor][j - 1] > 0) or (id != 2 and state[i+ vertCursor][j - 1] == -1)):
            valid = False
        vertCursor += 1

    return valid

# ******************************************************************************
#   Description --      Verifies that two states are equal by a 
#                       space-by-space comparison. I should also just be able
#                       to check the hashes on the Node class if it's available.
#                       I can add that in the future.
#                       
#   Parameters --
#       state1 --       First state to compare against
#       state2 --       Second state to compare against
#   
#   Return Value --     True: if the states are equal
#                       False: if the states are different
# ******************************************************************************
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
    # Space-by-space check to make the the states
    # are the same
    while (i < h and equalFlag):
        while (j < w and equalFlag):
            if (state1[i][j] != state2[i][j]):
                equalFlag = False
            j += 1
        i += 1
        j = 0

    return equalFlag

# ******************************************************************************
# Description --        Takes a state and a move as paramters and returns the 
#                       new state(normalized) after the move has taken place. Assumes the 
#                       move is valid.
# 
# Parameters --
#   currentState --     state to execute the move against
#   move --             move to execute on the currentState
#
# Return Value --       A new state with the move executed
#   
# ******************************************************************************
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

    return normalizeState(nextState)

# ******************************************************************************
# Description:      The following four functions execute a move on a state and 
#                   returns the new state. In each function, the logic is similar,
#                   just the direction is different. Read the comments in the 
#                   'moveLeft' function for details.
#
# Parameters --
#   currentState --     state to execute the move against
#   move --             move to execute on the currentState
#
# Return Value --       A new state with the move executed
#   
#   moveLeft, moveRight, moveUp, moveDown
# ******************************************************************************
def moveLeft(state, move):
    w = state[0][0]
    h = state[0][1]
    i = 1
    j = w - 1
    rightMost = True
    
    # Initially the next state will be a cloned
    # version of the current state.
    nextState = cloneState(state)
    
    # Loop through the spaces. If we get to a space
    # that matches the id in the 'move' object then
    # shift it to the left.
    while i < h:
        # Loop from right-to-left on each row. Makes some
        # of the logic easier for leaving the open space (0)
        # behind after the move.
        while j > 0:
            if (state[i][j] == move.id):
                nextState[i][j-1] = state[i][j]
                # If the space is the right-most space
                # of the piece then we need to leave
                # an open space.
                if (rightMost):
                    nextState[i][j] = 0
                    rightMost = False
            
            # Decrement j to move left in the row
            j -= 1
        # Next row
        i += 1
        # Reset j to the right-most space
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
    
    return nextState

# ******************************************************************************
# Description --        Returns a string indicating where the goal is in the game.
# 
# Parameters -- 
#   state --            Current state. We really just need the dimensions of the state
#                       for this check.
#   goalSpaces --       Array of tuples representing the (row,column) of each 
#                       goal space
# ******************************************************************************
def findGoalLocation(state, goalSpaces):
    w = state[0][0]
    h = state[0][1]

    goalLocation = None
    
    # We only need to look at the first goal space.
    if (goalSpaces[0][0] == 1):
        goalLocation = 'TOP'
    elif (goalSpaces[0][0] == h):
        goalLocation = 'BOTTOM'
    elif (goalSpaces[0][1] == 0):
        goalLocation = 'LEFT'
    elif (goalSpaces[0][1] == w -1):
        goalLocation = 'RIGHT'

    return goalLocation

# ******************************************************************************
# Description --        Calculates a simple heuristic indicating how far the 
#                       master block is away from the goal. This a direct path
#                       calculation, not concidering any other blocks in the way.
#
# Parameters --
#   state --            State to check how far away the master block is from the goal
#   goalSpaces --       An array of tuples indicating the (row, column) spaces for
#                       the goal.
#
# Return Value --       An integer indicating the distance the master block is 
#                       from the goal.
# ******************************************************************************
def checkMasterPath(state, goalSpaces):
    
    goalLocation = findGoalLocation(state, goalSpaces)
    goalDistance = None
    # Retrieve an array of tuples (row,column) indicating the spaces
    # the master block occupies in the state
    masterSpaces = findMasterSpaces(state)
    LAST_MASTER_SPACE = len(masterSpaces) - 1
    LAST_GOAL_SPACE = len(goalSpaces) - 1

    # Calculate the distance
    if (goalLocation == 'LEFT'):
        # The first master space will be the upper left space of the master block
        goalDistance  = abs(masterSpaces[0][0] - goalSpaces[0][0]) + abs(masterSpaces[0][1] - goalSpaces[0][1])
    elif (goalLocation == 'RIGHT'):
        # The last master space will be the lower right space of the master block
        # Compare the lower-right master block space to the lowest goal space.
        # for the distance calculation.
        goalDistance  = abs(masterSpaces[LAST_MASTER_SPACE][0] - goalSpaces[LAST_GOAL_SPACE][0]) + abs(masterSpaces[LAST_MASTER_SPACE][1] - goalSpaces[LAST_GOAL_SPACE][1])
    elif (goalLocation == 'TOP'):
        # The first master space will be the upper left space of the master block
        # Compare the top-left master block space to the left-most goal space.
        goalDistance  = abs(masterSpaces[0][0] - goalSpaces[0][0]) + abs(masterSpaces[0][1] - goalSpaces[0][1])
    elif (goalLocation == 'BOTTOM'):
        # The last master space will be the lower right space of the master block
        # Compare the lower-right master block space to the right-most goal space.
        # for the distance calculation.
        goalDistance  = abs(masterSpaces[LAST_MASTER_SPACE][0] - goalSpaces[LAST_GOAL_SPACE][0]) + abs(masterSpaces[LAST_MASTER_SPACE][1] - goalSpaces[LAST_GOAL_SPACE][1])

    return goalDistance

# ******************************************************************************
# Description --        Return an array of tuples (row, column) that
#                       Indicate where the master block piece lies within the state
# ******************************************************************************
def findMasterSpaces(state):
    w = state[0][0]
    h = state[0][1]
    i = 1
    j = 0

    masterSpaces = []
    while (i < h):
        while j < w:
            if(state[i][j] == 2):
                masterSpaces.append((i,j))
            j +=1
        j = 0
        i += 1

    return masterSpaces

# ******************************************************************************
# Description --        Return an array of tuples (row, column) that
#                       Indicate where the goal lies within the state
# ******************************************************************************
def findGoal(state):
    w = state[0][0]
    h = state[0][1]
    i = 1
    j = 0
    goalSpaces = []
    
    while (j < w):
        # Check Top Row
        if(state[1][j] == -1):
            # append tuple (row column) representing
            # the location of the goal space
            goalSpaces.append((j,i))
            
        # Check Bottom Row
        if(state[h][j] == -1):
            goalSpaces.append((h,j))

        j += 1
    
    while (i < h):
        # Check the left side
        if(state[i][0] == -1):
            goalSpaces.append((i,0))
        # Check the right side
        if(state[i][w-1] == -1):
            goalSpaces.append((i,w-1))

        i += 1

    
    return goalSpaces

