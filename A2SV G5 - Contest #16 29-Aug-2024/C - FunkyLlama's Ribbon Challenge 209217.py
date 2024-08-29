# Problem: C - FunkyLlama's Ribbon Challenge - https://codeforces.com/gym/523525/problem/C

import sys, threading
def I():
    return sys.stdin.readline().strip()
def main():
    inp = list(map(int,I().split()))
    n = inp[0]
    nums = inp[1:]
    nums.sort()
    memo = {}
    def dp(size):
        if size == 0:
            return 0
        # print(size)
        if size < 0:
            return float("-inf")
            
        if size not in memo:
 
            val = float("-inf")
            for num in nums:
                val = max(val,dp(size - num) + 1)
            # print(val,size)
            memo[size] = val
        # print("______")
        
        return memo[size]
 
    
    print(dp(n))
 
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()