import random
import sys
import src.stateUtils as stateUtils
from src.Node import Node
def execute(fileName):

    # Get the initial state file from input
    #inputStateFile = sys.argv[1]
    inputStateFile = fileName
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
    MAX_MOVES = 100000
    move_count = 0
    while(not stateUtils.inGoalCheck(currentState) and move_count < MAX_MOVES):
        # input("Press Enter to continue...")
        closed.append(currentState)
        moves = stateUtils.getValidMoves(currentState)
        selectedMove = random.randint(0,len(moves) - 1)
        print("# of Moves " + str(len(moves)))
        print("Selected Move: " + str(selectedMove) + " < " + str(moves[selectedMove]) + " >")

        currentState = stateUtils.makeMove(currentState, moves[selectedMove])
        stateUtils.printState(currentState)
        
        currentState = stateUtils.normalizeState(currentState)
        print("Normalized State")
        stateUtils.printState(currentState)
        move_count += 1
        
        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("TOTAL # MOVES: " + str(move_count))
    # for move in moves:
    #     print(move)
    #     nextState = stateUtils.makeMove(state, move)
    #     stateUtils.printState(nextState)
    #     print("~~~~~~~~~~~~~~~~~~~~~~~~~")