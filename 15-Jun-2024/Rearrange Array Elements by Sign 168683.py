# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        postive=[]
        negative=[]
        for num in nums:
            if num >0:
                postive.append(num)
            else:
                negative.append(num)
        answer=[]
        length=len(nums)//2
        for i in range(length):
            answer.append(postive[i])
            answer.append(negative[i])
        return answer
        