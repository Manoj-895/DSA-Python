from collections import *

def solve(node,visited,transpose):
    visited[node] = True
    
    for nigh in transpose[node]:
        if(visited[nigh] == False):
            solve(nigh , visited , transpose)
    

def dfs(node,visited,graph,stack):
    visited[node] = True

    for nigh in graph[node]:
        if(visited[nigh] == False ):
            dfs(nigh , visited , graph , stack)

    stack.append(node)

def stronglyConnectedComponents(v, edges):
    graph = defaultdict(list)
    for i in edges:
        graph[i[0]].append(i[1])
    stack=[]
    visited = [False for i in range(v)]
    for i in range(v):
        if(visited[i] == False):
            dfs(i,visited,graph,stack)
    visited = [False for i in range(v)]
    transpose = defaultdict(list)
    for i in edges:
        transpose[i[1]].append(i[0])
    
    count=0
    while(len(stack) != 0):
        node = stack[-1]
        stack.pop()
        if(visited[node] == False):
            solve(node,visited,transpose)
            count+=1
    return count

    