from os import *
from sys import *
from collections import *
from math import *

def solve(myStack , x):
	if(len(myStack) == 0):
		myStack.append(x)
		return myStack
	
	num = myStack[-1]
	myStack.pop()
	solve(myStack , x)
	myStack.append(num)


def pushAtBottom(myStack: deque, x: int):
	solve(myStack , x)
	return myStack