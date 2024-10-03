# Problem: D -  Longest Good Sequence - https://codeforces.com/gym/524965/problem/D

from collections import defaultdict
import math
import sys
 
def lstIn(dataType = int , itType = list):
    return itType(map(dataType , input().split()))
 
def solve():
    n = int(sys.stdin.readline().strip())
    nums = lstIn()
 
    memo = defaultdict(int)
 
    def factorize(num):
        lst = set()
        ind = 2
 
        while ind*ind <= num:
            while num % ind == 0:
                lst.add(ind)
                num //= ind
            ind += 1
        if num > 1 and num != nums[i]:
            lst.add(num)
        
        return list(lst)
 
    for i in range(n):
        lst = factorize(nums[i])
        # print(nums[i] , lst)
        ans = 0
        # memo[nums[i]] = 1
        # print(lst)
        for j in range(len(lst)):
            ans = max(ans , memo[lst[j]])
            # print(ans,nums[i])
            # memo[lst[j]] += memo[nums[i]]
        
        memo[nums[i]] = (ans+1)
        # print(nums[i] ,ans)
        for k in range(len(lst)):
            memo[lst[k]]  = memo[nums[i]]
        
        # print(nums[i],ans)
        
        # print(memo[nums[i]])
        # print("___________")
    
    print(max(memo.values()))
 
 
 
 
 
testcase = 0
T = int(input()) if testcase else 1
for _ in range(T):
    solve()