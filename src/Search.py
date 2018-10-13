import random
import time
import src.stateUtils as stateUtils
from src.Node import Node
from src.Queue import Queue
import heapq

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
#                                > 0  -- Use an iterative approach starting at
#                                        height MAX_DEPTH. MAX_DEPTH will increase by 
#                                        1 until the goal is found.
#                                < 0  -- Search using a pure depth-first approach.
# ******************************************************************************
def DFS(graph, startState, MAX_DEPTH):
    inGoal = False
    current_depth = 0
    visited = []
    # The loop is only needed for the iterative depth-first search otherwise 
    # just call DFSHelper once.
    if (MAX_DEPTH < 0):
        inGoal = DFSHelper(graph, startState, False, visited, MAX_DEPTH, current_depth)
    else:
        while (not inGoal):
            visited = []
            inGoal = DFSHelper(graph, startState, False, visited, MAX_DEPTH, current_depth)
            
            # Increment the MAX_DEPTH for an Iterative Depth-First approach
            MAX_DEPTH += 1
    
    # The visited array will contain the list of all visited nodes with the 
    # last element being the goal node
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

    # Create the Node object from state passed in.
    currentNode = Node(state)
    # Get valid moves from the state
    moves = stateUtils.getValidMoves(state)

    # If the goal has not been reach then iterate through
    # each move. Because DFSHelper is called recursively for 
    # each move we will navigate down through each child node
    # before exploring the adjacent move
    while moves and not inGoal:
        move = moves.pop()
        childState = stateUtils.makeMove(state, move)
       
        childNode = Node(childState)

        # Check if the generated node is the goal
        inGoal = stateUtils.inGoalCheck(childState)

        # Set the child nodes parent as the current node
        # and the move required to navigate to the child
        # node from the parent.
        # This is stored in tupal
        childNode.parent = (currentNode, move)
        # Either create the graph entry or added the child
        # to the graph entry to store nodes
        # connected to the current node.
        if (currentNode.hash not in graph.keys()):
            graph[currentNode.hash] = [currentNode, childNode]
        else:
            graph[currentNode.hash].append(childNode)

        # Added the child to the graph as well
        if (childNode.hash not in graph.keys()):
            graph[childNode.hash] = [childNode]

        # This is only difference in the pure depth-first search and an 
        # iterative depth-first search.
        # Only explore the child node of the following conditions have been met
        # 1)  Child node has not been explored
        # 2)  The child node is not the goal node
        # 3)  Either we are not doing an iterative depth-first search (MAX_DEPTH < 0)
        # 4)  Or the current depth is less than the MAX_DEPTH
        if (childNode.hash not in visited and not inGoal and (MAX_DEPTH < 0 or current_depth < MAX_DEPTH)):
            visited.append(childNode.hash)
            inGoal = DFSHelper(graph, childState, inGoal, visited, MAX_DEPTH, current_depth + 1)
        elif (inGoal):
            # If we are at the goal node just append
            # the hash as the last hash in closed set.
            # This will always be our goal node in the end.
            visited.append(childNode.hash)

    return inGoal


# ******************************************************************************
#   Description:   Creates and utilized Breadth-First Search to navigate a graph created from the 
#                  starting state of the Sliding Block Puzzle. 
#             
#                  1) A node representing the initial state of the puzzle is added to the queue
#                  2) While there are nodes in the fringe state queue and the goal has not been reached
#                     dequeue the top Node from the heap queue
#                  3) Check if the node is in the closed set (visited array) Continue evaluating the
#                     state if it hasn't been visited. Otherwise get the next top node from 
#                     the priority queue
#                  4) Check if it is a goal state
#                  5) Generate moves from the state
#                  6) For each move generate the resulting states, create a Node object 
#                     and push it on to the priority queue.
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
def AStar(graph, startState):

    # An arry used to keep track of the fringe state to explore
    # 
    queue = []
    # Get the location of the goal to use in heuristic
    # functions
    goalSpaces = stateUtils.findGoal(startState)

    # 1) A node representing the initial state of the puzzle is added to the queue
    currentNode = Node(startState)
    # Retrive a number that represents the distance from the goal.
    # The Node comparison functions will use this value to 
    currentNode.goalDistance = stateUtils.checkMasterPath(startState, goalSpaces)
    graph[currentNode.hash] = [currentNode]

    # Use the Python heapq module to create the priority queue
    heapq.heappush(queue,currentNode)

    visited = []

    i = 0
    inGoal = False

    # 2) While there are nodes in the fringe state queue and the goal has not been reached
    #    dequeue a node from the queue
    while (len(queue) > 0 and not inGoal):

        i = 0
       
        node = heapq.heappop(queue)
        # 3) Check if the node is in the closed set (visited array) Continue evaluating the
        #    state if it hasn't been visited. Otherwise get the next node from the priority queue
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

                childNode.distance = stateUtils.checkMasterPath(childState, goalSpaces)
                # childNodes.append(childNode)
                # 7) Add the node to the dictionary to create the graph relationship between
                #    the current state and the resulting states.
                if (node.hash not in graph.keys()):
                    graph[node.hash] = [node, childNode]
                else:
                    graph[node.hash].append(childNode)

                heapq.heappush(queue,childNode)

    # The end result is an array of visited nodes
    # The last node in the array is the node representing the goal state.
    # The graph object is updated and can be referened by the calling function.
    return visited
    
# ******************************************************************************
#   Description:   Walks back through the connected nodes from the last node evaluated (Goal State)
#                  to print the path to reach the goal
#             
#                  
#   Paremeters:    label      --    Label to print specifying the method of search done.
#                  dictionary --    Dictionary containing Node hashes as keys and an array
#                                   of Nodes connected to the Node represented by the key
#
#                  visited    --    A list of Node hashes for each state visiited
#                  
#                  totalSecs  --    Total number of seconds elapsed while doing the search
#                   
# ******************************************************************************
def PrintSearchResults(label, dictionary, visited, totalSecs):
    # The last node entered in the visited array is the goal node
    # We need to navigate through it's parents to print the path
    goalNode = dictionary[visited[-1]][0]
    node = goalNode

    # If a Node has a parent it is represented by a tuple that 
    # contains the parent Node and the move used to get from the parent
    # (Node, Move)
    parentHash = node.parent[0].hash
    parentMove = node.parent[1]

    print()
    print(label)

    finalPath = [ parentMove ]
    # While there is a parent hash navigate up through
    # the parents and add it to the finalPath list.
    while parentHash != None:
        # The first value in the dictionary is always the 
        # the Node represented by the hash given as the key.
        # Get the Node from the dictionary.
        node = dictionary[parentHash][0]
        
        # If the node has a parent add it to the finalPath list
        if hasattr(node,'parent'):
            # The parent is a tupal of (Node, move)
            # Represents the parent state and the move 
            # used to navigate from the parent to the child
            # We just need to move to print so just append the move
            # to the finalPath list
            finalPath.append(node.parent[1])

            # Set the parent
            parentHash = node.parent[0].hash
        else:
            parentHash = None
    
    # Reverse the order to print the list of moves from beginning
    for move in reversed(finalPath):
        print(move)
    
    # Print the final state 
    stateUtils.printState(goalNode.state)

    # Print metrics on the execution of the search
    #                                                                  # of Moves from Initial 
    # # of Explored Nodes              # Total Seconds to Execute        State to the goal node
    print(str(len(dictionary)) + " " + str(round(totalSecs, 5)) + " " + str(len(finalPath)))