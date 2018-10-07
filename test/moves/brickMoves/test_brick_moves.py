import unittest
import os
#import Move
from src.Move import Move
from src.Move import DIRECTION
import src.stateUtils as stateUtils
from test.state.moves.brick._1x1.top_left_moves_assert import getMoves as _1x1_top_left_moves_assert_getMoves
from test.state.moves.brick._1x1.middle_moves_assert import getMoves as _1x1_middle_moves_assert_getMoves
from test.state.moves.brick._1x1.top_right_moves_assert import getMoves as _1x1_top_right_moves_assert_getMoves
from test.util.validateMove import getState, validateMoves

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)

class TestBrickMoves(unittest.TestCase):

    def test_validate_1x1_top_left(self):
        statePath = dir_path + "/../../state/moves/brick/_1x1/"
        state = getState("test_validate_1x1_top_left", statePath + "/top_left.txt")
        expectedMoves = _1x1_top_left_moves_assert_getMoves()
        
        validateMoves(self, state, expectedMoves)
        
    def test_validate_1x1_middle(self):
        statePath = dir_path + "/../../state/moves/brick/_1x1/"
        state = getState("test_validate_1x1_middle", statePath + "/middle.txt")
        expectedMoves = _1x1_middle_moves_assert_getMoves()

        validateMoves(self, state, expectedMoves)

    def test_validate_1x1_top_right(self):
        statePath = dir_path + "/../../state/moves/brick/_1x1/"
        state = getState("test_validate_1x1_top_right", statePath + "/top_right.txt")
        expectedMoves = _1x1_top_right_moves_assert_getMoves()

        validateMoves(self, state, expectedMoves)