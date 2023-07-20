from queue import Queue
class Solution:
    
    #Function to return a list of nodes visible from the top view 
  
    def topView(self,root):
        topnode = {}
        q = Queue()
        q.put((root, 0))

        while not q.empty():
            node, hzd = q.get()
            if hzd not in topnode.keys():
                topnode[hzd] = node.data

            if node.left:
                q.put((node.left, hzd - 1))

            if node.right:
                q.put((node.right, hzd + 1))

        ans = []
        for i in sorted(topnode.keys()):
            ans.append(topnode[i])
            
        return ans