from collections import *
def detectCycleInDirectedGraph(n, edges):
    graph = defaultdict(list)
    for i in edges:
        graph[i[0]].append(i[1])
    
    indegree = [0 for i in range(n+1)]
    indegree[0]='a'
    
    for i in graph:
        for j in graph[i]:
            indegree[j]+=1
    
    q = deque()

    for i in range(n+1):
        if(indegree[i]==0):
            q.append(i)
    count = 0
    while(len(q)!=0):
        front = q[0]
        q.popleft()

        count += 1

        for neighbour in graph[front]:
            indegree[neighbour]-=1
            if(indegree[neighbour]==0):
                q.append(neighbour)
    
    if(count == n):
        return False
    else:
        return True