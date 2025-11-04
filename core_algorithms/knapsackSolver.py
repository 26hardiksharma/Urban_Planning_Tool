import numpy as np

def solveKnapsack(projects, maxBudget):
    n = len(projects)
    
    if maxBudget <= 0 or n == 0:
        return {
            'selectedProjects': [],
            'totalBenefit': 0,
            'totalCost': 0,
            'remainingBudget': maxBudget
        }
    
    dp = np.zeros((n + 1, maxBudget + 1), dtype=int)
    
    for i in range(1, n + 1):
        project = projects[i - 1]
        cost = project['cost']
        benefit = project['benefit']
        
        for w in range(maxBudget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - cost] + benefit)
            else:
                dp[i][w] = dp[i-1][w]
    
    selectedProjects = []
    w = maxBudget
    totalCost = 0
    
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            project = projects[i - 1]
            selectedProjects.append(project['name'])
            totalCost += project['cost']
            w -= project['cost']
    
    selectedProjects.reverse()
    
    totalBenefit = dp[n][maxBudget]
    remainingBudget = maxBudget - totalCost
    
    return {
        'selectedProjects': selectedProjects,
        'totalBenefit': totalBenefit,
        'totalCost': totalCost,
        'remainingBudget': remainingBudget
    }