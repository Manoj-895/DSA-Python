from os import *
from sys import *
from collections import *
from math import *

def calculatePrimsMST(n, m, g):
    graph = defaultdict(list)
    for i in range(m):
        u=g[i][0]
        v=g[i][1]
        w=g[i][2]
        graph[u].append([v,w])
        graph[v].append([u,w])

    distance = [float('inf') for i in range(n+1)]
    visited = [False for i in range(n+1)]
    parent = [-1 for i in range(n+1)]
    
    distance[1]=0
    for node in range(1,n+1):
        mini= float('inf')
        for i in range(1,n+1):
            if(visited[i]==False and distance[i]<mini):
                u=i
                mini = distance[i]

        visited[u]=True     
        for it in graph[u]:
            v=it[0]
            w=it[1] 
            if(visited[v] == False and w<distance[v]):
                distance[v] = w
                parent[v] = u
    
    ans = []
    for i in range(2,n+1):
        ans.append([i,parent[i],distance[i]])


    return ans