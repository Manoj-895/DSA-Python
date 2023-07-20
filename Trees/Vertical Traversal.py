from queue import Queue
def verticalOrder(self, root): 
        topnode = {}

        q = Queue()

        q.put((root, 0))

        

        while not q.empty():

            node, hzd = q.get()

            try:
                topnode[hzd].append(node.data)
            except:
                topnode[hzd] = [node.data]

            

            if node.left:

                q.put((node.left, hzd - 1))

            if node.right:

                q.put((node.right, hzd + 1))

                

        ans = []

        for i in sorted(topnode.keys()):
            for j in topnode[i]:
                ans.append(j)

        return ans