from heap import * # Heap, HeapWithDecreaseKey

class DijkstrasShortestPath:

    def __init__(self):
        pass
    
    def findPath(self, startNode, endNode, edgeListGraph):

        distance = {x: float("inf") for x in range(len(edgeListGraph))}
        distance[startNode] = 0

        h = Heap(lambda a, b: distance[a] < distance[b])
        h.pushItem(startNode)

        seen = {} # nodes in shortest path
        
        parent = {} # Track parents to rebuild route on completion
        parent[startNode] = None

        while True:

            currentNode = h.popItem()
            currentCost = distance[currentNode] if currentNode in distance else float("inf")

            if currentNode == endNode:
                break

            if currentNode in seen:
                continue
            seen[currentNode] = True

            for nextNode, weight in edgeListGraph[currentNode]:

                if nextNode in seen:
                    continue

                nodeCost = currentCost + weight
                knownDistance = distance[nextNode] if nextNode in distance else float("inf")

                if nodeCost < knownDistance:
                    distance[nextNode] = nodeCost
                    h.pushItem(nextNode)
                    parent[nextNode] = currentNode
        
        path = []
        currentNode = endNode
        while currentNode in parent:
            path.append(currentNode)
            currentNode = parent[currentNode]
        path = list(reversed(path))

        return path

    def tryGetDistance(self, distance, a, b):
        value = float("inf")
        try:
            value = distance[a][b]
        except:
            if a not in distance:
                distance[a] = {}
            if b not in distance[a]:
                distance[a][b] = value
        return value

class DijkstrasShortestPathWithDecreaseKey:

    def __init__(self):
        pass
    
    def findPath(self, startNode, endNode, edgeListGraph):

        distance = {x: float("inf") for x in range(len(edgeListGraph))}
        distance[startNode] = 0

        h = HeapWithDecreaseKey(lambda a, b: distance[a] < distance[b])
        h.pushItem(startNode)

        seen = {} # nodes in shortest path
        
        parent = {} # Track parents to rebuild route on completion
        parent[startNode] = None

        while True:

            currentNode = h.popItem()
            currentCost = distance[currentNode] if currentNode in distance else float("inf")

            if currentNode == endNode:
                break

            if currentNode in seen:
                continue
            seen[currentNode] = True

            for nextNode, weight in edgeListGraph[currentNode]:

                if nextNode in seen:
                    continue

                nodeCost = currentCost + weight
                knownDistance = distance[nextNode] if nextNode in distance else float("inf")

                if nodeCost < knownDistance:
                    distance[nextNode] = nodeCost
                    h.decreaseKey(nextNode)
                    parent[nextNode] = currentNode
        
        path = []
        currentNode = endNode
        while currentNode in parent:
            path.append(currentNode)
            currentNode = parent[currentNode]
        path = list(reversed(path))

        return path

    def tryGetDistance(self, distance, a, b):
        value = float("inf")
        try:
            value = distance[a][b]
        except:
            if a not in distance:
                distance[a] = {}
            if b not in distance[a]:
                distance[a][b] = value
        return value