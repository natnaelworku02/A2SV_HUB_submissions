# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        count=0
        ans=0
        for n in nums:
            if n==1:
                count+=1
                
            else:
                ans=max(ans,count)
                count=0
        ans=max(count,ans)
        return ans


        