# learn about segmentation errors 

def solve(self,root):
        if(root == None):
            return [0,0]
            
        left = self.solve(root)
        right = self.solve(root)
        
        ans = [0,0]
        ans[0] = root.data + left[1] + right[1]
        ans[1] = max(left[0] , left[1]) + max(right[0] , right[1])
        
        return ans
        
    def getMaxSum(self,root):
        #code here
        ans = self.solve(root)
        return max(ans[0],ans[1])