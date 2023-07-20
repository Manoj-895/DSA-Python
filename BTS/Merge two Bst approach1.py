# merge two sorted arrays to create a sorted array then create BST by the aew array
class TreeNode:
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right

def createArr(root , ans):
    if(root == None):
        return
    
    createArr(root.left , ans)
    ans.append(root.data)
    createArr(root.right ,ans)    

def sortingArrs(ans1 , ans2):
    arr=[]
    i=0
    j=0
    while(i<len(ans1) and j<len(ans2)):
        if(ans1[i] < ans2[j]):
            arr.append(ans1[i])
            i+=1
        else:
            arr.append(ans2[j])
            j+=1
    while(i <len(ans1)):
        arr.append(ans1[i])
        i+=1
    while(j < len(ans2)):
        arr.append(ans2[j])
        j+=1
    
    return arr

def createBSt(ans , s, e):
    if(s > e):
        return None
    
    mid = (s+e)//2
    root = TreeNode(ans[mid])
    root.left = createBSt(ans, s , mid -1)
    root.right = createBSt(ans , mid+1 , e )
    return root
    

def mergeBST(root1, root2):
	# Write your code here.
    ans1= []
    createArr(root1 , ans1)
    ans2 = []
    createArr(root2 ,ans2)
    ans = sortingArrs(ans1 , ans2)
    s=0
    e=len(ans)-1
    root = createBSt(ans , s, e)
    return root