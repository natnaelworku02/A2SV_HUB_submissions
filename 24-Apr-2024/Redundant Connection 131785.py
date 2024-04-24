# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {i+1:i+1 for i in range(len(edges))}
        ans = []
        adjlist = defaultdict(list)

        

        def find(node):
            return parent[node]
        
        def union (x,y):
            parx = find(x)
            pary = find(y)

            if parx == pary:
                return 0
            
            # parent[y] = parx
            for key,val in parent.items():
                if val == pary:
                    parent[key] = parx
            return 1
            
        
        # return []
        for edge in edges:
            u , v = edge

            if not union(u,v):
                return edge
        
        return []

                            

