def solve(inputStack,N,count):
    if(count == N//2):           # // floor division  int(15/2)  == 15//2
        inputStack.pop()
        return
    
    num = inputStack[-1]        # to get top element in python 
    inputStack.pop()
    solve(inputStack,N,count+1)
    inputStack.append(num)        # to push to stack in python

def deleteMiddle(inputStack, N):

    # Write your solution here
    count = 0
    solve(inputStack,N,count)
    print(inputStack)

deleteMiddle([1,2,3,4,5,6],6)