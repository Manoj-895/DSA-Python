# 1 2 4 -1 -1 5 -1 -1 3 6 -1 -1 7 -1 -1
from collections import deque
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.count = 0
    
    def addchild(self,newNode , q):
    
        x=q[0]
        q.popleft()
        newNode = Node(x)
        if(newNode.data == -1):
            return None
        
        # print("adding child to left")
        newNode.left = self.addchild(newNode.left , q)
        # print("adding child to right")
        newNode.right = self.addchild(newNode.right , q)

        return newNode
    
    def levelOrderTraversal(self, root):
        q = deque()
        q.append(root)
        while(len(q)!=0):
            temp = q[0]
            print(temp.data ,end=" ")
            q.popleft()
            if(temp.left != None):
                q.append(temp.left)
            if(temp.right != None):
                q.append(temp.right)
    # In order LNR , pre order NLR , Post order LRN 

    def InorderTraversal(self,root):
        if(root == None):
            return
        self.InorderTraversal(root.left)
        if(root.left == None and root.right == None):
            self.count += 1
        self.InorderTraversal(root.right)

        return self.count

    def PreorderTraversal(self,root):
        if(root == None):
            return
        
        print(root.data , end=" ")
        self.PreorderTraversal(root.left)
        self.PreorderTraversal(root.right)
    
    def PostorderTraversal(self,root):
        if(root == None):
            return
        
        self.PostorderTraversal(root.left)
        self.PostorderTraversal(root.right)
        print(root.data , end=" ")

        
    
x=Node(10)
q = deque([1,2, 4, -1, -1, 5, -1, -1, 3, 6, -1, -1, 7, -1, -1])
root=x.addchild(None , q)
x.levelOrderTraversal(root)
print(' ')
print(x.InorderTraversal(root),"leaf node")
print(' ')
x.PreorderTraversal(root)
print(' ')
x.PostorderTraversal(root)
