def tour(self,lis, n):
        #Code here
        start = 0
        balance = 0 
        deficient = 0
        for i in range(n):
            balance = balance + ( lis[i][0] - lis[i][1] )
            # print(lis[i][0],lis[i][1] , balance,deficient,i,start)
            if(balance < 0):
                deficient =deficient + balance
                start = i+1
                balance = 0
        # print(balance,deficient)
        if(balance + (deficient) >= 0):
            return start
        else:
            return -1