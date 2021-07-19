# T기업 코딩테스트
x = int(input())
array = []
for i in range(x):
    array.append(int(input()))
array.sort()
array.reverse()  # 오름차순이 흔하니 내림차순은 reverse
for x in array:
    print(x,end=' ')