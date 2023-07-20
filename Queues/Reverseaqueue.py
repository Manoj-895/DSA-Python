
def solve(q , stack):
    if(q.empty() == True):
        return
    stack.append(q.get())
    solve(q,stack)
    temp = stack[-1]
    stack.pop()
    q.put(temp)
    



#Function to reverse the queue.
def rev(q):
    # stack = []
    # while(q.empty()!= True):
    #     stack.append(q.get())
    # while(len(stack) != 0):
    #     temp = stack[-1]
    #     stack.pop()
    #     q.put(temp)
    solve(q,[])
    return q