# Problem: Heap Operations - https://codeforces.com/contest/681/problem/C

from heapq import heapify,heappop,heappush,heappushpop,heapreplace
n = int(input())
data = []
for i in range(n):
    data.append(list(input().split()))
    if len(data[-1]) == 2:
        data[-1][1] = int(data[-1][1])
# print(len(data[0]))
ans = []
ind = 0
heap = []

while ind  < n:
    # print(len(data[ind]),data[ind][0],"hi")
    if len(data[ind])  == 2 and data[ind][0] == "insert":
        ans.append(data[ind])
        heappush(heap,data[ind][1])
    elif len(data[ind]) == 1:
        # print("NO")
        if not heap:
            ans.append(["insert",0])
            # heappush(heap,-10**9)
        ans.append(["removeMin"])
        # print(heap)/
        if heap:
            # print("HI")
            heappop(heap)
    elif len(data[ind]) == 2 and data[ind][0] == "getMin":
        while heap and data[ind][1] > heap[0]:
            # print("hi")
            val = heappop(heap)
            ans.append(["removeMin"])
        # flag = False
        if heap and heap[0] != data[ind][1]:
            ans.append(["insert",data[ind][1]])
            heappush(heap,data[ind][1])
        elif not heap:
            ans.append(["insert",data[ind][1]])
            heappush(heap,data[ind][1])
        
        ans.append(data[ind])
    
    ind += 1
print(len(ans))
# print(ans)
for val in ans:
    # print(val)
    # continue
    # print(val)
    if len(val) == 2:

        s,v = val
        print(s, str(v))
    else:
        print(val[0])


