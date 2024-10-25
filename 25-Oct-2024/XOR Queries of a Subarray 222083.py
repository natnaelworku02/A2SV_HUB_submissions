# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        pre = 0
        nums = [0]

        for num in arr:
            pre ^= num

            nums.append(pre)

        ans =[]

        for l,r in queries:

            ans.append(nums[l]  ^ nums[r+1])

        return ans