
from collections import defaultdict
from collections import deque

# def lister():
#     return []
def visiter():
    return False

def findPath(node,graph,visited):
    parent = {}
    parent[node] = -1
    q=deque()
    q.append(node)
    visited[node]=True
    while(len(q) != 0):
        front = q[0]
        q.popleft()

        for i in graph[front]:
            if(visited[i] == True and parent[front] != i ):
                return True
            elif(visited[i] == False):
                q.append(i)
                visited[i]=True
                parent[i]=front


def cycleDetection(edges, n, m):
    graph = defaultdict(list)

    for i in edges:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    visited=defaultdict(visiter)
    for j in range(n):
        if(visited[j] == False):
            ans = findPath(j,graph, visited)
            if(ans == True):
                return "Yes"
    return "No"










