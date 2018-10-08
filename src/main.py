import random
from src.Node import Node
from src.Queue import Queue
import time
import sys
# import queue
import src.stateUtils as stateUtils
from src.Node import Node
def execute(fileName):

    # Get the initial state file from input
    #inputStateFile = sys.argv[1]
    inputStateFile = fileName
    # Read in the state file to a matrix
    state = stateUtils.readGameState(inputStateFile)
    # stateUtils.printState(state)

    # queue = Queue()

    state = stateUtils.normalizeState(state)
    # print("Normalized State")
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~")
    stateUtils.printState(state)

    # moves = stateUtils.getValidMoves(state)

    
    # currentNode.moves = moves
    currentNode = Node(state)
    # queue.enqueue(currentNode)

    dictionary = {currentNode.hash: []}
    start = time.time()
    visited = BFS(dictionary, state)
    end = time.time()
    totalSecs = end - start
    
    
    # stateUtils.printState(dictionary[visited[-1]][0].parent.state)
    
    parent = dictionary[visited[-1]][0].parent
    finalPath = []
    while parent: 
        finalPath.append(parent)
        # print(parent[1])
        if hasattr(parent[0],'parent'):
            parent = parent[0].parent
        else:
            parent = None

    # move = finalPath.pop()
    pathLength = len(finalPath)
    while finalPath: 
        result = finalPath.pop()
        stateUtils.printState(result[0].state)
        print(result[1])

    stateUtils.printState(dictionary[visited[-1]][0].state)

    print(str(len(visited)) + " " + str(round(totalSecs, 2)) + " " + str(pathLength))
    # for  move in dictionary[visited[-1]][0].moves:
    #     print(move)
    # # for node in dictionary[visited[1]]:
    #     stateUtils.printState(node.state)
    #Random(state)



def Random(initialState):
    MAX_MOVES = 100000
    move_count = 0
    currentState = initialState

    while(not stateUtils.inGoalCheck(currentState) and move_count < MAX_MOVES):
        #input("Press Enter to continue...")
        moves = stateUtils.getValidMoves(currentState)
        selectedMove = random.randint(0,len(moves) - 1)
        #print("# of Moves " + str(len(moves)))
        print(str(moves[selectedMove]))

        # for moveItem in moves:
        #     print(moveItem)
            
        currentState = stateUtils.makeMove(currentState, moves[selectedMove])
        #stateUtils.printState(currentState)
        
        currentState = stateUtils.normalizeState(currentState)
        #print("Normalized State")
        #stateUtils.printState(currentState)
        move_count += 1
        
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print("TOTAL # MOVES: " + str(move_count))
    
    stateUtils.printState(currentState)
    

    
def BFS(graph, startState):
    queue = Queue()
    currentNode = Node(startState)
    queue.enqueue(currentNode)
    visited = []
    explored = []
    i = 0
    inGoal = False
    while (queue.size() > 0 and not inGoal):

        node = queue.dequeue()
        if (node.hash not in visited):
            i += 1
            # print("Move #: " + str(i))
            visited.append(node.hash)
            inGoal = stateUtils.inGoalCheck(node.state)
            
            #stateUtils.printState(node.state)

            moves = stateUtils.getValidMoves(node.state)
            node.moves = moves
            for move in moves:
                childState = stateUtils.makeMove(node.state, move)
                childState = stateUtils.normalizeState(childState)
                childNode = Node(childState)
                # parent is a tuple containing the move and the node
                childNode.parent = (node, move)
                queue.enqueue(childNode)
                if (node.hash not in graph.keys()):
                    graph[node.hash] = [node, childNode]
                else:
                    graph[node.hash].append(childNode)
                

    return visited
    