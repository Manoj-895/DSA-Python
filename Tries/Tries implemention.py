class TrieNode:
    def __init__(self) -> None:
        self.children = [None for i in range(26)]
        self.isEnd = False
    
class Tries:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def getindex(self,ch):
        return ord(ch)-ord('a')

    def insert(self,data):
        start = self.root

        for i in data:
            index = self.getindex(i)
            if(start.children[index] == None):
                start.children[index] = TrieNode()
            start = start.children[index]
        start.isEnd = True
    
    def search(self,data):

        start = self.root
        for i in data:
            index = self.getindex(i)
            if(start.children[index] != None):
                start = start.children[index]
            else:
                return False
        return start.isEnd
        
t=Tries()
t.insert("manoj")
print(t.search("manoj"))


    

