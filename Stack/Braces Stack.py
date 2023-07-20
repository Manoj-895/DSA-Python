def isValidParenthesis(expression):

    # Write your code here.
    stack = []
    for i in expression:
        if( i == '{' or i == '(' or i == '['):
            stack.append(i)
        else:
            if(len(stack) != 0):
                brace = stack[-1]
                if(i == '}' and brace == '{' or
                   i == ')' and brace == '(' or
                   i == ']' and brace == '['):
                    stack.pop()
                else:
                    return False
            else:
                return False
    if(len(stack)) == 0:
        return True
    else:
        return False

# Main Code

t = int(input().strip())

for i in range(t):
    str = input().strip()
    ans = isValidParenthesis(str)

    if ans:
        print("Balanced")
        
    else:
        print("Not Balanced")
