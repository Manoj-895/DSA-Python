from collections import *

def topologicalSort(node,visited,stack,graph):
    visited[node]=True

    for neighbour in graph[node]:
        if(visited[neighbour[0]] == False):
            topologicalSort(neighbour[0],visited,stack,graph)
    
    stack.append(node)


graph = defaultdict(list)

graph[4].append([5,-2])
graph[3].append([4,-1])
graph[2].append([3,7])
graph[2].append([4,4])
graph[2].append([5,2])
graph[1].append([2,2])
graph[1].append([3,6])
graph[0].append([1,5])
graph[0].append([2,3])

n=6
stack =[]
visited = [False for i in range(n)]

for i in range(n):
    topologicalSort(i,visited,stack,graph)

distance = [float('inf') for i in range(n)]
source = 1
distance[source]=0

while(len(stack)!=0):
    top=stack[-1]
    stack.pop()
    if(distance[top] != float('inf')):
        for i in graph[top]:
            if(distance[top] + i[1] < distance[i[0]]):
                distance[i[0]]= distance[top]+i[1]

print(distance)