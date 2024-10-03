# Problem: B - tourist orz! - https://codeforces.com/gym/522079/problem/B

size = int(input())
for _ in range(size):
    n,z = list(map(int,input().split()))
 
    arr = list(map(int,input().split()))
 
    ans=  0
    for i in range(n):
        ans = max(ans,arr[i]|z)
    print(ans)