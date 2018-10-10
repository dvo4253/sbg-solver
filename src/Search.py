import random
import time
import src.stateUtils as stateUtils
from src.Node import Node
from src.Queue import Queue

def Random(initialState, N):
    MAX_MOVES = N
    move_count = 0
    currentState = initialState

    # Print the initial state
    stateUtils.printState(currentState)

    # Continue Randomly until either the goal is found or the maximum number
    # of the moves are made.
    while(not stateUtils.inGoalCheck(currentState) and move_count < MAX_MOVES):
        # Get list of valid moves from the current state
        moves = stateUtils.getValidMoves(currentState)
        
        # Randomly select a move
        selectedMove = random.randint(0,len(moves) - 1)
        
        print(str(moves[selectedMove]))
        print()
        # Execute the move and retrieve the next state.
        # State is normalized already
        currentState = stateUtils.makeMove(currentState, moves[selectedMove])

        stateUtils.printState(currentState)
        
        move_count += 1
    
    
    

    
def BFS(graph, startState):
    queue = Queue()

    currentNode = Node(startState)
    
    graph[currentNode.hash] = [currentNode]
    queue.enqueue(currentNode)
    visited = []

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
                childNode = Node(childState)
                # parent is a tuple containing the move and the node
                childNode.parent = (node, move)
                queue.enqueue(childNode)
                if (node.hash not in graph.keys()):
                    graph[node.hash] = [node, childNode]
                else:
                    graph[node.hash].append(childNode)

    return visited
    

def DFS(graph, startState, inGoal):
    queue = Queue()

    currentNode = Node(startState)
    
    graph[currentNode.hash] = [currentNode]
    # queue.enqueue(currentNode)
    visited = []

    # i = 0

    # moves = stateUtils.getValidMoves(startState)
    # for move in moves:
    #     print(move)
    
    # for hash in visited:
    #     print("Hash: " + hash)

    DFSHelper(graph, startState, inGoal, visited)

    # print("FINAL STATE: ")
    # print(visited[-1])
    # stateUtils.printState(graph[visited[-1]]c[0].parent[0].state)
    return visited


def DFSHelper(graph, state, inGoal, visited):

    currentNode = Node(state)
    moves = stateUtils.getValidMoves(state)
    
    # c


    while moves and not inGoal:
        move = moves.pop()
        childState = stateUtils.makeMove(state, move)
        # cinput("Press Enter to continue...")
        # stateUtils.printState(childState)
        childNode = Node(childState)

        inGoal = stateUtils.inGoalCheck(childState)


        childNode.parent = (currentNode, move)
        if (currentNode.hash not in graph.keys()):
            graph[currentNode.hash] = [currentNode, childNode]
        else:
            graph[currentNode.hash].append(childNode)

        if (childNode.hash not in graph.keys()):
            graph[childNode.hash] = [childNode]


        # if (inGoal):
            # print("Goal Hash:")
            # print(childNode.hash)
            # stateUtils.printState(childState)
            # PrintSearchResults(graph, childNode.hash, 5)


        if (childNode.hash not in visited and not inGoal):
            visited.append(childNode.hash)
            inGoal = DFSHelper(graph, childState, inGoal, visited)
        elif (inGoal):
            visited.append(childNode.hash)

    # print(visited)
    return inGoal

def PrintSearchResults(graph, goalStateHash, totalSecs):
    # Item 0 is the node itself
    parent = graph[goalStateHash][0].parent
    finalPath = []
    # Navigate through parent nodes to
    # retrieve the path to the goal node.
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
        # stateUtils.printState(result[0].state)
        print(result[1])

    stateUtils.printState(graph[goalStateHash][0].state)

    print(str(len(graph)) + " " + str(round(totalSecs, 5)) + " " + str(pathLength))