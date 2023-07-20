class Solution:
    def positioner(self,inorder,start,end,element):
        i=start
        while(i <= end):
            if(inorder[i]== element):
                return i
            i+=1
        
    
    def treeBuilder(self,inorder,preorder,n,index,start,end,mapped):
        if(index[0] >= n or start > end):
            return None
        
        element = preorder[index[0]]
        index[0]=index[0]+1
        root = Node(element)
        position = self.positioner(inorder,start,end,element)
        # print(element , start , end , position , "HII")
        root.left = self.treeBuilder(inorder , preorder ,n, index , start , position -1 ,mapped)
        root.right = self.treeBuilder(inorder , preorder ,n, index , position+1 , end ,mapped)
        
        return root
    
    def buildtree(self, inorder, preorder, n):
        # code here
        # build tree and return root node
        start = 0
        end = n-1
        index=[0]
        mapped={}
        for i in range(n):
            mapped[inorder[i]]=i
        # print(mapped)
        ans = self.treeBuilder(inorder,preorder,n,index,start,end,mapped)
        return ans