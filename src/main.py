from src.Node import Node
import time
import sys
# import queue
import src.stateUtils as stateUtils
from src.Node import Node
import src.Search

def execute(fileName):
    
    # # of steps taken in Random Walk
    N = 3

    # Get the initial state file from input
    #inputStateFile = sys.argv[1]
    inputStateFile = fileName
    # Read in the state file to a matrix
    state = stateUtils.readGameState(inputStateFile)

    # state = stateUtils.normalizeState(state)
   
    # stateUtils.printState(state)
    # currentNode = Node(state)

    # print("Random Walk (N=3)")
    # src.Search.Random(state, N)

    dictionary = {}
    start = time.time()
    visited = src.Search.BFS(dictionary, state)
    end = time.time()
    totalSecs = end - start
    
    print()
    print("Breadth-First Search")
    src.Search.PrintSearchResults(dictionary, visited[-1], totalSecs)


    dictionary = {}
    start = time.time()
    visited = src.Search.DFS(dictionary, state, False)
    end = time.time()
    totalSecs = end - start
    # print("VISITED: ")
    # print(visited[-1])
    # for hash in visited:
    #     print(str(hash))
    # print(dictionary[visited[-1]])
    # for node in dictionary[visited[-1]]:
    #     parentHash = print(node.parent[0].hash)
    #     stateUtils.printState(node.state)

    # print("DICTIONARY: ")
    goalNode = dictionary[visited[-1]][0]
    node = goalNode
    parentHash = node.parent[0].hash
    parentMove = node.parent[1]
    # print("PARENT MOVE: ")
    # print(parentMove)
    
    print()
    print("Depth-First Search")

    stateUtils.printState(state)
    finalPath = [ parentMove ]
    while parentHash != None:
        node = dictionary[parentHash][0]
        
        # stateUtils.printState(node.state)
        if hasattr(node,'parent'):
            finalPath.append(node.parent[1])
            parentHash = node.parent[0].hash
            # stateUtils.printState(parent[0].state)
        else:
            parentHash = None
        
    for move in reversed(finalPath):
        print(move)
    
    stateUtils.printState(goalNode.state)

    print(str(len(dictionary)) + " " + str(round(totalSecs, 5)) + " " + str(len(finalPath)))
    # for hash in dictionary:
    #     print(str(hash))
        
    #     if(hasattr(dictionary[hash][0], "parent")):
    #         print(str(dictionary[hash][0].parent[0].hash))
    #         stateUtils.printState(dictionary[hash][0].parent[0].state)
    #     else:
    #         print("NO PARENT: ")

    # parent = dictionary[visited[-1]][0].parent[0]
    # finalPath = []
    # # Navigate through parent nodes to
    # # retrieve the path to the goal node.
    # while parent: 
    #     finalPath.append(parent)
    #     # print(parent[1])
    #     if hasattr(parent[0],'parent'):
    #         parent = dictionary[parent[0].hash][0]
    #         stateUtils.printState(parent[0].state)
    #     else:
    #         parent = None


        




    # src.Search.PrintSearchResults(dictionary, visited[-1], totalSecs)
   
