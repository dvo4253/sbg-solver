import unittest
#import Move
from src.Move import Move
from src.Move import DIRECTION
import src.stateUtils as stateUtils
import os
path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)

class TestStringMethods(unittest.TestCase):

    def test_goalMoveLeft_1x1(self):
        statePath = dir_path + "/../state/goalBrick/moveLeft/"

        inputStateFile = statePath + "/1x1.txt"
        expectedStateFile = statePath + "/1x1_assert.txt"

        move = Move(2, DIRECTION.LEFT)
        assertGoalMoveResult(self, inputStateFile, expectedStateFile, move)

    def test_goalMoveLeft_1x2(self):
        statePath = dir_path + "/../state/goalBrick/moveLeft/"

        inputStateFile = statePath + "/1x2.txt"
        expectedStateFile = statePath + "/1x2_assert.txt"

        move = Move(2, DIRECTION.LEFT)
        assertGoalMoveResult(self, inputStateFile, expectedStateFile, move)

    def test_goalMoveLeft_2x1(self):
        statePath = dir_path + "/../state/goalBrick/moveLeft/"

        inputStateFile = statePath + "/2x1.txt"
        expectedStateFile = statePath + "/2x1_assert.txt"

        move = Move(2, DIRECTION.LEFT)
        assertGoalMoveResult(self, inputStateFile, expectedStateFile, move)

    def test_goalMoveLeft_2x2(self):
        statePath = dir_path + "/../state/goalBrick/moveLeft/"

        inputStateFile = statePath + "/2x2.txt"
        expectedStateFile = statePath + "/2x2_assert.txt"

        move = Move(2, DIRECTION.LEFT)
        assertGoalMoveResult(self, inputStateFile, expectedStateFile, move)

    def test_goalMoveRight_1x1(self):
        statePath = dir_path + "/../state/goalBrick/moveRight/"

        inputStateFile = statePath + "/1x1.txt"
        expectedStateFile = statePath + "/1x1_assert.txt"

        move = Move(2, DIRECTION.RIGHT)
        assertGoalMoveResult(self, inputStateFile, expectedStateFile, move)

    def test_goalMoveRight_1x2(self):
        statePath = dir_path + "/../state/goalBrick/moveRight/"

        inputStateFile = statePath + "/1x2.txt"
        expectedStateFile = statePath + "/1x2_assert.txt"

        move = Move(2, DIRECTION.RIGHT)
        assertGoalMoveResult(self, inputStateFile, expectedStateFile, move)

    def test_goalMoveRight_2x1(self):
        statePath = dir_path + "/../state/goalBrick/moveRight/"

        inputStateFile = statePath + "/2x1.txt"
        expectedStateFile = statePath + "/2x1_assert.txt"

        move = Move(2, DIRECTION.RIGHT)
        assertGoalMoveResult(self, inputStateFile, expectedStateFile, move)

    def test_goalMoveRight_2x2(self):
        statePath = dir_path + "/../state/goalBrick/moveRight/"

        inputStateFile = statePath + "/2x2.txt"
        expectedStateFile = statePath + "/2x2_assert.txt"

        move = Move(2, DIRECTION.RIGHT)
        assertGoalMoveResult(self, inputStateFile, expectedStateFile, move)

    def test_goalMoveDown_1x1(self):
        statePath = dir_path + "/../state/goalBrick/moveDown/"

        inputStateFile = statePath + "/1x1.txt"
        expectedStateFile = statePath + "/1x1_assert.txt"

        move = Move(2, DIRECTION.DOWN)
        assertGoalMoveResult(self, inputStateFile, expectedStateFile, move)

    def test_goalMoveDown_1x2(self):
        statePath = dir_path + "/../state/goalBrick/moveDown/"

        inputStateFile = statePath + "/1x2.txt"
        expectedStateFile = statePath + "/1x2_assert.txt"

        move = Move(2, DIRECTION.DOWN)
        assertGoalMoveResult(self, inputStateFile, expectedStateFile, move)

    def test_goalMoveDown_2x1(self):
        statePath = dir_path + "/../state/goalBrick/moveDown/"

        inputStateFile = statePath + "/2x1.txt"
        expectedStateFile = statePath + "/2x1_assert.txt"

        move = Move(2, DIRECTION.DOWN)
        assertGoalMoveResult(self, inputStateFile, expectedStateFile, move)

    def test_goalMoveDown_2x2(self):
        statePath = dir_path + "/../state/goalBrick/moveDown/"

        inputStateFile = statePath + "/2x2.txt"
        expectedStateFile = statePath + "/2x2_assert.txt"

        move = Move(2, DIRECTION.DOWN)
        assertGoalMoveResult(self, inputStateFile, expectedStateFile, move)

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
        state = stateUtils.readGameState(inputStateFile)
        state = stateUtils.normalizeState(state)
        expectedState = stateUtils.readGameState(expectedStateFile)
        expectedState = stateUtils.normalizeState(expectedState)
        
        printState("inputStateFile", state)
        printState("expectedState", expectedState)
        
        return [state, expectedState]


if __name__ == '__main__':
    unittest.main()