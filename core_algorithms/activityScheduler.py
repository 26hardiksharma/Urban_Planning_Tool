import json
from collections import defaultdict

# Helper function to get names from the network data
def get_node_name_map():
    try:
        with open('data/city_network.json') as f:
            data = json.load(f)
        return {node['id']: node['name'] for node in data['nodes']}
    except:
        return {} # Return empty dict on error

# Redefined loadTrafficFlows to generate activities based on Nagpur IDs
def loadTrafficFlows():
    
    # We will generate six activities using the first six Nagpur Node IDs (N1 to N6)
    node_name_map = get_node_name_map()
    
    # Define the six flows using Node IDs N1 through N6
    raw_flows = [
        {"id": "N1", "start": 0, "finish": 25}, # Sitabuldi
        {"id": "N2", "start": 5, "finish": 15}, # Dharampeth
        {"id": "N3", "start": 15, "finish": 30}, # Civil Lines
        {"id": "N4", "start": 20, "finish": 40}, # Ramdaspeth
        {"id": "N5", "start": 35, "finish": 50}, # Lakadganj
        {"id": "N6", "start": 45, "finish": 55}  # Itwari
    ]
    
    # Map Node ID to Node Name for final display clarity
    flows = []
    for flow in raw_flows:
        flow_name = node_name_map.get(flow['id'], flow['id'])
        flows.append({
            'id': flow['id'],
            'name': flow_name,
            'start': flow['start'],
            'finish': flow['finish']
        })
        
    return flows

def solveActivityScheduling(flows):
    
    sortedFlows = sorted(flows, key=lambda x: x['finish'])
    
    selectedFlowObjects = []
    
    lastFinishTime = 0
    totalGreenTime = 0
    
    for flow in sortedFlows:
        if flow['start'] >= lastFinishTime:
            selectedFlowObjects.append(flow)
            lastFinishTime = flow['finish']
            totalGreenTime += (flow['finish'] - flow['start'])
            
    # Prepare output using the full name, not the generic ID
    selectedNames = [f['name'] for f in selectedFlowObjects]
    scheduleDetails = []
    
    for originalFlow in flows:
        flowID = originalFlow['id']
        flowName = originalFlow['name']
        start_t = originalFlow['start']
        finish_t = originalFlow['finish']
        
        status = "Selected" if flowName in selectedNames else "Rejected"
        
        detail = (
            f"{{'id': '{flowID}', 'name': '{flowName}', 'start': {start_t}, 'finish': {finish_t}}} ({start_t}s to {finish_t}s) - {status}"
        )
        scheduleDetails.append(detail)


    return {
        'totalGreenTime': totalGreenTime,
        'selectedFlows': selectedNames, # Now returns names
        'scheduleDetails': scheduleDetails 
    }