# Problem: D - The Kittens Test - https://codeforces.com/gym/520688/problem/D

from collections import defaultdict,deque
n = int(input())
di = defaultdict(list)
# qu = []
parent = {i:i for i in range(1,n+1)}
size = {i:0 for i in range(1,n+1)}
# print(parent)
def  find(x):
    while x != parent[x]:
        x = parent[x]
        parent[x] = parent[parent[x]]
    return x
 
def union(x,y):
    parx = find(x)
    pary = find(y)
    parent[pary] = parx
    di[parx].append(pary)
    
    
 
for i in range(n- 1):
    u,v = list(map(int,input().split()))
    union(u,v)
 
stack = []
# visited = set()
# print(parent)
for keys in di.keys():
    di[keys] = di[keys][::-1]
for key , val in parent.items():
    if key == val:
        stack.append(val)
        break
 
ans = []
while stack:
    
    node = stack.pop()
    ans.append(node)
    for ind in di[node]:
        stack.append(ind)
print(*ans)