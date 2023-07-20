# from Inorder array means sorted array
class Solution:
    def creatBst(self,start , end , arr):
        if(start > end ):
            return None
    
        mid = (start + end)//2
        root = Node(arr[mid])
        root.left = self.creatBst(start , mid -1 , arr)
        root.right = self.creatBst(mid +1 , end , arr)

        return root

    def solve(self ,root ,arr):
        if(root == None):
            return None
    
        self.solve(root.left ,arr )
        arr.append(root.data)
        self.solve(root.right ,arr )
    
    def buildBalancedTree(self,root):
        #code here
        arr=[]
        self.solve(root , arr)
        start = 0
        end = len(arr)-1
        ans = self.creatBst( start ,end ,arr)
        return ans