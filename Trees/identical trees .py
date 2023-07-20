class Solution:
    #Function to check if two trees are identical. GFG
    def isIdentical(self,root1, root2):
        if(root1 == None and root2 == None):
            return True
        
        if(root1 != None and root2 == None):
            return False
        if(root1 == None and root2 != None):
            return False
            
        left = self.isIdentical(root1.left , root2.left)
        right = self.isIdentical(root1.right , root2.right)
        
        val = (root1.data == root2.data)
        if(left and right and val):
            return True
        else:
            return False

