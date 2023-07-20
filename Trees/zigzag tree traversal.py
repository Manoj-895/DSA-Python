from collections import deque
class Solution:
    #Function to store the zig zag order traversal of tree in a list.
    def zigZagTraversal(self, root):
        if(root == None):
            return -1
        result = []
        q = deque()
        q.append(root)
        rightLeftFlag = True
        while(len(q)!=0):
            ans = [0]*len(q)
            size = len(q)
            # print(size)
            for i in range(size):
                front = q[0]
                q.popleft()
                
                index = i if rightLeftFlag == True else size-1
                # print(index,front.data)
                ans[index]=front.data
                
                if(front.left):
                    q.append(front.left)
                if(front.right):
                    q.append(front.right)
                size = size-1
            rightLeftFlag = not rightLeftFlag
            for i in ans:
                result.append(i)
        return result