# Problem: B - Grid Path - https://codeforces.com/gym/524965/problem/B

size = int(input())
for _ in range(size):
    n,m,k = list(map(int,input().split()))
    if n*m - 1 == k:
        print("YES")
    else:
        print("NO")
 