from os import *
from sys import *
from collections import *
from math import *

def visiter():
    return False

def solve(node,visited,graph,stack):
    visited[node] = True
    for i in graph[node]:
        if(visited[i]==False):
            solve(i,visited,graph,stack)

    stack.append(node)
def topologicalSort(adj, v, e):
    graph = defaultdict(list)

    for i in range(e):
        a=adj[i][0]
        b=adj[i][1]
        graph[a].append(b)

    stack=[]
    visited = defaultdict(visiter)
    for i in range(v):
        if(visited[i]==False):
            solve(i,visited,graph,stack)
    ans = []
    while(len(stack)!=0):
        ans.append(stack[-1])
        stack.pop()

    return ans
        

