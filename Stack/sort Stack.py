from os import *
from sys import *
from collections import *
from math import *

def insertinSortedOrder(stack ,num):
    if(len(stack) == 0 or stack[-1] <= num):
        stack.append(num)
        return
    topval = stack[-1]
    stack.pop()
    insertinSortedOrder(stack,num)
    stack.append(topval)
    

def sortStack(stack):
    # given data structure is a python list 
    # as list have all the similar operations available so use them
    # Write your code here
    if(len(stack)== 0):
        return
    
    num = stack[-1]
    stack.pop()
    sortStack(stack)
    insertinSortedOrder(stack,num)
