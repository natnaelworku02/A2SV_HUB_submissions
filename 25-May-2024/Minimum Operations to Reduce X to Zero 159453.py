# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        tar=sum(nums)-x
        l=0
        max_win=-1
        s=0
        for r in range(len(nums)):
            s+=nums[r]
            while l<=r and tar <s:
                s-=nums[l]
                l+=1
            if tar==s:
                max_win=max(max_win,r-l+1)
        return max_win if max_win==-1 else len(nums)-max_win
