def printAdjacency(n, m, edges):                # coding nijas implementation using lists
    
    graph = [[] for i in range(n)]

    # Creating the graph.
    for i in range(m):

        # Adding adjecent nodes.
        graph[edges[i][0]].append(edges[i][1])
        graph[edges[i][1]].append(edges[i][0])

    # Create an adjacency list of size 'N'.
    adjacencyList = [[] for i in range(n)]

    for i in range(n):
        adjacencyList[i].append(i)

        for j in graph[i]:
            adjacencyList[i].append(j)

    return adjacencyList

# my implementation using dictionary
from os import *
from sys import *
from collections import *
from math import *

def printAdjacency(n, m, edges):
    graph = {}

    # Creating the graph.
    for i in edges:
        if(i[0] in graph.keys()):
            graph[i[0]].append(i[1])
        else:
            graph[i[0]]=[i[1]]
        if(i[1] in graph.keys()):
            graph[i[1]].append(i[0])
        else:
            graph[i[1]]=[i[0]]

           
    
    # print(graph)
    # Create an adjacency list of size 'N'.
    adjacencyList = [[] for i in range(n)]

    for i in range(n):
        adjacencyList[i].append(i)
        
        try:
            for j in graph[i]:
                adjacencyList[i].append(j)
        except:
            continue
    return adjacencyList





    


