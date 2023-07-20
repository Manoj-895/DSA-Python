class Solution:

    def findMinDiff(self, A,N,M):
        A.sort()
        i=0
        j=M-1
        mini = float('inf')
        while(j<N):
            diff = A[j] - A[i]
            mini = min(mini,diff)
            i+=1
            j+=1
            
        return mini
            