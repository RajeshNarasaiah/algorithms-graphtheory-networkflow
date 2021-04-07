"""
Finding Articulation points in a graph using Tarjan,.

2 cases for a node to be an articulation pt:
1. if u is a root and has atleast 2 children.
2. u is not a root and it has a child v such that no vertex in subtree rooted with v has 
   a back edge to an ancestor of u.
   
Time: O(v + E)
"""
class FindArticulationPts():
    graph = {}
    ap = []
    low = []
    disc = []
    visited = []
    parent = []
    
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.time = 0
        self.initialize()
        
    def initialize(self):
        for idx in range(self.num_nodes):
            self.graph[idx] = []
            
        self.ap = [False] * self.num_nodes
        self.low = [-1] * self.num_nodes
        self.disc = [-1] * self.num_nodes
        self.parent = [-1] * self.num_nodes
        self.visited = [False] * self.num_nodes
    
    def add_edge(self, frm, to):
        self.graph[frm].append(to)
    
    def print_graph(self):
        print(self.graph)
        
    def APUtil(self, u):
        children     = 0
        self.visited[u] = True
        self.low[u]     = self.time
        self.disc[u]    = self.time
        self.time   += 1
        
        for v in self.graph[u]:
            if self.visited[v] == False:
                self.parent[v] = u
                children += 1
                self.APUtil(v)
                
                self.low[u] = min( self.low[u], self.low[v] )
                
                #case 1: root with two or more children
                if self.parent[u] == -1 and children > 1:
                    self.ap[u] = True
                    
                #case 2: node with no back edges from its childre
                if self.parent[u] != -1 and self.low[v] >= self.disc[u]:
                    self.ap[u] = True
                    
            elif v != self.parent[u]:
                self.low[u] = min( self.low[u], self.disc[v] )
                
    def AP(self):
        for idx in range(self.num_nodes):
            if self.visited[idx] == False:
                self.APUtil(idx)
        
        for idx in range(self.num_nodes):
            if self.ap[idx] == True:
                print(idx)
                

solver = FindArticulationPts(5)
solver.add_edge(1,0)
solver.add_edge(0,2)
solver.add_edge(2,1)
solver.add_edge(0,3)
solver.add_edge(3,4)

print('AP for graph 1: ')
solver.AP()

solver = FindArticulationPts(4)
solver.add_edge(0,1)
solver.add_edge(1,2)
solver.add_edge(2,3)

print('AP for graph 2: ')
solver.AP()

solver = FindArticulationPts(7)
solver.add_edge(0,1)
solver.add_edge(1,2)
solver.add_edge(2,0)
solver.add_edge(1,3)
solver.add_edge(1,4)
solver.add_edge(1,6)
solver.add_edge(3,5)
solver.add_edge(4,5)

print('AP for graph 3: ')
solver.AP()
