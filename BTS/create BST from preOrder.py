
def solve(preorder , mini , maxi , arr):
    if(arr[0] > len(preorder)-1):
        return None
    if(preorder[arr[0]] < mini or preorder[arr[0]] > maxi ):
        return None
    root = TreeNode(preorder[arr[0]])
    arr[0]=arr[0]+1
    root.left = solve(preorder , mini , root.data , arr)
    root.right = solve(preorder , root.data , maxi ,arr)

    return root

def preorderToBST(preorder):
    arr =[0]
    ans = solve(preorder , float('-inf') , float('inf') , arr)
    return ans