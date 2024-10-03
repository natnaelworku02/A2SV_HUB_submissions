# Problem: C - Balanced Parentheses Clusters - https://codeforces.com/gym/520688/problem/C

from collections import defaultdict
size = int(input())
for _ in range(size):
    n = int(input())
    s= input()
    parent = {i:i for i in range(1,2*n+1)}
    size = {i:0 for i in range(1,2*n+1)}
    # print(parent)
    def  find(x):
        while x != parent[x]:
            x = parent[x]
            parent[x] = parent[parent[x]]
        return x
    
    def union(x,y):
        parx = find(x)
        pary = find(y)
        # print(parx)
        # print(pary)
        # print(x)
        # print("_____________")
        if parx != pary:
            if size[parx] > size[pary]:
                parent[pary] = parx
                size[parx] += size[pary]
            else:     
                parent[parx] = pary
                size[pary] += size[parx]
 
    stack = []
    zero = defaultdict(set)
    zero[0].add(1)
    pre = 0
    prev = 1
    prev_pre = 0
    for i in range(2*n):
        if s[i] == "(":
            stack.append(i+1)
            pre += 1
        elif s[i] == ")" and stack:
            ind = stack.pop()
 
            pre -= 1
            # print(pre,"hihihi")
            # if pre == 0:
            #     zero.add(ind)
            #     for node in zero:
            #         union(node,i+1)
            #     # zero.remove(ind)
            # elif pre == prev_pre :
            #     union(ind,i+1) 
            #     union(prev,i+1)
            # else:
            #     union(ind,i+1)
            zero[pre].add(ind)
            if prev_pre >= pre:
                # print(i,s[i])
                # print(zero[pre])
                # print(zero[pre],pre)
                # print("________")
                for node in zero[pre]:
                    union(node,i+1)
                zero[pre].clear()
                zero[pre].add(ind)
                if prev_pre > pre:
                    zero[prev_pre].clear()
            else:
                union(ind,i+1)
        
            prev = i+1
            prev_pre = pre
    ans = 0
    # print(parent)
    for key , value in parent.items():
        if key == value:
            ans += 1
    
    print(ans)