class TrieNode:
    def __init__(self) -> None:
        self.children = [None for i in range(26)]
        self.count = 0
        self.isEnd = False
    
class Trie :
    def __init__(self) :
        self.root = TrieNode()
    
    def getindex(self,ch):
        return ord(ch)-ord('a')

    def insert(self, string) :
        start = self.root
        for i in string:
            index = self.getindex(i)
            if(start.children[index] == None):
                start.children[index] = TrieNode()
                start.count +=1
            start = start.children[index]
        start.isEnd = True
    
    def lprefix(self,word):
        start = self.root
        ans = ""
        for i in word:
            index = self.getindex(i)
            if(start.count == 1):
                ans=ans+i
                start = start.children[index]
            else:
                break
            if(start.isEnd == True):
                break
        return ans

def longestCommonPrefix(arr, n):
    root = Trie()
    for i in arr:
        root.insert(i)
    return root.lprefix(arr[0])


 # space optimized solution 
 def longestCommonPrefix(arr, n):
    ans=""
    for i in range(len(arr[0])):
        ch = arr[0][i]

        match = True

        for j in range(1,n):
            if(len(arr[j]) < i or ch != arr[j][i]):
                match = False
                break

        if(match==False):
            break
        else:
            ans=ans+ch

    return ans