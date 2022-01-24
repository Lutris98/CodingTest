n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
s = 0

a.sort()

for i in range(n):
    rank = 0 #작은 순서
    for j in range(n):
        if b[i] > b[j]: rank+=1
    s += b[i]*a[n-rank-1]
print(s)