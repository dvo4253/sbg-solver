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
    # of moves are made.
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
        
        # Increment the move count to
        # ensure we keep it under the max # of moves
        move_count += 1

# ******************************************************************************
#   Description:   Creates and utilized Breadth-First Search to navigate a graph created from the 
#                  starting state of the Sliding Block Puzzle. 
#             
#                  1) A node representing the initial state of the puzzle is added to the queue
#                  2) While there are nodes in the fringe state queue and the goal has not been reached
#                     dequeue a node from the queue
#                  3) Check if the node is in the closed set (visited array) Continue evaluating the
#                     state if it hasn't been visited. Otherwise get the next node from the queue
#                  4) Check if it is a goal state
#                  5) Generate moves from the state
#                  6) For each move generate the resulting states, create a Node object 
#                     and add it to the queue.
#                  7) Add the node to the dictionary to create the graph relationship between
#                     the current state and the resulting states.
#                  8) Repeat steps 2 - 7 
#
#   Paremeters:    graph --      Dictionary to keep track of the graph representing the states
#                                and connected states. 
#                                   Key: A hash of the state matrix.
#                                   Value: An array of Nodes representing the connected states
#
#                  startState -- Matrix (same format as the initial file) representing the
#                                starting state of the sliding block puzzle           
#
# ******************************************************************************
def BFS(graph, startState):

    # FIFO Queue used to keep track of the fringe state to explore
    queue = Queue()
    # 1) A node representing the initial state of the puzzle is added to the queue
    currentNode = Node(startState)
    graph[currentNode.hash] = [currentNode]

    queue.enqueue(currentNode)
    visited = []

    i = 0
    inGoal = False
    # 2) While there are nodes in the fringe state queue and the goal has not been reached
    #    dequeue a node from the queue
    while (queue.size() > 0 and not inGoal):

        node = queue.dequeue()
        # 3) Check if the node is in the closed set (visited array) Continue evaluating the
#            state if it hasn't been visited. Otherwise get the next node from the queue
        if (node.hash not in visited):
            i += 1
            # The node is now visited
            visited.append(node.hash)
            # 4) Check if it is a goal state
            inGoal = stateUtils.inGoalCheck(node.state)
            # 5) Generate moves from the state
            moves = stateUtils.getValidMoves(node.state)
            # Relate the current node to the list of valid moves from the state
            # represented by the node
            node.moves = moves
            # 6) For each move generate the resulting states, create a Node object 
            #    and add it to the queue.
            for move in moves:
                childState = stateUtils.makeMove(node.state, move)
                childNode = Node(childState)
                # parent is a tuple containing the node and the move
                # required to get to the child from the node.
                childNode.parent = (node, move)
                queue.enqueue(childNode)
                # 7) Add the node to the dictionary to create the graph relationship between
                #    the current state and the resulting states.
                if (node.hash not in graph.keys()):
                    graph[node.hash] = [node, childNode]
                else:
                    graph[node.hash].append(childNode)

    # The end result is an array of visited nodes
    # The last node in the array is the node representing the goal state.
    # The graph object is updated and can be referened by the calling function.
    return visited
    

# ******************************************************************************
#   Description:   Creates and utilized Depth-First Search to navigate a graph 
#                  created from the starting state of the Sliding Block Puzzle. 
#                  This function will be used as the stating point for both the 
#                  Depth-First Search and the Interative Depth-First Search.
#                   
#
#   Paremeters:    
#                  graph --      Dictionary to keep track of the graph representing the states
#                                and connected states. 
#                                   Key: A hash of the state matrix.
#                                   Value: An array of Nodes representing the connected states
#
#                  startState -- Matrix (same format as the initial file) representing the
#                                starting state of the sliding block puzzle           
#
#                  inGoal:      Indicates of the goal state has been found.
#
#                  MAX_DEPTH:   Indicates the initial max depth for an iterative depth-first
#                               search. If the value is less than zero a pure depth-first
#                               search will be done.
#                       
#                       Valid Values:
#                               True  -- Use an iterative approach startting at
#                                        height 1 and increasing by 1
#                               False -- Search using a pure depth-first approach.
# ******************************************************************************
def DFS(graph, startState, inGoal, MAX_DEPTH):

    current_depth = 0

    while (not inGoal):
        visited = []
        inGoal = DFSHelper(graph, startState, inGoal, visited, MAX_DEPTH, current_depth)
        MAX_DEPTH += 1

    return visited


# ******************************************************************************
#   Description:   Helper function doing most of the leg-work of the depth-first
#                  search. Recursively called to search 
#                   
#
#   Paremeters:    
#                  graph --      Dictionary to keep track of the graph representing the states
#                                and connected states. 
#                                   Key: A hash of the state matrix.
#                                   Value: An array of Nodes representing the connected states
#
#                  startState -- Matrix (same format as the initial file) representing the
#                                starting state of the sliding block puzzle           
#
#                  inGoal:      Indicates of the goal state has been found.
#
#                  visited:     An array of hashes representing the states (nodes) previously
#                               visited. Represents the closed set.
#                  
#                  MAX_DEPTH:   Indicates the current maxiume depth for an iterative depth-first
#                               search. If the value is less that zero then a pure depth-first
#                               approach will be used.
#                  
#                  current_depth: Current depth. Compared with the MAX_DEPTH to determine
#                               if the max depth has been reached during an iterative approach.
# ******************************************************************************
def DFSHelper(graph, state, inGoal, visited, MAX_DEPTH, current_depth):

    currentNode = Node(state)
    moves = stateUtils.getValidMoves(state)

    while moves and not inGoal:
        move = moves.pop()
        childState = stateUtils.makeMove(state, move)
       
        childNode = Node(childState)

        inGoal = stateUtils.inGoalCheck(childState)

        childNode.parent = (currentNode, move)
        if (currentNode.hash not in graph.keys()):
            graph[currentNode.hash] = [currentNode, childNode]
        else:
            graph[currentNode.hash].append(childNode)

        if (childNode.hash not in graph.keys()):
            graph[childNode.hash] = [childNode]

        if (childNode.hash not in visited and not inGoal and (MAX_DEPTH < 0 or current_depth < MAX_DEPTH)):
            visited.append(childNode.hash)
            inGoal = DFSHelper(graph, childState, inGoal, visited, MAX_DEPTH, current_depth + 1)
        elif (inGoal):
            visited.append(childNode.hash)

    return inGoal

def PrintSearchResults(label, dictionary, visited, totalSecs):
    goalNode = dictionary[visited[-1]][0]
    node = goalNode
    parentHash = node.parent[0].hash
    parentMove = node.parent[1]

    print()
    print(label)

    finalPath = [ parentMove ]
    while parentHash != None:
        node = dictionary[parentHash][0]
        
        if hasattr(node,'parent'):
            finalPath.append(node.parent[1])
            parentHash = node.parent[0].hash
        else:
            parentHash = None
        
    for move in reversed(finalPath):
        print(move)
    
    stateUtils.printState(goalNode.state)

    print(str(len(dictionary)) + " " + str(round(totalSecs, 5)) + " " + str(len(finalPath)))