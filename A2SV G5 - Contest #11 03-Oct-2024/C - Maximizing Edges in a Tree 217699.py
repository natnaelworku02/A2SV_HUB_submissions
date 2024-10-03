# Problem: C - Maximizing Edges in a Tree - https://codeforces.com/gym/515998/problem/C

import sys
from collections import defaultdict,deque
def I():
    return sys.stdin.readline().strip()
def main():
    n = int(I())
    di = defaultdict(list)
 
    for i in range(n-1):
        val = list(map(int,I().split()))
        di[val[0]].append(val[1])
        di[val[1]].append(val[0])
    ans = 0
 
    stack = []
    visited = set()
    color = [-1] * n
    stack.append(1)
    color [0] = 0
 
    while stack:
        node = stack.pop()
        visited.add(node)
        for ind in di[node]:
            if color[node - 1]  == 0:
                color[ind - 1] = 1
            else :
                color[ind - 1] = 0
            if ind not in visited:
                stack.append(ind)
                visited.add(ind)
              
    
    # print(color)
    zero = color.count(0)
    one = color.count(1)
    ans = ((zero*one) - (n - 1))
    print(ans)
        
main ()