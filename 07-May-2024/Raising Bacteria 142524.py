# Problem: Raising Bacteria - https://codeforces.com/contest/579/problem/A

n = int(input())
ans = 0

while n>1:
    if n % 2:
        ans += 1
    n //=2
print(ans+1)
    