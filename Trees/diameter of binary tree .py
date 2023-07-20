# gfg question plzzz g through     or else done h000geee

class Solution:
    
    def diafast(self,root):
        if(root == None):
            return [0,0]
        left=self.diafast(root.left)
        right=self.diafast(root.right)
        
        op1 = left[0]
        op2 = right[0]
        
        op3 = left[1] + right[1] + 1
        
        ans=[0,0]
        ans[0] = max(op1,max(op2,op3))
        ans[1] = max(left[1],right[1])+1
        return ans
        
    #Function to return the diameter of a Binary Tree.
    def diameter(self,root):
        # Code here
        x = self.diafast(root)
        return x[0]