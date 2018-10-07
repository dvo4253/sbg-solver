import unittest
#import Move
from src.Move import Move
from src.Move import DIRECTION
import src.stateUtils as stateUtils
from test.util.validateMove import assertGoalMoveResult, printState, getState, getGameStates, validateMoves
import os
path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)

class TestGoalBrickMoves(unittest.TestCase):

    def test_goalMoveLeft_1x1(self):
        statePath = dir_path + "/../../state/goalBrick/moveLeft/"

        inputStateFile = statePath + "/1x1.txt"
        expectedStateFile = statePath + "/1x1_assert.txt"

        move = Move(2, DIRECTION.LEFT)
        assertGoalMoveResult(self, inputStateFile, expectedStateFile, move)

    def test_goalMoveLeft_1x2(self):
        statePath = dir_path + "/../../state/goalBrick/moveLeft/"

        inputStateFile = statePath + "/1x2.txt"
        expectedStateFile = statePath + "/1x2_assert.txt"

        move = Move(2, DIRECTION.LEFT)
        assertGoalMoveResult(self, inputStateFile, expectedStateFile, move)

    def test_goalMoveLeft_2x1(self):
        statePath = dir_path + "/../../state/goalBrick/moveLeft/"

        inputStateFile = statePath + "/2x1.txt"
        expectedStateFile = statePath + "/2x1_assert.txt"

        move = Move(2, DIRECTION.LEFT)
        assertGoalMoveResult(self, inputStateFile, expectedStateFile, move)

    def test_goalMoveLeft_2x2(self):
        statePath = dir_path + "/../../state/goalBrick/moveLeft/"

        inputStateFile = statePath + "/2x2.txt"
        expectedStateFile = statePath + "/2x2_assert.txt"

        move = Move(2, DIRECTION.LEFT)
        assertGoalMoveResult(self, inputStateFile, expectedStateFile, move)

    def test_goalMoveRight_1x1(self):
        statePath = dir_path + "/../../state/goalBrick/moveRight/"

        inputStateFile = statePath + "/1x1.txt"
        expectedStateFile = statePath + "/1x1_assert.txt"

        move = Move(2, DIRECTION.RIGHT)
        assertGoalMoveResult(self, inputStateFile, expectedStateFile, move)

    def test_goalMoveRight_1x2(self):
        statePath = dir_path + "/../../state/goalBrick/moveRight/"

        inputStateFile = statePath + "/1x2.txt"
        expectedStateFile = statePath + "/1x2_assert.txt"

        move = Move(2, DIRECTION.RIGHT)
        assertGoalMoveResult(self, inputStateFile, expectedStateFile, move)

    def test_goalMoveRight_2x1(self):
        statePath = dir_path + "/../../state/goalBrick/moveRight/"

        inputStateFile = statePath + "/2x1.txt"
        expectedStateFile = statePath + "/2x1_assert.txt"

        move = Move(2, DIRECTION.RIGHT)
        assertGoalMoveResult(self, inputStateFile, expectedStateFile, move)

    def test_goalMoveRight_2x2(self):
        statePath = dir_path + "/../../state/goalBrick/moveRight/"

        inputStateFile = statePath + "/2x2.txt"
        expectedStateFile = statePath + "/2x2_assert.txt"

        move = Move(2, DIRECTION.RIGHT)
        assertGoalMoveResult(self, inputStateFile, expectedStateFile, move)

    def test_goalMoveDown_1x1(self):
        statePath = dir_path + "/../../state/goalBrick/moveDown/"

        inputStateFile = statePath + "/1x1.txt"
        expectedStateFile = statePath + "/1x1_assert.txt"

        move = Move(2, DIRECTION.DOWN)
        assertGoalMoveResult(self, inputStateFile, expectedStateFile, move)

    def test_goalMoveDown_1x2(self):
        statePath = dir_path + "/../../state/goalBrick/moveDown/"

        inputStateFile = statePath + "/1x2.txt"
        expectedStateFile = statePath + "/1x2_assert.txt"

        move = Move(2, DIRECTION.DOWN)
        assertGoalMoveResult(self, inputStateFile, expectedStateFile, move)

    def test_goalMoveDown_2x1(self):
        statePath = dir_path + "/../../state/goalBrick/moveDown/"

        inputStateFile = statePath + "/2x1.txt"
        expectedStateFile = statePath + "/2x1_assert.txt"

        move = Move(2, DIRECTION.DOWN)
        assertGoalMoveResult(self, inputStateFile, expectedStateFile, move)

    def test_goalMoveDown_2x2(self):
        statePath = dir_path + "/../../state/goalBrick/moveDown/"

        inputStateFile = statePath + "/2x2.txt"
        expectedStateFile = statePath + "/2x2_assert.txt"

        move = Move(2, DIRECTION.DOWN)
        assertGoalMoveResult(self, inputStateFile, expectedStateFile, move)

if __name__ == '__main__':
    unittest.main()