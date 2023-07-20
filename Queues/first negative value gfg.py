from collections import deque

def printFirstNegativeInteger( A, N, K):
    # code here
    ans = []
    q=deque()
    for i in range(K):
        if(A[i]<0):
            q.append(i)
    
    if(len(q)!=0):
        ans.append(A[q[0]])
    else:
        ans.append(0)

    for i in range(K,N):
        if(len(q) !=0 and i - q[0] >= K):
            q.popleft()
        
        if(A[i]<0):
            q.append(i)
        if(len(q)!=0):
            ans.append(A[q[0]])
        else:
            ans.append(0)
        
    return ans