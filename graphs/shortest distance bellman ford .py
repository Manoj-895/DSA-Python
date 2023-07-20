from os import *
from sys import *
from collections import *
from math import *


# good for negative cycle

def bellmonFord(n, m, src, dest, edges):
    distance = [1000000000 for i in range(n+1)]
    distance[src] = 0
    for i in range(1,n+1):
        for j in range(m):
            u = edges[j][0]
            v = edges[j][1]
            w = edges[j][2]

            if(distance[u]!=1000000000 and (distance[u] + w )<distance[v]):
                distance[v] = distance[u]+w
    
    # check for negative cycle
    flag = 0
    for j in range(m):
            u = edges[j][0]
            v = edges[j][1]
            w = edges[j][2]

            if(distance[u]!=1000000000 and (distance[u] + w )<distance[v]):
                flag = 1
    if(flag == 0):
        return distance[dest]
    return -1
