class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        temp = ''
        ans = ''
        for i in S:
            if(i != '.'):
                temp = temp+i
            else:
                ans = temp+'.'+ans
                temp = ''
        ans = temp+'.'+ans
        return ans[:-1]