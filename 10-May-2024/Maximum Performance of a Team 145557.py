# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        nums = []
        for i in range(len(speed)):
            nums.append([efficiency[i],speed[i]])
        
        nums.sort(reverse = True)
        heap = []
        ans = 0
        sumed = 0
        for i in range(len(nums)):
            if len(heap) == k:
                sumed -= heappop(heap)
            heappush(heap,nums[i][1])
            sumed += nums[i][1]
            
            ans = max(ans,nums[i][0] * sumed)
        
        return (ans) % (pow(10,9) + 7)
