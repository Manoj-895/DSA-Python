def largestBST(root):
    def solve(root):
        nonlocal ans
        if(root == None):
            return [100000 , -100000 , True , 0]
        left = solve(root.left)
        right = solve(root.right)
        # print(left, right ,"Hello",root.data)
        res = [0 , 0, 0 ,0]
        res[3] = left[3] + right[3] +1
        res[1] = max(root.data , right[1])
        res[0] = min(root.data , left[0])

        if((left[2]==True and right[2]==True) and (root.data > left[1] and root.data < right[0])):
            res[2] = True
        else:
            res[2] = False
        # print(res[2],ans)
        if(res[2] == True):
            ans = max(ans,res[3])
        return res

    ans=0
    solve(root)
    return ans