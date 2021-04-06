"""
Topological sort using DFS:
Applicable only for DAG (Directed Acyclic graphs).
Provides an ordering of vertices along a horizontal line so that 
all directed edges for from left to right.

Algo:
1. Call DFS() to process each vertex.
2. As each vertex is finished, insert it into a list.
3. Return the list in reverse.

Time: O(V + E)
"""
class TopologicalSortAdjList:
    graph = {}
    topo_order = []
    visited = []
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.initialize()
        
    def initialize(self):
        self.visited = [False] * self.num_nodes
        for idx in range(self.num_nodes):
            self.graph[idx] = []
        
    def add_edge(self, frm, to):
        self.graph[frm].append(to)
            
    def print_graph(self):
        print(self.graph)
        print(self.visited)
        
    def dfs(self, vtx):
        if self.visited[vtx] == True:
            return
        
        self.visited[vtx] = True
        
        for neighbor in self.graph[vtx]:
            if self.visited[neighbor] == False:
                self.dfs(neighbor)
                
        self.topo_order.append(vtx)
        
    
    def topo_sort(self):
        for idx in range(self.num_nodes):
            self.dfs(idx)
            
        print(self.topo_order[::-1])
     
        
solver = TopologicalSortAdjList(7)
solver.add_edge(0, 1)
solver.add_edge(0, 2)
solver.add_edge(0, 5)
solver.add_edge(1, 3)
solver.add_edge(1, 2)
solver.add_edge(2, 3)
solver.add_edge(2, 4)
solver.add_edge(3, 4)
solver.add_edge(5, 4)
solver.print_graph()
solver.topo_sort()
