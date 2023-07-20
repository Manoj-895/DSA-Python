    def flatten(self, root):
        #code here
        current = root
        
        while(current != None):
            if(current.left != None):
                pre = current.left
                while(pre.right != None):
                    pre = pre.right
                pre.right = current.right
                current.right=current.left
                current.left =None
            current = current.right
                
            
        return root