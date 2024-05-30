# Problem: Fedor and New Game - https://codeforces.com/contest/467/problem/B

n,m,k  = list(map(int,input().split()))
arr = []

for _ in range(m+1):
    arr.append(int(input()))
ans = 0
for i in range(m):
    val =(arr[i] ^ arr[-1])
    val = bin(val)
    val = val[2:]
    if val.count('1') <= k:
        ans+=1
# print(bin(~(26 ^ 18)),26 ^ 18, ~(26 ^ 18))
print(ans)