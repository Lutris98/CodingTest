# 2018 E기업 알고리즘대회
N, K = map(int,input().split())
result = 0

while True:  #무한반복은 while전문
    if N%K == 0:
        N = N/K
        result += 1
    elif N == 1:
        break
    else: #생각해보니 나누는게 최우선이니 가장 앞으로
        N -= 1
        result += 1
print(result)
