class Stacke:
    def __init__(self,size) -> None:
        self.top = -1
        self.arr = [0]*size
        self.size = size

    def push(self,data):
        print(self.top)
        if(self.top < self.size -1 ):
            self.top +=1
            self.arr[self.top] = data
        else:
            print("Stack overflow at",data)
    
    def pop(self):
        if(self.top >= 0):
            data = self.arr[self.top]
            self.arr[self.top] =0
            self.top -=1
            return data
        else:
            return "Stack empty"
    def peak(self):
        if(self.top >= 0):
            return self.arr[self.top]
        else:
            return "Stack empty"

if __name__ == '__main__':
    sta = Stacke(4)
    sta.push(5)
    sta.push(4)
    sta.push(1)
    sta.push(0)
    sta.push(44)
    print(sta.peak())
    sta.pop()
    print(sta.peak())
    sta.push(23)
    print(sta.peak())
    