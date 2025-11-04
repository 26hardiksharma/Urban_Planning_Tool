class UnionFind:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        
        if root1 == root2:
            return False
        
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1
        
        return True

def buildMST(graph):
    nodes = graph['nodes']
    edges = graph['edges']
    
    node_ids = [node['id'] for node in nodes]
    
    sorted_edges = sorted(edges, key=lambda e: e[2])
    
    uf = UnionFind(node_ids)
    mstEdges = []
    totalCost = 0
    
    for u, v, weight in sorted_edges:
        if uf.union(u, v):
            mstEdges.append((u, v, weight))
            totalCost += weight
            
            if len(mstEdges) == len(node_ids) - 1:
                break
    
    edgeList = [f"({u} - {v}) Cost: {weight}" for u, v, weight in mstEdges]
    
    return {
        'cost': totalCost,
        'edges': edgeList
    }