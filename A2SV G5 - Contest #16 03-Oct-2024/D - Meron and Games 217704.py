# Problem: D - Meron and Games - https://codeforces.com/gym/523525/problem/D

import sys, threading
def I():
    return sys.stdin.readline().strip()
def main():
    from collections import defaultdict
    n = int(input())
    arr = list(map(int,input().split()))
 
    di = defaultdict(int)
    for i in range(len(arr)):
        di[arr[i] ] += arr[i]
    # print(di)
    memo = {}
    def dp(num):
        if num >= pow(10,5) + 1:
            return 0
        if num not in memo:
            val = dp(num+2) + di[num]
            val = max(val,dp(num+1))
            memo[num] = val
        
        return memo[num]
    # print()
    print(dp(1))
 
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()