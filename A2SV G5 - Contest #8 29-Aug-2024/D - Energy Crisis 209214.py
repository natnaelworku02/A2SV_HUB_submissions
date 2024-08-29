# Problem: D - Energy Crisis - https://codeforces.com/gym/511242/problem/D

n,l = list(map(int,input().split()))
arr =  list(map(int,input().split()))
 
def check  (val):
    move = 0
 
    for i in range(len(arr)):
        div = abs(arr[i] - val)
        if arr[i] >= val:
            move += (div)
        else:
            move -= (div * 100) / (100 - l)
            # print(div  *(div * (100 - l)/100),val)
    # print(move)
    return True if move  >= 0 else False
 
 
_min = min(arr)
_max = max(arr)
 
dif =  1/1000000
ans = 0
while abs(_max - _min) > dif:
 
    mid = (_min + _max)/2
    if check(mid) :
        _min = mid 
        # ans = mid
    else:
        _max =  mid
print(_max)   