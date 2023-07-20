from collections import *


def solve(node,parent,graph,disc,low,visited,timer,result):
    visited[node]=True
    disc[node] = timer[0]
    low[node] = timer[0]
    timer[0] = timer[0]+1
    for neigbour in graph[node]:
        if(neigbour == parent):
            continue
        
        if(visited[neigbour]==False):
            solve(neigbour,node,graph,disc,low,visited,timer,result)
            low[node]=min(low[neigbour],low[node])
            if(low[neigbour] > disc[node]):
                ans = [node , neigbour]
                result.append(ans)

        else:
            low[node] = min(low[node],disc[neigbour])

def findBridges(edges, v, e):
    graph = defaultdict(list)
    for i in edges:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    disc = [-1 for i in range(v)]
    low = [-1 for i in range(v)]
    visited = [False for i in range(v)]
    parent = -1
    result = []
    timer=[0]
    for i in range(v):
        if(visited[i]==False):
            solve(i,parent,graph,disc,low,visited,timer,result)
    
    return result

