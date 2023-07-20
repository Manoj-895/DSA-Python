class Solution:
    def minimumDays(self, S, N, M):
        sunday = S // 7
        buyableDays = S - sunday
        totalFood = S*M
        ans = 0
        if(totalFood % N == 0):
            ans = totalFood//N
        else:
            ans = totalFood//N +1
        if(ans <= buyableDays):
            return ans
        else:
            return -1
        