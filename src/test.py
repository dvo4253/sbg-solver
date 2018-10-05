import stateUtils
import sys

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
for move in moves:
    print(move)
    nextState = stateUtils.makeMove(state, move)
    stateUtils.printState(nextState)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")