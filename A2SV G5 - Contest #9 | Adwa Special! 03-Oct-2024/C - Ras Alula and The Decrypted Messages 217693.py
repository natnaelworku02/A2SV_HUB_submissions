# Problem: C - Ras Alula and The Decrypted Messages - https://codeforces.com/gym/513152/problem/C

size = int(input())
for _ in range(size):
    n,m = list(map(int,input().split()))
    s = input()
    data = input()
    
    scount = 0
    dcount = 0
    for i in range(m):
        scount += ord(s[i])
        dcount += ord(data[i])
    
    if scount == dcount:
        print("YES")
    else:
 
        for i in range(m,n):
            scount -= ord(s[i-m])
            scount += ord(s[i])
            if scount == dcount:
                print("YES")
                break
        else:
            print("NO")