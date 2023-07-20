def findRedundantBrackets(s:str):
	stack = []
	for i in s:
		if(i == '(' or i == '+' or i == '-' or i == '*' or i == '/'):
			stack.append(i)
		else:
			if(i == ')'):
				isredundant = True
				while(stack[-1] != '('):
					top = stack[-1]
					if(top == '+' or top == '-' or top == '*' or top == '/'):
						isredundant = False
					stack.pop()

				if(isredundant == True):
					return True
				stack.pop()
	return False

print(findRedundantBrackets("((a+-b)*)"))