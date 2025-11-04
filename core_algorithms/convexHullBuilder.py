from scipy.spatial import ConvexHull
import json

def buildConvexHull(points):
    if len(points) < 3:
        return {'error': 'Need at least 3 points to build a hull.', 'area': 0, 'hullPointsStr': ''}
    
    coords = [(p['x'], p['y']) for p in points]
    
    try:
        hull = ConvexHull(coords)
        
        hull_points = [points[i] for i in hull.vertices]
        
        hull_points_str = "\n".join([f"{p['name']}: ({p['x']}, {p['y']})" for p in hull_points])
        
        area = hull.volume
        
        return {
            'area': round(area, 2),
            'hullPointsStr': hull_points_str,
            'numVertices': len(hull.vertices)
        }
    except Exception as e:
        return {'error': str(e), 'area': 0, 'hullPointsStr': ''}
