# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:

        nums.sort()
        if len(nums) <= 4:
            return 0
        
        min_ = float("inf")

        for i in range(4):
            r = len(nums) - 4 + i
            min_ = min(min_,nums[r] - nums[i])
        
        return min_




