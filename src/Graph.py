
class Graph: 
    # Constructor 
    def __init__(self, Node):
        self.graph = [] 
        # 

    def addNewEdge(self, id, node):
        self.graph[id].append(node)