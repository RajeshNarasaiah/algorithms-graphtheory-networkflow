"""
Tarjan algo for finding strongly connected components.

2 cases:
1. Tree edge: low[u] = min( low[u], low[v] )
2. Back edge: low[u] = min( low[u], disc[v] )
"""
class TarjanSCC:
    graph = {}
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.time      = 0
        self.initialize()
        
    def initialize(self):
        for idx in range(self.num_nodes):
            self.graph[idx] = []
    
    def add_edge(self, frm, to):
        self.graph[frm].append(to)
    
    def print_graph(self):
        print(self.graph)
    
    def SCCUtil(self, vtx, low, disc, stkMember, stk):
        disc[vtx] = self.time
        low[vtx]  = self.time
        self.time += 1
        stkMember[vtx] = True
        stk.append(vtx)
        
        for neighbor in self.graph[vtx]:
            if disc[neighbor] == -1:
                #Case 1: tree edge. 
                self.SCCUtil(neighbor, low, disc, stkMember, stk)
                low[vtx] = min(low[vtx], low[neighbor])
            elif stkMember[neighbor] == True:
                #Case 2: back edge
                low[vtx] = min(low[vtx], disc[neighbor])
                
        w = -1
        if low[vtx] == disc[vtx]:
            #head of SCC
            while w != vtx:
                w = stk.pop()
                print(w)
                stkMember[w] = False
            print("")
            

    def SCC(self):
        
        disc      = [-1] * self.num_nodes
        low       = [-1] * self.num_nodes
        stkMember = [False] * self.num_nodes
        stk       = []
        
        for idx in range(self.num_nodes):
            if disc[idx] == -1:
                self.SCCUtil(idx, low, disc, stkMember, stk)
        
        
solver = TarjanSCC(5)
solver.add_edge(1, 0)
solver.add_edge(0, 2)
solver.add_edge(2, 1)
solver.add_edge(0, 3)
solver.add_edge(3, 4)
solver.print_graph()
solver.SCC()
