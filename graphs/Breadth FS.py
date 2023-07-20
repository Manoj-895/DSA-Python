from os import *
from sys import *
from collections import *
from math import *
from collections import defaultdict
from collections import deque

def def_value():
    return False
def defvalue1():
    return []

def BFS(vertex, edges):
    def solve(graph , visited , ans , node):
        queue = deque()
        queue.append(node)
        visited[node] = True
        while(len(queue) != 0):
            frontnode = queue[0]
            queue.popleft()

            ans.append(frontnode)

            for i in graph[node]:
                if(visited[i] == False):
                    queue.append(i)
                    visited[i] = True


    graph = defaultdict(defvalue1)
    for i in range(len(edges[0])):
        graph[edges[0][i]].append(edges[1][i])
        graph[edges[1][i]].append(edges[0][i])
    
    for i in graph.values():
        i.sort()

    visited = defaultdict(def_value)
    ans = []
    for i in range(vertex):
        if(visited[i] == False):
            solve(graph , visited , ans , i)
   
    return ans