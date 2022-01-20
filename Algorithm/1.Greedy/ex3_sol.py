n,m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int,input().split()))
    min_value = min(data)
    result = max(result, min_value)  # 굳이 다 저장하지 않고 변수 하나만 지정해서 매번 갱신하는 방식

print(result)