"""
Capacity Scaling implementation.

Algo:
 1. find delta , the largest power of 2 <= largest edge capacity in the initial flow graph.
 2. Find augmenting paths (using DFS) with remaining capacity >= delta until no more paths satisfy
    this criteria, then decrease the valye of delta by dividing it by 2 and repeat while delta > 0

graph is a dict of dict
{ frm1: { to1: [capacity, flow], to2: [capacity, flow], .. } 
  frm2: { to1: [capacity, flow], to2: [capacity, flow], .. } }
  
Time : O(E2log(U))
"""
import sys

class NetworkFlowSoverBase:
    class Edge:
        def __init__(self, capacity):
            #self.frm = frm
            self.capacity = capacity
            self.flow     = 0
            
        def isResidual(self):
            return self.capacity == 0
            
        def remainingCapacity(self):
            return self.capacity - self.flow
    
    graph = {}
    level = []
    largest_edge_capacity = float('-inf')
    
    def __init__(self, num_nodes, source, sink):
        self.num_nodes = num_nodes
        self.source    = source
        self.sink      = sink
        
            
    def addEdge(self, frm, to, capacity):
        if capacity < 0:
            raise Exception("invalid capacity")
        e1 = self.Edge(capacity)
        e2 = self.Edge(0)
        self.largest_edge_capacity = max( self.largest_edge_capacity, capacity )
        
        if frm not in self.graph:
            self.graph[frm] = {to : e1}
        elif frm in self.graph:
            self.graph[frm].update({to : e1})
        
        if to not in self.graph:
            self.graph[to] = {frm : e2}
        elif to in self.graph:
            self.graph[to].update({frm: e2})
        
    def printGraph(self):
        for idx in range(self.num_nodes):
            adj = self.graph[idx]
            print('idx: ', idx)
            for key in adj.keys():
                print('to: ', key, 'cap: ', adj[key].capacity,'flow: ', adj[key].flow)
                
   
    def getLargestPowerof2(self, n):
        if n < 1:
            return 0
            
        res = 1
        for idx in range( 8 * sys.getsizeof(n) ):
            curr = 1 << idx
            if curr > n:
                break
            res = curr
            
        return res
            
    def dfs(self, at, flow, visited, delta):
        if at == self.sink:
            return flow
    
        visited[at] = True
        adj_dict    = self.graph[at]
        print('d: ', delta)
        for key in adj_dict.keys():
            adj_edge = adj_dict[key]
            cap = adj_edge.remainingCapacity()
            if visited[key] == False and cap >= delta:
                visited[key] = True
                bottleneck = self.dfs(key, min(flow,cap), visited, delta)
                if bottleneck > 0:
                    adj_edge.flow += bottleneck
                    residual_edges = self.graph[key]
                    residual_edges[at].flow -= bottleneck
                    return bottleneck
                    
        return 0
        
    def capacity_scaling_solver(self):
        max_flow = 0
        delta = self.getLargestPowerof2( self.largest_edge_capacity )
        print(self.largest_edge_capacity)
        
        while delta > 0:
            flow = float('inf')
            while flow != 0:
                visited   = [False] * self.num_nodes
                flow      = self.dfs( self.source, float('inf'), visited, delta )
                max_flow += flow
            delta = delta // 2
            
        print('max_flow: ', max_flow)
        return max_flow
        
        
nodes = 6
s     = nodes - 1
t     = nodes - 2

solver = NetworkFlowSoverBase(nodes, s, t)



solver.addEdge(s, 0, 6);
solver.addEdge(s, 1, 14);


solver.addEdge(2, t, 11);
solver.addEdge(3, t, 12);


solver.addEdge(0, 1, 1);
solver.addEdge(2, 3, 1);
solver.addEdge(0, 2, 5);
solver.addEdge(1, 2, 7);
solver.addEdge(1, 3, 10);

#solver.printGraph()
solver.capacity_scaling_solver()
#solver.printGraph()
 
