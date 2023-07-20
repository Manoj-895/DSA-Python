class Solution:
    #Your Function Should return True/False
    def counter(self,root):
        if(root == None):
            return 0
        
        ans =  1 + self.counter(root.left) + self.counter(root.right)
        return ans
    
    def isCBT(self,root,index,count):
        if(root == None):
            return True
        if(index >= count):
            return False
        else:
            left = self.isCBT(root.left , 2*index +1 , count)
            right = self.isCBT(root.right , 2*index +2 ,count)
            return (left and right)
    
    def isMaxheap(self,root):
        if(root == None):
            return True
        if(root.right == None and root.left == None):
            return True
        if(root .right == None):
            return (root.data > root.left.data)
        else:
            left = self.isMaxheap(root.left)
            right = self.isMaxheap(root.right)
            return ((left and right)and ((root.data > root.left.data) and (root.data > root.right.data)))
    
    def isHeap(self, root):
        count = self.counter(root)
        # print(self.isCBT(root , 0 ,count))
        # print(self.isMaxheap(root))
        if(self.isCBT(root , 0 , count) and self.isMaxheap(root)):
            return True
        else:
            return False