stack = []
str = "manoj"
for i in str:
    stack.append(i)
i=0
ans = ""
print(stack)
while(i < len(str)):
    ans = ans + stack.pop()
    i+=1

print(ans)
