def findMinimumCost(str):
	if(len(str)%2 != 0):
		return -1
	stack = []
	for i in str:
		if(i == '{'):
			stack.append(i)
		else:
			if(len(stack) != 0 and stack[-1] == '{'):
				stack.pop()
			else:
				stack.append(i)
	a=0
	b=0
	while(len(stack) != 0):
		if(stack[-1] == '{'):
			a+=1
			stack.pop()
		else:
			b+=1
			stack.pop()

	return (a+1)//2 +(b+1)//2

print(findMinimumCost("{{{}}{}{"))