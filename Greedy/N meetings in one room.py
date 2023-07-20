class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        d = []
        for i in range(len(start)):
            d.append((end[i], start[i]))
        d = sorted(d)
        count = 1
        end = d[0][0]
        for i in range(1,len(start)):
            if(d[i][1] > end):
                count += 1
                end = d[i][0]
        return count