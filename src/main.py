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

    dictionary = {}
    start = time.time()
    visited = src.Search.BFS(dictionary, state)
    end = time.time()
    totalSecs = end - start
    
    src.Search.PrintSearchResults("Breadth-First Search", dictionary, visited, totalSecs)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    dictionary = {}
    start = time.time()
    visited = src.Search.DFS(dictionary, state, False, -1)
    end = time.time()
    totalSecs = end - start
    
    src.Search.PrintSearchResults("Depth-First Search", dictionary, visited, totalSecs)

        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    dictionary = {}
    start = time.time()
    visited = src.Search.DFS(dictionary, state, False, 1)
    end = time.time()
    totalSecs = end - start

    src.Search.PrintSearchResults("Iterative Depth-First Search", dictionary, visited, totalSecs)
