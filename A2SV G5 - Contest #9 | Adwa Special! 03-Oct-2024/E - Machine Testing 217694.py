# Problem: E - Machine Testing - https://codeforces.com/gym/513152/problem/E

import math
size= int (input())
 
for _ in range(size):
    n = int(input())
    h = list(map(int,input().split()))
    p = list(map(int,input().split()))
 
    st = [(max(h),p[0])]
    ans = 0
    for i in range(1 , n):
        val = 0
        time = 0
        while st  and ((time < st[-1][0] and (st[-1][0] - time) * st[-1][1] < h[i]) or time >= st[-1][0]):
            if time >= st[-1][0]:
                st.pop()
            else:
                val += st[-1][0] - time
                # print(val,i,"hi")
                h[i] -= st[-1][1] * (st[-1][0]  - time)
                time = val
                st.pop()
        val += math.ceil(h[i]/st[-1][1])
        # print(val, " hi")
        ans = max(ans,val)
        st.append((val,p[i]))
    print(ans)