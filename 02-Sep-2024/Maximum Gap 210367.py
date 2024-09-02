# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()

        ans = 0 
        for i in range(1,len(nums)):
            ans = max(nums[i]-nums[i-1],ans)
        return ans