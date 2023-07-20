def positioner(In,start,end,element):
        i=start
        while(i <= end):
            if(In[i]== element):
                return i
            i+=1
        
    
def treeBuilder(In,post,n,index,start,end):
    if(index[0] < 0 or start > end):
        return None
        
    element = post[index[0]]
    index[0]=index[0]-1
    root = Node(element)
    position = positioner(In,start,end,element)
    # print(element , start , end , position , "HII")
    root.right = treeBuilder(In , post ,n, index , position+1 , end)
    root.left = treeBuilder(In , post ,n, index , start , position -1)
    
        
    return root

        
def buildTree(In, post, n):
    # your code here
    start = 0
    end = n-1
    index=[n-1]
    ans = treeBuilder(In,post,n,index,start,end)
    return ans