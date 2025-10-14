from scipy.spatial import ConvexHull
import numpy as np

def buildConvexHull(pointsList):
    coords = [(p['x'], p['y']) for p in pointsList]
    points = np.array(coords)
    
    if len(points) < 3:
        return {'hullPointsStr': "Requires at least 3 points.", 'area': 0, 'error': "Requires at least 3 points."}
        
    try:
        hull = ConvexHull(points)
        
        hullPointsIndices = hull.vertices
        hullPointsInfo = [pointsList[i] for i in hullPointsIndices]
        
        hullPointsStr = [f"{p['name']} ({p['x']}, {p['y']})" for p in hullPointsInfo]
        
        return {
            'hullPointsStr': "\n".join(hullPointsStr),
            'area': round(hull.area, 2),
            'error': None
        }
    except Exception as e:
        return {'hullPointsStr': "Calculation failed.", 'area': 0, 'error': f"Hull calculation failed: {e}"}