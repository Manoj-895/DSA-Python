
def LCAinaBST(root, P, Q):
    if(root == None):
        return None

    if(root.data > P.data and root.data > Q.data):
        return LCAinaBST(root.left,P,Q)
    if(root.data < P.data and root.data < Q.data):
        return LCAinaBST(root.right, P ,Q)
    return root