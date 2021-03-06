import random

def getWeightedGraphAsAdjMatrix(numVert):
    if numVert < 5:
        return None
    graph = []
    for r in range(numVert):
        row = []
        for c in range(numVert):
            row.append( random.randint(1, 5000) )
        for i in range(0, 2):
            row[random.randint(0, len(row) - 1)] = None
        graph.append(row)
    return graph

def getWeightedGraphAsEdgeList(numVert):
    graphAdjMatrix = getWeightedGraphAsAdjMatrix(numVert)
    graph = []
    for row in graphAdjMatrix:
        newRow = filter(lambda x: x != None, row)
        graph.append(newRow)
    return graph

def getWeightedGraphAsEdgeDictionary(numVert):
    graphAdjMatrix = getWeightedGraphAsAdjMatrix(numVert)
    graph = {}
    for i in range(len(graphEdgeList)):
        graph[i] = {}
    for i in range(len(graphAdjMatrix)):
        for j in range(graphAdjMatrix[i]):
            if graphAdjMatrix[i][j] != None:
                graph[i][j] = graphAdjMatrix[i][j]
    return graph