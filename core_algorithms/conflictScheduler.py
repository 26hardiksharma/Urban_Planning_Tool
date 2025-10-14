import math
import networkx as nx

CRITICAL_DISTANCE = 25.0 # Define the 25-unit threshold

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def solveConflictScheduler(allLocalities):
    
    # 1. Map raw locality data to (name, coords) structure
    points = []
    for p in allLocalities:
        points.append({'name': p['name'], 'coords': (p['x'], p['y'])}) 

    # 2. Build the Conflict Graph (Edge = Conflict)
    G_conflict = nx.Graph()
    for p in points:
        G_conflict.add_node(p['name'])

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = euclidean_distance(points[i]['coords'], points[j]['coords'])
            
            if dist < CRITICAL_DISTANCE:
                G_conflict.add_edge(points[i]['name'], points[j]['name'])
                
    # 3. Greedy Independent Set (Approximation)
    available_nodes = set(G_conflict.nodes())
    selected_set = []
    
    while available_nodes:
        best_node = None
        min_degree = float('inf')
        
        for node in available_nodes:
            # Convert iterator to set for intersection
            conflicting_neighbors_of_node = set(G_conflict.neighbors(node))
            
            degree = len(conflicting_neighbors_of_node & available_nodes)
            
            if degree < min_degree:
                min_degree = degree
                best_node = node

        if best_node is None:
            break
            
        selected_set.append(best_node)
        available_nodes.remove(best_node)
        
        conflicting_neighbors = set(G_conflict.neighbors(best_node))
        available_nodes -= conflicting_neighbors

    # NOTE: Keys are intentionally snake_case to match Python module standards.
    return {
        'total_selected': len(selected_set),
        'selected_areas': selected_set,
        'conflict_threshold': CRITICAL_DISTANCE
    }