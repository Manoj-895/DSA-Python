def lca(self,root, n1, n2):
        if(root == None):
            return None
        if(root.data == n1 or root.data == n2):
            return root
        
        left = self.lca(root.left,n1,n2)
        right = self.lca(root.right,n1,n2)
        
        if(left != None and right != None):
            return root
        elif(left != None and right == None):
            return left
        elif(left == None and right != None):
            return right
        else:
            return None