from collections import *
def shortestPath(edges, n, m, s, t):
    graph = defaultdict(list)
    for i in edges:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    visited = [False for i in range(n+1)]
    parent = [-1 for i in range(n+1)]

    q = deque()
    q.append(s)
    visited[s] = True
    while(len(q) != 0):
        front = q[0]
        q.popleft()

        for neighbour in graph[front]:
            if(visited[neighbour] == False):
                q.append(neighbour)
                visited[neighbour] = True
                parent[neighbour]= front
    
    currentNode = t
    ans = []
    ans.insert(0,currentNode)
    while(currentNode != s):
        currentNode = parent[currentNode]
        ans.insert(0,currentNode)
    return ans