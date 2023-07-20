
from collections import defaultdict
from collections import deque

# def lister():
#     return []
def visiter():
    return False

def findPath(node,graph,visited,par):
    visited[node] = True
    for child in graph[node]:
        if(visited[child] == False):
            cyle = findPath(child,graph,visited,node)
            if(cyle):
                return True
        elif(child != par):
            return True
    return False

def cycleDetection(edges, n, m):
    graph = defaultdict(list)

    for i in edges:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    visited=defaultdict(visiter)
    for j in range(n):
        if(visited[j] == False):
            ans = findPath(j,graph, visited,-1)
            if(ans == True):
                return "Yes"
    return "No"










