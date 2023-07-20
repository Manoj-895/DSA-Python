from os import *
from sys import *
from collections import *
from math import *

def visiter():
    return False

def topologicalSort(adj, v, e):
    ans = []
    graph = defaultdict(list)

    for i in range(e):
        a=adj[i][0]
        b=adj[i][1]
        graph[a].append(b)
    
    indegree = [0 for i in range(v)]

    for i in graph:
        for j in graph[i]:
            indegree[j]+=1
    
    q=deque()

    for i in range(v):
        if(indegree[i]==0):
            q.append(i)

    while(len(q)!=0):
        front = q[0]
        q.popleft()
        ans.append(front)

        for neighbour in graph[front]:
            indegree[neighbour]-=1
            if(indegree[neighbour]==0):
                q.append(neighbour)
        
    return ans

        

