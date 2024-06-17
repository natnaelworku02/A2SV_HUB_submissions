# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players=set()
        di=Counter()
        ans=[[],[]]
        for match in matches:
            players.update(match)
            di[match[1]]+=1
        for item in players:
            if item not in  di:
                ans[0].append(item)
            elif item in di and di[item]==1:
                ans[1].append(item)
        ans[0].sort()
        ans[1].sort()
        return ans

        

