def modifyQueue(q,k):
    n= len(q)
    stack = []
    for i in range(k):
        stack.append(q.pop(0))
    
    while(len(stack)!=0):
        q.append(stack.pop())
    
    for i in range(n-k):
        q.append(q.pop(0))
    return q