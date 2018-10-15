import time
import sys
import src.stateUtils as stateUtils
import src.Search

def execute(fileName):
    
    # # of steps taken in Random Walk
    N = 3
    # Get the initial state file from input
    inputStateFile = fileName
    # Read in the state file to a matrix
    state = stateUtils.readGameState(inputStateFile)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    print("Random Search")
    # Executes and prints the results of N moves in a 
    # Random Walk from the state passed in as the
    # first parameter
    src.Search.Random(state, N)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # Initialize the dictionary used as a gragh to store
    # the connected states.
    dictionary = {}
    # Start the start time to log the performance
    start = time.time()

    # Breadth-First Search
    # The closed set will be returned with the last element
    # in the closed set as the goal state.
    # The dictionary will be modified to contain all states visited
    # along with an array of connected states.
    visited = src.Search.BFS(dictionary, state)
    end = time.time()
    totalSecs = end - start
    
    src.Search.PrintSearchResults("Breadth-First Search", dictionary, visited, totalSecs)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    dictionary = {}
    start = time.time()
    # Depth-First Search
    # dictionary -- Dictionary containing a graph of the connected elements {hash, [Node, Node,...]}
    # state -- initial starting state of the game
    # -1 -- do not do an iterative depth-first search since the MAX_DEPTH is less than zero
    visited = src.Search.DFS(dictionary, state, -1)
    # Completed time to calculate total time.
    end = time.time()
    # Calculate total seconds to execute search
    totalSecs = end - start
    
    # Print the path (moves) used by navigating parents of nodes
    src.Search.PrintSearchResults("Depth-First Search", dictionary, visited, totalSecs)

        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    dictionary = {}
    start = time.time()
    # Initial MAX_DEPTH is 1 to search using an Iterative Depth-First search
    visited = src.Search.DFS(dictionary, state, 1)
    end = time.time()
    totalSecs = end - start

    src.Search.PrintSearchResults("Iterative Depth-First Search", dictionary, visited, totalSecs)



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    dictionary = {}
    start = time.time()
    # Uses a very simple heuristic that is guaranteed to be consistent
    # It uses a distance from the master node to the goal node as the 
    # heuristic metric. This is the shortest path from Master node to 
    # to the goal for any given state and presumes there is a unhindered
    # path to the goal. Minimum distance to the goal is prioritized first.
    visited = src.Search.AStar(dictionary, state)
    end = time.time()
    totalSecs = end - start
    
    src.Search.PrintSearchResults("A* Search", dictionary, visited, totalSecs)
