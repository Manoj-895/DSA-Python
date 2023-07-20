class Solution:
    #Function to return list containing elements of right view of binary tree.
    def RightViewer(self,root,level,ans):
        if root is None:
            return
        
        if(level == len(ans)):
            ans.append(root.data)
        
        self.RightViewer(root.right,level+1,ans)
        self.RightViewer(root.left,level+1,ans)
        
    def rightView(self,root):
        
        ans = []
        level = 0
        self.RightViewer(root,level,ans)
        return ans