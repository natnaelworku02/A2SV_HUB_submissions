# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ans = [[-1] * len(mat[0]) for _ in range(len(mat))]
        queue = deque()
        visited = set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append([i,j,0])
                    visited.add((i,j))
                    # ans[i][j] = 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        def inbound(r,c):
            return 0<= r< len(mat) and 0<= c < len(mat[0])
        while queue:
            for i in range(len(queue)):
                row,col,val = queue.popleft()
                ans[row][col] = val
                for r,c in directions:
                    r += row
                    c += col
                    if inbound(r,c) and (r,c) not in visited:
                        queue.append([r,c,val + 1])
                        visited.add((r,c))

        return ans  




        
