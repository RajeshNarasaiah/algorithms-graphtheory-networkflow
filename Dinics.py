"""
Network flow - Dinic's algo implementation.

Algo:
 1. Create a level graph using BFS from soruce to sink.
    Level graph: edges going from level l to l+1 with remaining capacity > 0
 2. If the sink was never reachable while building the level graph, then stop and return max
    flow.
 3. Using valid edges from level graph, do multiple dfs runs from source -> sink unitl a 
    blocking flow is reached. Sum over all the bottleneck values of the augmenting paths
    to calculate total max_flow.
    
    blocking flow: no more flow can be sent using level graph. Dead ends, vertices already visited,
                   no path to sink.

graph is a dict of dict
{ frm1: { to1: [capacity, flow], to2: [capacity, flow], .. } 
  frm2: { to1: [capacity, flow], to2: [capacity, flow], .. } }
  
Time : O(EV2)
"""
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
    def __init__(self, num_nodes, source, sink):
        self.num_nodes = num_nodes
        self.source    = source
        self.sink      = sink
        
            
    def addEdge(self, frm, to, capacity):
        if capacity < 0:
            raise Exception("invalid capacity")
        e1 = self.Edge(capacity)
        e2 = self.Edge(0)
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
                
   
    def build_level_graph(self):
        # all edges going from level l to l + 1 with remaining capacity > 0
        self.level = [-1] * self.num_nodes
        self.level[self.source] = 0
        queue = []
        queue.append(self.source)
        while queue:
            node = queue.pop(0)
            adj_dict = self.graph[node]
            for key in adj_dict.keys():
                edge    =  adj_dict[key]
                rem_cap = edge.remainingCapacity()
                if rem_cap > 0 and self.level[key] == -1:
                    self.level[key] = self.level[node] + 1
                    queue.append(key)
                    
        print('source: ', self.source)
        print('sink: ', self.sink)
        print(self.level)
        return self.level[self.sink] != -1
            
    def dfs(self, at, nxt, flow, visited):
        if at == self.sink:
            return flow
    
        visited[at] = True
        adj_dict    = self.graph[at]
        for key in adj_dict.keys():
            adj_edge = adj_dict[key]
            cap = adj_edge.remainingCapacity()
            if visited[key] == False and self.level[key] == self.level[at] + 1 and cap > 0:
                visited[key] = True
                bottleneck = self.dfs(key, nxt, min(flow,cap), visited)
                if bottleneck > 0:
                    adj_edge.flow += bottleneck
                    residual_edges = self.graph[key]
                    residual_edges[at].flow -= bottleneck
                    return bottleneck
                    
        return 0
        
    def dinic_solver(self):
        nxt = []
        max_flow = 0
        while self.build_level_graph():
            visited = [False] * self.num_nodes
            flow = float('inf')
            while flow != 0:
                flow = self.dfs( self.source, nxt, float('inf'), visited)
                max_flow += flow
                
        print('max_flow: ', max_flow)
        return max_flow
        
        
nodes = 11
s     = nodes - 1
t     = nodes - 2

solver = NetworkFlowSoverBase(nodes, s, t)


solver.addEdge(s, 0, 5);
solver.addEdge(s, 1, 10);
solver.addEdge(s, 2, 15);

solver.addEdge(0, 3, 10);
solver.addEdge(1, 0, 15);
solver.addEdge(1, 4, 20);
solver.addEdge(2, 5, 25);
solver.addEdge(3, 4, 25);
solver.addEdge(3, 6, 10);
solver.addEdge(3, 7, 20);
solver.addEdge(4, 2, 5);
solver.addEdge(4, 7, 30);
solver.addEdge(5, 7, 20);
solver.addEdge(5, 8, 10);
solver.addEdge(7, 8, 15);


solver.addEdge(6, t, 5);
solver.addEdge(7, t, 15);
solver.addEdge(8, t, 10);

#solver.printGraph()
solver.dinic_solver()
#solver.printGraph()
 
