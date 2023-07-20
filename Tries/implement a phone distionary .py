class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def getindex(self,ch):
        return ord(ch) - ord('a')
    
    def insert(self,string):
        start = self.root
        for i in string:
            index = self.getindex(i)
            if(start.children[index] == None):
                start.children[index] = TrieNode()
            start = start.children[index]

        start.isEnd = True

    def printSugesstions(self , curr , temp , prefix):
        # print("prefix",prefix)
        if(curr.isEnd == True):
            temp.append(prefix)
        
        for i in range(ord('a') , ord('z')+1):
            next = curr.children[i-ord('a')]
            if(next != None):
                prefix = prefix + chr(i)
                self.printSugesstions(next , temp , prefix)
                prefix = prefix[:-1]
                

    def solve(self , qList):
        pre = self.root
        prefix = ''
        ans = []
        qList = qList.strip()
        for i in qList:
            prefix = prefix + i
            index = self.getindex(i)
            curr = pre.children[index]

            if(curr == None):
                break
            
            temp = []
            self.printSugesstions(curr , temp , prefix)
            ans.append(temp)
            pre = curr
        return ans


def phoneDirectory(arr,qList):
    t = Trie()
    for i in arr:
        t.insert(i)
    return t.solve(qList)
    
        
