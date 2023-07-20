from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)



# Edge class for storing the Edges of thee graph
class Edge:
    
    def __init__(self, start, end, weight) :

        self.start = start
        self.end = end
        self.weigth = weight

def findparent(parent,node):
    if(parent[node] == node):
        return node
    
    parent[node] = findparent(parent,parent[node])
    return parent[node]

def unionSet(u,v,parent,rank):
    u = findparent(parent , u)
    v = findparent(parent,v)
    
    if(rank[u] < rank[v]):
        parent[u]=v
    elif(rank[v] < rank[u]):
        parent[v]=u
    else:
        parent[v]=u
        rank[u]+=1  

    
def minimumSpanningTree(edges, V, E):
    edges.sort(key= lambda x:x.weigth)
    parent = [i for i in range(V)]
    rank = [0 for i in range(V)]
    minWit=0
    for i in range(len(edges)):
        u = findparent(parent,edges[i].start)
        v = findparent(parent,edges[i].end)
        weight = edges[i].weigth
        if(u!=v):
            minWit += weight
            unionSet(u,v,parent,rank)
    
    return minWit