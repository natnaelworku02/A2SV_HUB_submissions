# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

m,s = list(map(int, input().split()))

if 9 * m < s:
    print(-1,-1)
elif s == 0 :
    if m > 1:
        print(-1,-1)
    else:
        print(0,0)
else:
    _max = [0 for _ in range(m)]
    num = s
    # data = [9,8,7,6,5,4,3,2,1]
    for i in range(m):
        _max[i] = min(9,s)
        s -= min(9,s)
        if not s:
            break
    # print(_max)
    _min = [0 for _ in range(m)]
    _min[0] =  1 if len(_min) >= 1 else 0
    
    num -= _min[0]
    # print(num)
    for i in range(m-1 ,- 1, -1):
        _min[i] += min(9,num)
        num -= min(9,num)
        # print(num)
        if not num:break
    # print(_min)
    print(''.join(map(str,_min)), ''.join(map(str,_max)))
