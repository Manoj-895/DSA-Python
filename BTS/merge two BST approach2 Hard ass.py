from os import *
from sys import *
from collections import *
from math import *

class TreeNode:
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right

def sortDLL(head1,head2):
    head = None
    tail = None
    while(head1 != None and head2 != None):
        if(head1.data <= head2.data):
            if(head == None):
                head = head1
                tail = head1
                head1 = head1.right
            else:
                tail.right = head1
                head1.left = tail
                tail = head1
                head1 = head1.right

        else:
            if(head == None):
                head = head2
                tail = head2
                head2 = head2.right
            else:
                tail.right = head2
                head2.left = tail
                tail = head2
                head2 = head2.right
    while(head1 != None):
        tail.right = head1
        head1.left = tail
        tail = head1
        head1 = head1.right
    while(head2 != None):
        tail.right = head2
        head2.left = tail
        tail = head2
        head2 = head2.right

    return head



def mergeBST(root1, root2):
    def createDDLL(root):
        nonlocal head
        if(root == None):
            return None
        createDDLL(root.right)
        root.right = head
        if head!= None:
            head.left = root

        head = root
        createDDLL(root.left)

    def createBST(n):
        nonlocal mainHead
        if( n <= 0 or mainHead == None):
            return None
        left = createBST(n//2)
        root = mainHead
        root.left = left
        mainHead = mainHead.right

        root.right = createBST(n-n//2-1)
        return root

    head=None
    createDDLL(root1)
    head1 =head
    head1.left = None
    head=None
    createDDLL(root2)
    head2=head
    head2.left = None
    mainHead = sortDLL(head1 , head2)
    count = 0
    temp = mainHead
    while(temp!=None):
        count = count+1
        # print(temp.data)
        temp= temp.right
    ans = createBST(count)
    return ans
    

    





