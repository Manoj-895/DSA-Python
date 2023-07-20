def solve(root , k, i):
  if(root == None):
    return -1
  
  left = solve(root.left , k ,i )

  if(left != -1):
    return left
  
  i[0]= i[0]+1
  if(i[0]==k):
    return root.data
  
  else:
    return solve(root.right , k ,i)

def kthSmallest(root, k):

    # Write your code here
    # Return the value of 'k-th' smallest node.
    i=[0]
    return solve(root , k ,i)
