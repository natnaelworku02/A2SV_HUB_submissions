# Problem: Kids With the Greatest Number of Candies - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[]
        big=max(candies)
        for n in candies:
            if n+extraCandies>=big:
                ans.append(True)
            else:
                ans.append(False)
        return ans