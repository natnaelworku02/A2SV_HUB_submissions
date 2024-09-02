# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        # if not edges:
        #     return (n*(n-1))//2

        adjlist = defaultdict(list)

        parent = {i:i  for i in range(n) }
        size = {i:1 for i in range(n)}


        def find( x):
            while x != parent[x]:
                x = parent[x]
                parent[x] = parent[parent[x]]  
            return parent[x]
        def union( x, y) :
            rootx = find(x)
            rooty = find(y)
            if rootx != rooty:
                if size[rootx] < size[rooty]:
                    parent[rootx] = rooty
                    size[rooty] += size[rootx]
                else:
                    parent[rooty] = rootx
                    size[rootx] += size[rooty]
            
        for edge in edges:
            x,y = edge

            union(x,y)
        
        ans = 0
        arr = [0]
        pre = 0
        count = 0
        for i in range(n):
            if parent[i] == i:
                pre += size[i]
                if count:
                    arr.append( arr[-1] + size[i])
                    ans += size[i]*(n - arr[-1])
                count += 1


        return ans
        






