# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

size= int(input())
for _ in range(size):
    n = int(input())
    n =  list(map(int,bin(n)[2:]))
    val = n[::-1]

    for i in range(len(val)):
        if val[i] == 1:
            val = val[:i+1]
            val = val[::-1]
            break
    count = 0
    val = ''.join(map(str,val))
    n = ''.join(map(str,n))
    val = int(val,2)
    n = int(n,2)

    
    if not val ^ n:
        if val >1:
            val += 1
            # print(int(''.join(map(str,val))))
        elif val == 1:
            val = 3
    
    print(val)
        



