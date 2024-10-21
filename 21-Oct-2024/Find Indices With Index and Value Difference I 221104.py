# Problem: Find Indices With Index and Value Difference I - https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description/

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        
        
        for l in range(len(nums)):
            r = l + indexDifference

            while r < len(nums):
                if abs(nums[r] -  nums[l]) >= valueDifference:
                    return [l,r]
                r += 1
                

        return [-1,-1]

            