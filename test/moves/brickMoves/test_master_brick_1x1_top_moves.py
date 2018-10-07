import unittest
import os
from src.Move import Move
from src.Move import DIRECTION
import src.stateUtils as stateUtils
from test.state.moves.master._1x1.top.top_middle_moveUp_assert import getMoves as _1x1_top_middle_moveUp_assert_getMoves
from test.state.moves.master._1x1.top.top_middle_moveLeft_assert import getMoves as _1x1_top_middle_moveLeft_assert_getMoves
from test.state.moves.master._1x1.top.top_middle_moveRight_assert import getMoves as _1x1_top_middle_moveRight_assert_getMoves
from test.state.moves.master._1x1.top.top_middle_moveDown_assert import getMoves as _1x1_top_middle_moveDown_assert_getMoves
from test.state.moves.master._1x1.top.top_left_moveUp_assert import getMoves as _1x1_top_left_moveUp_assert_getMoves
from test.state.moves.master._1x1.top.top_left_moveRight_assert import getMoves as _1x1_top_left_moveRight_assert_getMoves
from test.state.moves.master._1x1.top.top_left_moveDown_assert import getMoves as _1x1_top_left_moveDown_assert_getMoves
from test.state.moves.master._1x1.top.top_right_moveUp_assert import getMoves as _1x1_top_right_moveUp_assert_getMoves
from test.state.moves.master._1x1.top.top_right_moveLeft_assert import getMoves as _1x1_top_right_moveLeft_assert_getMoves
from test.state.moves.master._1x1.top.top_right_moveDown_assert import getMoves as _1x1_top_right_moveDown_assert_getMoves

from test.util.validateMove import getState, validateMoves
path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)

class TestCheckMasterMoves(unittest.TestCase):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # TOP LEFT TESTING          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def test_master_Top_Left_MoveUp__1x1(self):
        statePath = dir_path + "/../../state/moves/master/_1x1/top/"
        state = getState("test_master_Top_Left_MoveUp__1x1", statePath + "top_left_moveUp.txt")
        expectedMoves = _1x1_top_left_moveUp_assert_getMoves()
        
        validateMoves(self, state, expectedMoves)

    def test_master_Top_Left_MoveRight_1x1(self):
        statePath = dir_path + "/../../state/moves/master/_1x1/top/"
        state = getState("test_master_Top_Left_MoveRight_1x1", statePath + "top_left_moveRight.txt")
        expectedMoves = _1x1_top_left_moveRight_assert_getMoves()
        
        validateMoves(self, state, expectedMoves)

    def test_master_Top_Left_MoveDown_1x1(self):
        statePath = dir_path + "/../../state/moves/master/_1x1/top/"
        state = getState("test_master_Top_Left_MoveDown_1x1", statePath + "top_left_moveDown.txt")
        expectedMoves = _1x1_top_left_moveDown_assert_getMoves()
        
        validateMoves(self, state, expectedMoves)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # TOP MIDDLE TESTING        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def test_master_Top_Middle_MoveUp_1x1(self):
        statePath = dir_path + "/../../state/moves/master/_1x1/top/"
        state = getState("test_master_Top_Middle_MoveUp_1x1", statePath + "top_middle_moveUp.txt")
        expectedMoves = _1x1_top_middle_moveUp_assert_getMoves()
        
        validateMoves(self, state, expectedMoves)

    def test_master_Top_Middle_MoveLeft_1x1(self):
        statePath = dir_path + "/../../state/moves/master/_1x1/top/"
        state = getState("test_master_Top_Middle_MoveLeft_1x1", statePath + "top_middle_moveLeft.txt")
        expectedMoves = _1x1_top_middle_moveLeft_assert_getMoves()
        
        validateMoves(self, state, expectedMoves)

    def test_master_Top_Middle_MoveRight_1x1(self):
        statePath = dir_path + "/../../state/moves/master/_1x1/top/"
        state = getState("test_master_Top_Middle_MoveRight_1x1", statePath + "top_middle_moveRight.txt")
        expectedMoves = _1x1_top_middle_moveRight_assert_getMoves()
        
        validateMoves(self, state, expectedMoves)

    def test_master_Top_Middle_MoveDown_1x1(self):
        statePath = dir_path + "/../../state/moves/master/_1x1/top/"
        state = getState("test_master_Top_Middle_MoveDown_1x1", statePath + "top_middle_moveDown.txt")
        expectedMoves = _1x1_top_middle_moveDown_assert_getMoves()
        
        validateMoves(self, state, expectedMoves)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # TOP RIGHT TESTING         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def test_master_Top_Right_MoveUp_1x1(self):
        statePath = dir_path + "/../../state/moves/master/_1x1/top/"
        state = getState("test_master_Top_Right_MoveUp_1x1", statePath + "top_right_moveUp.txt")
        expectedMoves = _1x1_top_right_moveUp_assert_getMoves()
        
        validateMoves(self, state, expectedMoves)

    def test_master_Top_Right_MoveLeft_1x1(self):
        statePath = dir_path + "/../../state/moves/master/_1x1/top/"
        state = getState("test_master_Top_Right_MoveLeft_1x1", statePath + "top_right_moveLeft.txt")
        expectedMoves = _1x1_top_right_moveLeft_assert_getMoves()
        
        validateMoves(self, state, expectedMoves)

    def test_master_Top_Right_MoveDown_1x1(self):
        statePath = dir_path + "/../../state/moves/master/_1x1/top/"
        state = getState("test_master_Top_Right_MoveDown_1x1", statePath + "top_right_moveDown.txt")
        expectedMoves = _1x1_top_right_moveDown_assert_getMoves()
        
        validateMoves(self, state, expectedMoves)

