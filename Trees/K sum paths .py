# Re Doooooooooooooo plzzzzz   TL marrahiheeee

  def solve(self, root, k, vector, count):
        if root is None:
            return

        vector.append(root.data)
        self.solve(root.left, k, vector, count)
        self.solve(root.right, k, vector, count)
        sum = 0
        n = len(vector)
        for i in range(n-1, -1, -1):
            sum = sum + vector[i]
            if (sum == k):
                count[0] = count[0] + 1
        # print(vector,count)
        vector.pop()

    def sumK(self,root,k):
        vector=[]
        count = [0]
        self.solve(root,k,vector,count)
        return count[0]