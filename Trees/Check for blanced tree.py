# GFG problem babar annaa
class Solution:
    
    def fastBalance(self,root):
        if(root == None):
            return [True , 0]
        
        left = self.fastBalance(root.left)
        right = self.fastBalance(root.right)
        
        leftans  =  left[0]
        rightans = right[0]
        
        dif = (abs(left[1] - right[1])<= 1)
        
        ans = [0,0]
        ans[1]=max(left[1],right[1])+1
        if(leftans and rightans and dif):
            ans[0]=True
        else:
            ans[0]=False
        return ans
        
    
    def isBalanced(self,root):
        x=self.fastBalance(root)
        return x[0]
            