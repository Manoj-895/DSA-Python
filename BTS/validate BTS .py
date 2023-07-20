def isBST(root , min , max):
    if(root == None):
        return True
    if(root.data >= min and root.data <= max):
        left = isBST(root.left , min , root.data)
        right = isBST(root.right , root.data , max)
        return left and right
    else:
        return False
        
def validateBST(root):
    
    min = float('-inf')
    max = float('inf')
    return isBST(root , min ,max)