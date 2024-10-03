# Problem: D - Final Strength - https://codeforces.com/gym/513152/problem/D

from collections import defaultdict
import bisect
size=  int(input())
 
def mergesort(l,r):
    if l == r:
        return [[arr[l],l]]
 
    m = (l+r)//2
 
    lh = mergesort(l,m)
    rh = mergesort(m + 1, r)
 
    return merge(lh,rh)
 
def merge(lh, rh):
 
    # d = [0] * len(lh)
 
    for i in range(len(lh)):
        ans[lh[i][1]] += bisect.bisect_left(rh,[lh[i][0],-1])
    
    for i in range(len(rh)):
        ans[rh[i][1]] += bisect.bisect_left(lh,[rh[i][0],-1])
        
    for i in range(len(lh)):
        lh[i][0] = ans[lh[i][1]]
    
    for i in range(len(rh)):
        rh[i][0] = ans[rh[i][1]]
    
    
 
    i = 0
    j = 0
    # eq = 0
    # print(lh)
    # print(rh)
    res = []
    while i < len(lh) and j < len(rh):
        if lh[i][0] > rh[j][0]:
            res.append(rh[j])
            j +=1
        else:
            res.append(lh[i])
            i +=1
    res.extend(lh[i:])
    res.extend(rh[j:])
 
    
    
    # print(res)
    return res
 
 
      
 
for _ in range(size):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = [val for val in arr]
    played = defaultdict(int)
 
    nums = mergesort(0,(2**n) - 1)
    # print(nums)
    print(*ans)
 
 