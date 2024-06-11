# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        ind = 0

        while ind < n:
            if nums[ind] > 0 and nums[ind] < n +1:

                temp = nums[ind] - 1
                if temp != ind and nums[temp] != nums[ind]:
                    
                    nums[ind],nums[temp] = nums[temp], nums[ind]
                else:
                    ind +=1
            else:
                ind +=1
        
        for i in range(n):
            if nums[i] != i + 1:
                return i +1
        
        return n +1



                    
