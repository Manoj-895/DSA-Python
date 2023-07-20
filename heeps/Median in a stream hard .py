import heapq

def signum(a,b):
    if(a==b):
        return 0
    elif(a>b):
        return 1
    else:
        return -1


def solve(minheap , maxheap , element ,median):
    if(signum(len(maxheap),len(minheap)) == 0):
        if(element > median[0]):
            heapq.heappush(minheap,element)
            median[0] =minheap[0]
        else:
            heapq.heappush(maxheap,-1*element)
            median[0] =-1*(maxheap[0])
    elif(signum(len(maxheap),len(minheap)) == 1):
        if(element > median[0]):
            heapq.heappush(minheap,element)
            median[0] = int((minheap[0]+(-1*maxheap[0])) / 2)
        else:
            heapq.heappush(minheap , -1*maxheap[0])
            heapq.heappop(maxheap)
            heapq.heappush(maxheap , -1 *element)
            median[0] = int((minheap[0]+(-1*maxheap[0])) / 2)
    else:
        if(element > median[0]):
            heapq.heappush(maxheap ,-1*minheap[0])
            heapq.heappop(minheap)
            heapq.heappush(minheap,element)
            median[0] = int((minheap[0]+(-1*maxheap[0])) / 2)
        else:
            heapq.heappush(maxheap ,-1*element)
            median[0] = int((minheap[0]+(-1*maxheap[0])) / 2)


def findMedian(arr, n):
    median = [-1]
    minheap=[]
    maxheap=[]
    heapq.heapify(minheap)
    heapq.heapify(maxheap)
    ans = []
    for i in arr:
        # print(i,"k")
        solve(minheap , maxheap ,i ,median)
        # print(maxheap,"jii",minheap,"p",median[0])
        ans.append(median[0])

    return ans
    
