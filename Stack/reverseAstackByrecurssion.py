from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def addatBottom(stack , x):
	if(len(stack) == 0):
		stack.append(x)
		return stack
	
	num = stack[-1]
	stack.pop()
	addatBottom(stack , x)
	stack.append(num)
	return

def reverseStack(stack):
	if(len(stack) == 0):
		return stack

	num = stack[-1]
	stack.pop()
	reverseStack(stack)
	addatBottom(stack , num)
