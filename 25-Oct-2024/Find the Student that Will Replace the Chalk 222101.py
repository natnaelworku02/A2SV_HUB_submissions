# Problem: Find the Student that Will Replace the Chalk - https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        val = sum(chalk)
        # print(k,val)
        if val  <= k:
            k %=val
        i = 0
        while k > 0:
            k -= chalk[i]
            # print(i,k)
            if  k < 0:

                return i
            i += 1
        
        return i