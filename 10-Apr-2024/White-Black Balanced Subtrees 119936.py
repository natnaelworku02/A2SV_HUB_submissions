# Problem: White-Black Balanced Subtrees - https://codeforces.com/contest/1676/problem/G




import sys
def I():
    return sys.stdin.readline().strip()
# sys.setrecursionlimit(10000)
from collections import defaultdict,deque

def main():
    pass
    def S(): return sys.stdin.readline().strip()
    size= int(S())

    

    for _ in range(size):
        count = []
        n = int(S())
        di = defaultdict(list)
        point = list(map(int,S().split()))
        for i in range(1,n):
            di[point[i-1]].append(i + 1)
        color = [ch for ch in I()]
        # print(color)
        stack = []
        stack.append(1)
        visited = set()
        visited.add(1)
        parent = defaultdict(list)
        ans = [[0,0] for _ in range(n)]
        # print(ans)
        while stack:
            val = stack[-1]
            flag = True
            for ind in di[val]:
                if ind not in visited:
                    flag = False
                    stack.append(ind)
                    visited.add(ind)
                    parent[ind] = val
            # print(parent)

            if flag:
                # print(val)
                # print(stack)
                val = stack.pop()
                if color[val -1 ] =="W":
                    ans[val - 1][0] += 1
                else:
                    ans[val - 1][1] += 1
                par = parent[val]
                # print(par)
                if val != 1: 
                    ans[par - 1][0] += ans[val - 1][0]
                    ans[par - 1][1] += ans[val - 1][1]
            #     print(ans)
            # print("___________")
        
        count = 0
        for white , black in ans:
            if white == black:
                count += 1
        
        print(count)



main()






