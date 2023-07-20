from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)
class TrieNode:
    def __init__(self) -> None:
        self.children = [None for i in range(26)]
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
            start = start.children[index]
        start.isEnd = True
    
    def search(self, word) :
        start = self.root
        for i in word:
            index = self.getindex(i)
            if(start.children[index] != None):
                start = start.children[index]
            else:
                return False
        return start.isEnd

        
    def startWith(self, prefix) :
        start = self.root
        for i in prefix:
            index = self.getindex(i)
            if(start.children[index] != None):
                start = start.children[index]
            else:
                return False
        return True



# main
t = int(input().strip())
root = Trie()
for i in range(t) :

    q_str = stdin.readline().strip().split(" ")
    q = int(q_str[0].strip())
    str1 = q_str[1].strip()

    if(q == 1) :
        root.insert(str1)
    
    elif (q == 2) :
        if(root.search(str1)) :
            print("true") 

        else :
            print("false")
        
    else :
        if(root.startWith(str1)) :
            print("true")

        else :
            print("false")

