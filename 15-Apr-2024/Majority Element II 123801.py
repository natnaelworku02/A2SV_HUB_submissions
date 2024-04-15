# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dictonary=Counter(nums)
        answer=[]
        length=len(nums)//3
        for key,value in dictonary.items():
            if value> length:
                answer.append(key)
        return answer
        