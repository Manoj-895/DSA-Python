
class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        jobs = sorted(Jobs , key = lambda x: x.profit ,reverse=True)
        max_deadline = 0
        for i in jobs:
            max_deadline = max(max_deadline,int(i.deadline))
        
        # print(max_deadline)
        dead = [-1 for i in range(max_deadline+1)]
        count = 0
        max_profit = 0
        for i in jobs:
            profit = i.profit
            deadline = i.deadline
            jobId = i.id
            
            for k in range(deadline,0,-1):
                if(dead[k] == -1):
                    dead[k] = jobId
                    count += 1
                    max_profit += profit
                    break
                
        return (count ,max_profit)
                    