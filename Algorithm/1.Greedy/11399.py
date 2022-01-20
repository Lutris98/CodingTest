n = int(input())  # N 1000수준이니까 O(N2)까진 가능
p = list(map(int,input().split()))
t = [0]*n
p.sort()

for i in range(n):
    t[i] += p[i]
    for j in range(i):  # 이중 반복문 별로 짜고 싶진 않은데ㅠ
        t[i] += p[j] # 일단 i 1로 고정했을때 p의 0하나만
print(sum(t))