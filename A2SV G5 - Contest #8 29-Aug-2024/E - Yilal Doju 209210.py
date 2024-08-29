# Problem: E - Yilal Doju - https://codeforces.com/gym/511242/problem/E

import math
n = int(input())
arr = list(map(int,input().split()))
 
sortedarr = sorted(arr)
 
 
ans = 0
 
ans += math.ceil(sortedarr[0]/2) +  math.ceil(sortedarr[1]/2)
 
for i in range(n-1):
 
    val = math.ceil(max(arr[i],arr[i+1])/2)
    val1 = math.ceil((arr[i] + arr[i+1])/3)
    val = max(  val, val1  )
    ans = min(ans,val)
 
for i in range(n - 2):
    val = math.ceil((arr[i] + arr[i+2])/2)
    ans = min(val, ans)
 
print(ans)