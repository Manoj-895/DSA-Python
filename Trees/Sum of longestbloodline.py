def solve(self,root,ans,sum,h):
        if(root is None):
            if(h>ans[1]):
                ans[0]=sum
                ans[1]=h
            if(h==ans[1]):
                ans[0]=max(sum,ans[0])
                ans[1]=h
            return 
        sum = sum + root.data
        # print(sum)
        h=h+1
        self.solve(root.left,ans,sum,h)
        self.solve(root.right,ans,sum,h)
        

def sumOfLongRootToLeafPath(self,root):
    h=0
    sum=0
    ans=[0,0]
    self.solve(root,ans,sum,h)
    return ans[0]