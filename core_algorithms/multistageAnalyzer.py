import json
import networkx as nx

# Note: The functionality has been simplified to use Dijkstra's on the whole graph
#       because the complex N-stage structure is not compatible with the N1-N50 data.

def solveMultistage(data, startNodeID, endNodeID):
    """
    Finds the minimum cost path between two nodes (N1 to N50) by treating 
    the network as a general shortest path problem using NetworkX (Dijkstra's).
    """
    
    G_project = nx.DiGraph()
    
    # Build the full graph G_project using all nodes/edges from the JSON
    for node in data['nodes']:
        G_project.add_node(node['id'], name=node['name'])
        
    # Edges are treated as bidirectional costs in the DiGraph.
    for u, v, w in data['edges']:
        G_project.add_edge(u, v, weight=w)
        G_project.add_edge(v, u, weight=w)
        
    
    try:
        path = nx.shortest_path(G_project, source=startNodeID, target=endNodeID, weight='weight')
        cost = nx.shortest_path_length(G_project, source=startNodeID, target=endNodeID, weight='weight')
        
        return {
            'totalCost': cost,
            'optimalPath': " -> ".join(path)
        }
        
    except nx.NetworkXNoPath:
        return {
            'totalCost': float('inf'),
            'optimalPath': f"ERROR: No valid path found from {startNodeID} to {endNodeID}."
        }
    except nx.NodeNotFound as e:
        return {
            'totalCost': float('inf'),
            'optimalPath': f"ERROR: Invalid node ID used in start/end: {e}"
        }

def loadNetworkEdgesOnly():
    with open('data/city_network.json') as f:
        return json.load(f)