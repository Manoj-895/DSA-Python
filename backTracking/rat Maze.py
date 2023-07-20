from os import *
from sys import *
from collections import *
from math import *

def isOktomove(tracker,x,y,n,arr):
    if( -1 < x < n and -1 < y < n and tracker[x][y] != 1 and arr[x][y] == 1 ):
        return True
    else:
        return False 

def solve(tracker,arr,n,x,y,string,ans):
    if(x==n-1 and y==n-1):
        ans.append(string)
        return
    
    tracker[x][y]=1
    if(isOktomove(tracker,x+1,y,n,arr)):
        solve(tracker,arr,n,x+1,y,string + 'D',ans)
    
    if(isOktomove(tracker,x,y-1,n,arr)):
        solve(tracker,arr,n,x,y-1,string + 'L',ans)
    
    if(isOktomove(tracker,x,y+1,n,arr)):
        solve(tracker,arr,n,x,y+1,string + 'R',ans)

    if(isOktomove(tracker,x-1,y,n,arr)):
        solve(tracker,arr,n,x-1,y,string + 'U',ans)
    
    tracker[x][y]=0
    

def searchMaze(arr, n):
    if(arr[0][0] == 0):
        return []
    tracker=[[0 for i in range(n)]for j in range(n)]
    ans=[]
    string = ""
    solve(tracker,arr,n,0,0,string, ans)
    return ans

arr=[[1,0],[1,1]]
n=2
searchMaze(arr, n)