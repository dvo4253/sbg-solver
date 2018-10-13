# Sliding Block Puzzle Solver



### Files

#### main.py

Contains one method used to execute all searching methods and produce the output. Reads in a file as a paramenter that contains the state. The state is stored as a m x n matrix including the dimensions on the first row.

The following search methods are executed on a graph representing the relation between a current state, and all immediate future states based off of the possible moves from the current state. 

---
- Random

- Breadth-First Search

- Depth-First Search

- Iterative Depth-First Search

- A* Search


#### Move.py

Contains a class representing a move in the game. The data stored is a block ID and a direction. The direction is maintained by an enumeration which is also maintained in this file. Also simple comparison operations are implemented prioritized by ID and then my direction of the move.

#### Node.py
Class used to maintain a Node within the graph structure. Each node contains all relevant data for a game state and valid moves. A hash is created from a concatenated string of the matrix. If the state is normalized then this hash is sufficient. Comparisons are implemented for use within a priority queue. The distance property on the determines the priority on the queue.


#### Queue.py
Simple queue structure to use with standard operations.


#### Search.py
Contains each of the main methods to exeucte a search for a solution of the sliding block puzzle.

-   __Random (Take a Random Walk)__
    1) For each state generate the list of valid moves. 
    2) Choose one using a uniformly random variable.
    3) Execute the move, generating a new state.
    4) Repeat until the max number of searches has been reached or the goal has been reached.

-   __BFS (Breadth-First)__
    Generate a list of moves and future game states and add them to a FIFO queue. Dequeue and explore a state if it has not already been explored. Add any generated states to the queeu and repeat. A Node object is used to store the state, a hash, list of valid moves and a parent node if applicable.

-   __DFS (Depth-First & Iterative Depth-First)__
    Generate a list of moves. Explore the state generated  from the first move recursively. When no valid moves are possible or all generated states have already been visited the recurrsion will back out, exploring the next move on the previous node. The nodes are popped off a stack and explored LIFO. 
    For the iterative depth-first search, generate a list of moves. Explore the nodes utilizing the same depth-first technique previously until the specified depth is reached.

-   __AStar__
    Moves are generated from the initial state. After this a simple heuristic (distance master block is from goal) is calculated for each possible future state. States to check and explore and orderd by the heuristic metric in a priority queue.


#### stateUtils.py




