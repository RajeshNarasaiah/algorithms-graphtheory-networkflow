"""
Topological sort using KHAN's Algo:
Khan's alog finds a topological ordering by iteratively removing 
nodes in the graph which have no incoming edges. When a node is 
removed, it's added into the topological ordering and all it's edges 
are removed (decrementing in_degree for neighbors by 1) allowing for the 
next set of nodes with no incoming edges to be selected.

Once our of the while loop, if the len of topo_order != number of nodes 
in the graph, it implies there was a cycle.

Time: O(V + E)
"""
class TopologicalSortKhan:
    graph = {}
    topo_order = []
    visited = []
    in_degree = {}
    queue = []
    
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.initialize()
        
    def initialize(self):
        self.visited = [False] * self.num_nodes
        for idx in range(self.num_nodes):
            self.graph[idx] = []
            self.in_degree[idx] = 0
        
    def add_edge(self, frm, to):
        self.graph[frm].append(to)
        self.in_degree[to] += 1
            
    def print_graph(self):
        print(self.graph)
        print(self.in_degree)

    def topo_sort_Khan(self):
        for key in self.in_degree:
            if self.in_degree[key] == 0:
                self.queue.append(key)
        
        while self.queue:
            vtx = self.queue.pop(0)
            self.topo_order.append(vtx)
            
            for neighbor in self.graph[vtx]:
                self.in_degree[neighbor] -= 1
                if self.in_degree[neighbor] == 0:
                    self.queue.append(neighbor)
            
        if len(self.topo_order) != self.num_nodes:
            print("Detected a cycle !!")
            return
        
        print(self.topo_order)
     
        
solver = TopologicalSortAdjList(14)
solver.add_edge(0, 2)
solver.add_edge(0, 3)
solver.add_edge(0, 6)
solver.add_edge(1, 4)
solver.add_edge(2, 6)
solver.add_edge(3, 1)
solver.add_edge(3, 4)
solver.add_edge(4, 5)
solver.add_edge(4, 8)
solver.add_edge(6, 7)
solver.add_edge(6, 11)
solver.add_edge(7, 4)
solver.add_edge(7, 12)
solver.add_edge(9, 2)
solver.add_edge(9, 10)
solver.add_edge(10, 6)
solver.add_edge(11, 12)
solver.add_edge(12, 8)
solver.print_graph()
solver.topo_sort_Khan()
