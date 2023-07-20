class   TreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right

def solve(root,inArr):
    if(root == None):
        return None
    
    solve(root.left , inArr)
    inArr.append(root)
    solve(root.right , inArr)



def flatten(root):
    inArr=[]
    solve(root, inArr)
    n=len(inArr)
    root = inArr[0]
    i=0
    while(i < n-1):
        inArr[i].left = None
        inArr[i].right = inArr[i+1]
        i+=1
    inArr[i].left=None
    inArr[i].right=None

    return root