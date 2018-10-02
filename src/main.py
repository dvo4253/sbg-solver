import stateUtils
import sys

inputStateFile = sys.argv[1]
# '../state/SBP-level1.txt'
state = stateUtils.readGameState(inputStateFile)
stateAdd = "Original State Address" + hex(id(state))
newState = stateUtils.cloneState(state)
newStateAdd = "New State Address " + hex(id(newState))
print("ORIGINAL")
print(stateAdd)
stateUtils.printState(state)
print("NEW")
print(newStateAdd)
stateUtils.printState(newState)

inGoal = "In Goal? " + str(stateUtils.inGoalCheck(state))
print(inGoal)

state = stateUtils.normalizeState(state)
print("Normalized State")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
stateUtils.printState(state)

moves = stateUtils.getValidMoves(state)

print("Moves")
for move in moves:
    print(move)