from typing import *
from collections import defaultdict

"""
    Time complexity : O(Vlog(V) + E )
    Space complexity : O(V+E)
    where V is the number of vertex and E is the number of edges in graph

"""
def defvalue1():
    return []
def defvalue():
    return False

def depthFirstSearchHelper(vertex, visited, singleComponent, gra):
    visited[vertex] = True
    singleComponent.append(vertex)

    for child in gra[vertex]:

        # Check if the node is visited before or not.
        if visited[child] == False:
            depthFirstSearchHelper(child, visited, singleComponent, gra)


def depthFirstSearch(V, E, edges):

    # Creating Adjacency Matrix.
    gra = defaultdict(defvalue1)
    for a, b in edges:
        gra[a].append(b)
        gra[b].append(a)

    components = []
    visited = defaultdict(defvalue)

    for vertex in range(V):

        if visited[vertex] == False:
            singleComponent = []
            depthFirstSearchHelper(vertex, visited, singleComponent, gra)
            singleComponent.sort()
            components.append(singleComponent)

    return components