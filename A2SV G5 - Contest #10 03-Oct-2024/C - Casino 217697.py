# Problem: C - Casino - https://codeforces.com/gym/514644/problem/C

import math
from collections  import defaultdict
n = int(input())
nums = list(map(int,input().split()))
 
for i in range(len(nums)):
    while nums[i] % 2 == 0 or nums[i] % 3 == 0:
        if nums[i] % 2==0:
            nums[i] //= 2
        else:
            nums[i] //= 3
val = nums[0]
 
for i in range(1,len(nums)):
    if nums[i] != val:
        print("No")
        break
else:
    print("Yes")