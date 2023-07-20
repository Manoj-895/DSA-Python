class Solution:
    def getnextSmallerElement(self,heights):
        stack=[]
        ans = []
        stack.append(-1)
        for i in range(len(heights)-1,-1,-1):
            cur = heights[i]
            while(stack[-1] != -1 and heights[stack[-1]]>=cur):
                stack.pop()
            ans.insert(0,stack[-1])
            stack.append(i)
        return ans

    def getpresmallerElement(self,heights):
        stack=[]
        ans = []
        stack.append(-1)
        for i in range(len(heights)):
            cur = heights[i]
            while(stack[-1] != -1 and heights[stack[-1]]>=cur):
                stack.pop()
            ans.append(stack[-1])
            stack.append(i)
        return ans

    def largestRectangleArea(self, heights) -> int:
        next = self.getnextSmallerElement(heights)
        pre = self.getpresmallerElement(heights)
        maxarea = -1
        
        for i in range(len(heights)):
            h = heights[i]
            
            if(next[i] == -1):
                next[i] = len(heights)
            a=next[i]
            b = pre[i]
            width = a-b-1
            area = h*width
            maxarea = max(area,maxarea)
            
        return maxarea
    def maxArea(self,M, n, m):
        
        area = self.largestRectangleArea(M[0])
        max_area = area
        for i in range(1,n):
            for j in range(m):
                if(M[i][j] != 0):
                    M[i][j] = M[i][j]+M[i-1][j]
                else:
                    M[i][j]= 0
                
                area = self.largestRectangleArea(M[i])
                max_area = max(max_area,area)
        return max_area
                