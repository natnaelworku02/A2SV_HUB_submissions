# Problem: D - The Flip Tree - https://codeforces.com/gym/515998/problem/D

import sys, threading
def I():
    return sys.stdin.readline().strip()
from collections import defaultdict
n = int(I())
 
di = defaultdict(list)
 
for i in range(n - 1):
    val = list(map(int,I().split()))
    di[val[0]].append(val[1])
    di[val[1]].append(val[0])
 
now = list(map(int,I().split()))
comp = list(map(int,I().split()))
# print(di)
# print("________")
 
stack = []
visited = set()
stack.append([1,0,0,0])
visited.add(1)
ans_count = 0
ans_ind = []
 
while stack:
    node,level,even,odd = stack.pop()
    change = 0
    
    if level % 2:
        change = odd
    else:
        change = even
    
    if change and change % 2:
        now[node - 1] = 1 - now[node - 1]
    
    if now[node - 1] != comp[node - 1] and level % 2:
        ans_count += 1
        ans_ind.append(node)
        odd += 1
    elif now[node - 1] != comp[node - 1] and level % 2 == 0:
        ans_count += 1
        ans_ind.append(node)
        even += 1
    
    for ind in di[node]:
        if ind not  in visited:
            stack.append([ind,level + 1,even,odd])
            visited.add(ind)
# print(stack)
 
print(ans_count)
ans_ind = ans_ind[::-1]
for num in ans_ind:
    print(num)
    