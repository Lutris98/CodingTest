def binary_search(array,target,start,end):
    while start<=end:  #못찾으면 멈춰야하니깐
        mid = (start+end)//2
        if array[mid]==target: return mid
        elif array[mid]>target: end = mid-1
        else: start = mid+1
    return None

n = int(input())
array = list(map(int,input().split()))
array.sort()
m = int(input())
target = list(map(int,input().split()))

for i in target:
    result = binary_search(array,i,0,n-1)
    if result!=None: print('yes',end=' ')
    else: print('no',end=' ')

# 계수정렬
n = int(input())
array = [0]*1000001  # 제시된 조건이 백만까지
for i in map(int,input().split()): array[i]=1  # 값없어도 0으로 남아있는 리스트
m = int(input())
target = list(map(int, input().split()))
for i in target:  # array가 빈 배열로 모든 수를 커버하기때문
    if array[i]==1: print('yes',end=' ')
    else: print('no',end=' ')