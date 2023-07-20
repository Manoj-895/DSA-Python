def solve(root , sumarr):
    if(root == None):
        return None
    # print(root.data)
    solve(root.left , sumarr)
    sumarr.append(root.data)
    solve(root.right , sumarr)



def twoSumInBST(root, target):
    # Write your code here
    sumarr = []
    solve(root , sumarr)
    n = len(sumarr)
    i,j=0,n-1
    while(i<j):
        if(sumarr[i] + sumarr[j] == target):
            return True
        if(sumarr[i] + sumarr[j] > target):
            j-=1
        if(sumarr[i] + sumarr[j] < target):
            i+=1
    return False   