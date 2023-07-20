def solve(root,ok,node):
    if root is None:
        return None
        
    if(root.data == node):
        return root
        
    left = solve(root.left,ok,node)
    right = solve(root.right,ok,node)

    if(left !=None and right==None):
        ok[0] = ok[0]-1
        if(ok[0] <= 0):
            ok[0]=1000000
            return root
        return left
    if(left == None and right != None):
        ok[0] = ok[0]-1
        if(ok[0] <= 0):
            ok[0]=10000000
            return root
        return right
    return None
    

def kthAncestor(root,k, node):
    ok=[k]
    ans = solve(root,ok,node)
    if(ans == None or ans.data ==node ):
        return -1
    else:
        return ans.data