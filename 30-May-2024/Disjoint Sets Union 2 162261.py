# Problem: Disjoint Sets Union 2 - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B

n,m = list(map(int,(input().split())))
parent = {i:i for i in range(1,n+1)}
size = {i:1 for i in range(1,n+1)}
_min = {i:i for i in range(1,n+1)}
_max ={i:i for i in range(1,n+1)}

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
            _min[parx ] = min(x,y,_min[pary],_min[parx])
            _max[parx ] = max(x,y,_max[pary],_max[parx])
            # print(x,y,parx,"hi")
            # print()

        else:     
            parent[parx] = pary
            size[pary] += size[parx]
            _min[pary ] = min(x,y,_min[pary],_min[parx])
            _max[pary ] = max(x,y,_max[pary],_max[parx])


    

for _ in range(m):
    qu = list((input().split()))
    if qu[0] == "union":
        union(int(qu[1]),int(qu[2]))
    else:
        # print(parent)
        print(_min[find(int(qu[1])) ], _max[find(int(qu[1])) ],size[find(int(qu[1]))])