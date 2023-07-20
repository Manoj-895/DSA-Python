from collections import defaultdict
def visiter():
    return False

def solve(node , visited , dfsvisited , graph):
    visited[node] = True
    dfsvisited[node]=True

    for child in graph[node]:
        if(visited[child] == False):
            cycle = solve(child,visited,dfsvisited,graph)
            if(cycle == True):
                return True
        elif(dfsvisited[child]== True):
            return True
    dfsvisited[node]=False
    return False


def detectCycleInDirectedGraph(n, edges):
    graph = defaultdict(list)
    for i in edges:
        graph[i[0]].append(i[1])
    visited = defaultdict(visiter)
    dfsvisited = defaultdict(visiter)
    for i in range(n):
        if(visited[i] == False):
            ans = solve(i,visited,dfsvisited,graph)
            if(ans == True):
                return True
    return False
    
