from os import *
from sys import *
from collections import *
from math import *

def addans(ans,tracker,n):
    temp=[]
    for i in range(n):
        for j in range(n):
            temp.append(tracker[i][j])
    ans.append(temp)
            
def possible(tracker,row,col,n):
    x = row 
    y = col
    while(y > -1):
        if(tracker[x][y] == 1):
            return False
        y -= 1

    x = row 
    y = col
    while(y > -1 and x > -1):
        if(tracker[x][y] == 1):
            return False
        x -= 1
        y -= 1
    
    x = row 
    y = col
    while(y > -1 and x < n):
        if(tracker[x][y] == 1):
            return False
        x += 1
        y -= 1
        
    return True


def solve(col,ans,tracker,n):
    if(col == n):
        addans(ans,tracker,n)
        return
    
    for row in range(n):
        if(possible(tracker,row,col,n)):
            tracker[row][col]=1
            # print(tracker)
            solve(col + 1,ans,tracker,n)
            tracker[row][col]=0
    # print("end")
def nQueens(n):
    tracker = [[0 for i in range(n)] for j in range(n)]
    ans=[]
    solve(0,ans,tracker,n)
    return ans






    
