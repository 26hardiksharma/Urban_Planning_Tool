import networkx as nx

def solveDijkstra(G, startNode, endNode):
    try:
        path = nx.shortest_path(G, source=startNode, target=endNode, weight='weight')
        distance = nx.shortest_path_length(G, source=startNode, target=endNode, weight='weight')
        return {
            'path': " -> ".join(path), 
            'distance': distance
        }
    except nx.NetworkXNoPath:
        return {'path': "No path found.", 'distance': 0}
    except nx.NetworkXError as e:
        return {'path': f"Error: Invalid Node ({startNode} or {endNode})", 'distance': 0}