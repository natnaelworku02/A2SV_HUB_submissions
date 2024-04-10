# Problem: Longest Cycle in a Graph - https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        

        color = [0] *(len(edges))
        di = defaultdict(int)
        ans = -1

        for i in range(len(color)):
            if color [i] == 0:
                # print(i)
                ind = i
                visited = set()
                count = 0
                while ind > -1 and color[ind] == 0:
                    color[ind] = 1
                    di[ind] = count
                    count += 1
                    visited.add(ind)
                    ind = edges[ind]
                # print(ind)
                if ind != -1 and ind in visited:
                    # print("hi")
                    ans = max(ans,count - di[ind])

        
        return ans
