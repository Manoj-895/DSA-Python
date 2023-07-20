def findmin(root):
    temp = root.right
    while(temp.left!= None):
        temp = temp.left
    return temp
    
def deleteNode(root, X):
    if(root == None):
        return root
    # print(root.data)
    if(root.data == X):
        if(root.left == None and root.right == None):
            del root
            return None
        elif(root.left == None and root.right != None):
            temp = root.right
            del root
            return temp
        elif(root.left != None and root.right == None):
            temp = root.left
            del root
            return temp
        else:
            min = findmin(root).data
            root.data = min
            root.right = deleteNode(root.right , min)
            return root
    elif(root.data > X):
        root.left = deleteNode(root.left , X)
        return root
    
    else:
        root.right = deleteNode(root.right , X)
        return root
            