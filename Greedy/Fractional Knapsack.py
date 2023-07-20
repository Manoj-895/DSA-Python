class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        our = []
        for i in range(n):
            perUnit = arr[i].value / arr[i].weight
            our.append((perUnit , arr[i].value ,arr[i].weight))
        
        our = sorted(our , reverse=True)
        
        max_val = 0
        for i in range(n):
            if(our[i][2] > W):
                max_val += our[i][0] * W
                W=0
            else:
                max_val += our[i][1]
                W -= our[i][2]
        return max_val