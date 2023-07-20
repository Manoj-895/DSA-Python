#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here 
        stack =[]
        for i in range(n):
            stack.append(i)
        
        while(len(stack)!=1):
            a = stack[-1]
            stack.pop()
            b = stack[-1]
            
            stack.pop()
            
            if(M[a][b]==1):
                stack.append(b)
            else:
                stack.append(a)
                
        rowcheck =False
        rowcount =0
        colcheck = False
        colcount = 0
        cleb = stack[-1]
        for i in range(n):
            if(M[cleb][i] == 0):
                rowcount+=1
        for i in range(n):
            if(M[i][cleb]==1):
                colcount+=1
        # print(rowcount,colcount,n)
        if(colcount == n-1):
            colcheck= True
        if(rowcount == n):
            rowcheck = True
        if(rowcheck == True and colcheck == True):
            return cleb
        else:
            return -1
            
                
