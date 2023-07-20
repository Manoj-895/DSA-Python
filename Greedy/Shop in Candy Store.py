class Solution:

    def candyStore(self, candies,N,K):
        min_amount = 0
        i = 0
        n = N-1
        candies = sorted(candies)
        while(i<= n):
            min_amount = min_amount + candies[i]
            i =i+1
            n = n - K
            
        max_amount = 0
        i = N-1
        n = 0
        while(n <= i):
            max_amount = max_amount + candies[i]
            i =i- 1
            n = n + K
            
        return (min_amount , max_amount)