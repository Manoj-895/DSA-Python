def LeftViewer(root,level,ans):
    if root is None:
        return
    
    if(level == len(ans)):
        ans.append(root.data)
        
    LeftViewer(root.left,level+1,ans)
    LeftViewer(root.right,level+1,ans)
    
def LeftView(root):
    
    ans = []
    level = 0
    LeftViewer(root,level,ans)
    return ans