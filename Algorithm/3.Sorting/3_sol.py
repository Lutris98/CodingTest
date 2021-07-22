# D기업 프로그래밍 컨테스트 예선
n = int(input())
array = [0]*n
for i in range(n):
    data = input().split()
    array[i]=[data[0],int(data[1])]
array = sorted(array, key=lambda x: x[1])  # 원소가 리스트일때 key설정가능  # lambda 원소 변수설정: 결과값
for student in array:
    print(student[0], end=' ')