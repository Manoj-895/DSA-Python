#User function Template for python3
from collections import deque
class Solution:
    def mapper(self,root , target):
        mapp={}
        burningRoot=None
        q=deque()
        q.append(root)
        
        while(len(q)!=0):
            front = q[0]
            q.popleft()
            # print(front,front.data)
            if(front.data == target):
                burningRoot = front
                
            if(front.left != None):
                mapp[front.left] =front
                q.append(front.left)
                
            if(front.right):
                mapp[front.right]=front
                q.append(front.right)
                
        return burningRoot , mapp
            
            
    def treeBurner(self,root,mapp):
        ans = 0
        q=deque()
        q.append(root)
        visited=[]
        visited.append(root)
        
        while(len(q)!=0):
            flag = 0
            n=len(q)
            for i in range(n):
                front = q[0]
                q.popleft()
                # print(mapp[front])
                if(front.left != None and (front.left not in visited)):
                    flag = 1
                    q.append(front.left)
                    visited.append(front.left)
                if(front.right != None and (front.right not in visited)):
                    flag = 1
                    q.append(front.right)
                    visited.append(front.right)
                if(front in mapp.keys() and mapp[front] not in visited):
                    flag =1
                    q.append(mapp[front])
                    visited.append(mapp[front])
            
            if(flag == 1):
                ans += 1
        return ans
            
    def minTime(self, root,target):
        # code here
        root , mapp = self.mapper(root,target)
        ans = self.treeBurner(root,mapp)
        return ans