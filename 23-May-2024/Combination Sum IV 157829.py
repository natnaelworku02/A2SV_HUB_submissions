# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def dp(tar):

            if tar == 0:
                return 1
            
            if tar not in memo:

                val = 0

                for num in nums:
                    if tar - num >=0:
                        val += dp(tar - num)
                
                memo[tar] = val
            
            return memo[tar]
        
        return dp(target)