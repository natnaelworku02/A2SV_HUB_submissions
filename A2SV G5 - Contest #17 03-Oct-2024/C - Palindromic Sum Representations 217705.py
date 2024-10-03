# Problem: C - Palindromic Sum Representations - https://codeforces.com/gym/524965/problem/C

pali = []
for i in range(1,40000+1):
    if str(i) == str(i)[::-1]:
        pali.append(i)
# print(len(pali))
memo = [0] * (40000+1)
memo [0] = 1
 
for i in range(len(pali)):
    for j in range(len(memo)):
        if j+pali[i] < len(memo):
            memo[j+pali[i]] += memo[j]
            memo[j+pali[i]] %= (pow(10,9)+ 7)
 
size = int(input())
for _ in range(size):
    n =int(input())
 
    print(memo[n] )