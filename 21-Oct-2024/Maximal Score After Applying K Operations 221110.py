# Problem: Maximal Score After Applying K Operations - https://leetcode.com/problems/maximal-score-after-applying-k-operations

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        for i in range(len(nums)):
            nums[i] = - nums[i]
        
        heapq.heapify(nums)
        ans = 0

        for i in range(k):
            val = - heapq.heappop(nums)
            ans += val
            val = ceil(val/3)
            heapq.heappush(nums,-val)
        
        return ans