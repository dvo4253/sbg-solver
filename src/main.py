import stateUtils
import random
import sys
from Node import Node

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



closed = []


print("Moves")

currentState = state
# while(not stateUtils.inGoalCheck(currentState)):
MAX_MOVES = 500
move_count = 0
while(not stateUtils.inGoalCheck(currentState) and move_count < MAX_MOVES):
    closed.append(currentState)
    moves = stateUtils.getValidMoves(currentState)
    selectedMove = random.randint(0,len(moves) - 1)
    print("# of Moves " + str(len(moves)))
    print("Selected Move: " + str(selectedMove) + " < " + str(moves[selectedMove]) + " >")

    currentState = stateUtils.makeMove(currentState, moves[selectedMove])
    move_count += 1
    stateUtils.printState(currentState)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("TOTAL # MOVES: " + str(move_count))
# for move in moves:
#     print(move)
#     nextState = stateUtils.makeMove(state, move)
#     stateUtils.printState(nextState)
#     print("~~~~~~~~~~~~~~~~~~~~~~~~~")