# Problem: Find the Difference - https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=list(s)
        for char in t:
            if char not in s:
                return char
            else:
                s.pop(s.index(char))
        return ""