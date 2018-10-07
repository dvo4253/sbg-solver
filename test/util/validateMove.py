import src.stateUtils as stateUtils

def assertGoalMoveResult(self, inputStateFile, expectedStateFile, move):
    states = getGameStates(inputStateFile, expectedStateFile)

    startState = states[0]
    expectedState = states[1]

    stateUtils.getValidMoves(startState)
    nextState = stateUtils.makeMove(startState, move)

    printState("nextState", nextState)

    equal = stateUtils.isStateEqual(expectedState, nextState)
    self.assertTrue(equal)


def printState(label, state):
    print(label + " State")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")
    stateUtils.printState(state)


# Returns [inputState, expectedState] normalized
def getGameStates(inputStateFile, expectedStateFile):

    state = getState("inputStateFile", inputStateFile)
    expectedState = getState("expectedState", expectedStateFile)
    
    return [state, expectedState]

def getState(label, stateFile):
    state = stateUtils.readGameState(stateFile)
    state = stateUtils.normalizeState(state)
    printState(label, state)

    return state

def validateMoves(self, state, expectedMoves):
    expectedMoves = sorted(expectedMoves)
    print("expectedMoves")
    for move in expectedMoves:
        print(move)

    lExpected = len(expectedMoves)
    i = 0

    moves = sorted(stateUtils.getValidMoves(state))
    lMoves = len(moves)

    self.assertEqual(lMoves, lExpected)

    print("moves")

    if (lMoves == lExpected):
        for move in moves:
            print(move)
        while (i < lMoves):
            self.assertTrue(moves[i] == expectedMoves[i])
            i += 1
