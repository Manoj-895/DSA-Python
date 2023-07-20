#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def traverseLeft(self,root,ans):
        if(root == None or (root.left == None and root.right == None)):
            return
        ans.append(root.data)
        if(root.left):
            self.traverseLeft(root.left, ans)
        else:
            self.traverseLeft(root.right,ans)
    def leafnode(self,root,ans):
        if(root == None):
            return
        if(root.left==None and root.right ==None):
            ans.append(root.data)
            return
        
        self.leafnode(root.left,ans)
        self.leafnode(root.right,ans)
        
    def traversalright(self,root,ans):
        if(root == None or (root.left == None and root.right == None)):
            return
        if(root.right):
            self.traversalright(root.right,ans)
        else:
            self.traversalright(root.left,ans)
        
        ans.append(root.data)

    
    def printBoundaryView(self, root):
        ans=[]
        if(root == None):
            return ans
        ans.append(root.data)
        self.traverseLeft(root.left,ans)
        self.leafnode(root.left,ans)
        self.leafnode(root.right,ans)
        self.traversalright(root.right,ans)
        return ans
