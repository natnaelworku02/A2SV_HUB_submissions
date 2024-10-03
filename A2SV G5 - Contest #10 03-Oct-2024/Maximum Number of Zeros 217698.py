# Problem: Maximum Number of Zeros - https://codeforces.com/gym/514644/problem/D

from collections import defaultdict
import math
n = int(input())
nums = list(map(int,input().split()))
nums2 = list(map(int,input().split()))
 
di = defaultdict(int)
count = 0
 
for  i in range(n):
    if nums[i] == 0 and nums2[i] == 0:
        count += 1
        continue
    elif nums[i] == 0:
        continue
    val = math.gcd(nums[i],nums2[i])
    nums[i]//= val
    nums2[i]//= val
    if nums[i] <0 :
        nums2[i]  *= -1
        nums[i] *= -1
    key = str(nums[i]) + "/" + str(nums2[i])
    # print(key)
    di[key] += 1
    # print(di)
# ans = 
 
if di:
    print(max(di.values()) + count)
else:
    print(count)
 
 
 