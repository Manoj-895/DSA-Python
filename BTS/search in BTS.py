def searchInBST(root, x):
	
	temp = root
	while( temp!= None):
		if(temp.data == x):
			return True

		if(temp.data > x):
			temp = temp.left
		else:
			temp = temp.right

	return False


# recurssion 
def searchInBST(root, x):
	if(root == None):
		return False

	if(root.data == x):
		return True

	if( root.data > x):
		return searchInBST(root.left, x)
	else:
		return searchInBST(root.right, x)