"""
Finding Articulation Bridge in a graph using Tarjan,.

Time: O(v + E)
"""
class FindArticulationBridge():
    graph = {}
    bridge = []
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
            
        self.low = [-1] * self.num_nodes
        self.disc = [-1] * self.num_nodes
        self.parent = [-1] * self.num_nodes
        self.visited = [False] * self.num_nodes
        self.bridge = []
    
    def add_edge(self, frm, to):
        self.graph[frm].append(to)
        self.graph[to].append(frm)
    
    def print_graph(self):
        print(self.graph)
        
    def ABUtil(self, u):
        self.visited[u] = True
        self.low[u]     = self.time
        self.disc[u]    = self.time
        self.time   += 1
        for v in self.graph[u]:
            # If v is not visited yet, then make it a child of u
            # in DFS tree and recur for it
            if self.visited[v] == False :
                self.parent[v] = u
                self.ABUtil(v)
  
                # Check if the subtree rooted with v has a connection to
                # one of the ancestors of u
                self.low[u] = min(self.low[u], self.low[v])
  
  
                ''' If the lowest vertex reachable from subtree
                under v is below u in DFS tree, then u-v is
                a bridge'''
                if self.low[v] > self.disc[u]:
                    self.bridge.append([u,v])
      
                      
            elif v != self.parent[u]: # Update low value of u for parent function calls.
                self.low[u] = min(self.low[u], self.disc[v])
                
    def AB(self):
        for idx in range(self.num_nodes):
            if self.visited[idx] == False:
                self.ABUtil(idx)
        
        print(self.bridge)
                

solver = FindArticulationBridge(5)
solver.add_edge(1,0)
solver.add_edge(0,2)
solver.add_edge(2,1)
solver.add_edge(0,3)
solver.add_edge(3,4)

print('AB for graph 1: ')
solver.AB()

solver = FindArticulationBridge(4)
solver.add_edge(0,1)
solver.add_edge(1,2)
solver.add_edge(2,3)

print('AB for graph 2: ')
solver.AB()

solver = FindArticulationBridge(7)
solver.add_edge(0,1)
solver.add_edge(1,2)
solver.add_edge(2,0)
solver.add_edge(1,3)
solver.add_edge(1,4)
solver.add_edge(1,6)
solver.add_edge(3,5)
solver.add_edge(4,5)

print('AB for graph 3: ')
solver.AB()
