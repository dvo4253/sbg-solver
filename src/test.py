import stateUtils
import sys
from Move import Move
from Move import DIRECTION

# Get the initial state file from input
inputStateFile = sys.argv[1]

# Read in the state file to a matrix
state = stateUtils.readGameState(inputStateFile)
stateUtils.printState(state)

inGoal = "In Goal? " + str(stateUtils.inGoalCheck(state))
print(inGoal)

state = stateUtils.normalizeState(state)
print("Normalized State")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
stateUtils.printState(state)

moves = stateUtils.getValidMoves(state)

closed = []
closed.append(state)


print("Moves")
move = Move(2, DIRECTION.DOWN)
print(move)
nextState = stateUtils.makeMove(state, move )
stateUtils.printState(nextState)
# for move in moves:
#     print(move)
#     nextState = stateUtils.makeMove(state, move)
#     stateUtils.printState(nextState)
#     print("~~~~~~~~~~~~~~~~~~~~~~~~~")