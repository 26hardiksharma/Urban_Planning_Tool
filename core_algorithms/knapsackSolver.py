def solveKnapsack(projects, maxBudget):
    if maxBudget <= 0 or len(projects) == 0:
        return {
            'selectedProjects': [],
            'totalBenefit': 0,
            'totalCost': 0,
            'remainingBudget': maxBudget
        }
    
    projectsWithRatio = []
    for project in projects:
        cost = project['cost']
        benefit = project['benefit']
        if cost > 0:
            ratio = benefit / cost
            projectsWithRatio.append({
                'name': project['name'],
                'cost': cost,
                'benefit': benefit,
                'ratio': ratio
            })
    
    projectsWithRatio.sort(key=lambda x: x['ratio'], reverse=True)
    
    selectedProjects = []
    totalCost = 0
    totalBenefit = 0
    remainingBudget = maxBudget
    
    for project in projectsWithRatio:
        if totalCost + project['cost'] <= maxBudget:
            selectedProjects.append(project['name'])
            totalCost += project['cost']
            totalBenefit += project['benefit']
            remainingBudget -= project['cost']
    
    return {
        'selectedProjects': selectedProjects,
        'totalBenefit': totalBenefit,
        'totalCost': totalCost,
        'remainingBudget': remainingBudget
    }