from collections import *


def solve(node,parent,graph,disc,low,visited,timer,result):
    visited[node]=True
    disc[node] = timer[0]
    low[node] = timer[0]
    timer[0] = timer[0]+1
    child = 0
    for neigbour in graph[node]:
        if(neigbour == parent):
            continue
        
        if(visited[neigbour]==False):
            solve(neigbour,node,graph,disc,low,visited,timer,result)
            low[node]=min(low[neigbour],low[node])
            if(low[neigbour] >= disc[node] and parent != -1):
                ans = [node]
                result.append(ans)
            child+=1

        else:
            low[node] = min(low[node],disc[neigbour])
    if(parent == -1 and child >1):
        result.append(node)

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