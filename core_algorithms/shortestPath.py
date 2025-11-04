import heapq

def solveDijkstra(graph, startNode, endNode):
    nodes = graph['nodes']
    edges = graph['edges']
    
    node_ids = [node['id'] for node in nodes]
    
    if startNode not in node_ids or endNode not in node_ids:
        return {'path': f"Error: Invalid Node ({startNode} or {endNode})", 'distance': 0}
    
    adjacency = {}
    for node in nodes:
        adjacency[node['id']] = []
    
    for u, v, weight in edges:
        adjacency[u].append((v, weight))
        adjacency[v].append((u, weight))
    
    distances = {node: float('inf') for node in node_ids}
    predecessors = {node: None for node in node_ids}
    
    distances[startNode] = 0
    
    priorityQueue = [(0, startNode)]
    visited = set()
    
    while priorityQueue:
        currentDistance, currentNode = heapq.heappop(priorityQueue)
        
        if currentNode in visited:
            continue
        
        visited.add(currentNode)
        
        if currentNode == endNode:
            break
        
        for neighbor, weight in adjacency[currentNode]:
            distance = currentDistance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = currentNode
                heapq.heappush(priorityQueue, (distance, neighbor))
    
    if distances[endNode] == float('inf'):
        return {'path': "No path found.", 'distance': 0}
    
    path = []
    current = endNode
    while current is not None:
        path.append(current)
        current = predecessors[current]
    
    path.reverse()
    
    return {
        'path': " -> ".join(path), 
        'distance': distances[endNode]
    }