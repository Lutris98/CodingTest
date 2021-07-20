# 순차탐색
def sequential_search(array,target):  # 순차탐색도 간단하지만 자주 사용됨(최악의 경우 시간복잡도 O(N))
    for i in range(len(array)):
        if array[i]==target:
            return i+1  # 결과는 인덱스가 아니라 사람 생각대로

array = input().split()
target = input()

print(sequential_search(array,target))

# 이진탐색 by 재귀함수
def binary_search(array,target,start,end):
    if start>end: return None
    mid = (start+end)//2  # 몫이 곧 버림연산
    if array[mid]==target: return mid
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)  #재귀로 하면 간단함
    else:
        return binary_search(array,target,mid+1,end)

array = list(map(int, input().split()))
target =int(input())
print(binary_search(array,target,0,len(array)-1)+1)

# 이진탐색 by 반복문
def binary_search(array,target,start,end):
    while start<=end:  # 정상인 쪽을 반복문에 넣음
        mid = (start+end)//2
        if array[mid]==target: return mid
        elif array[mid]>target: end=mid-1
        else: start = mid+1
    return None
array = list(map(int,input().split()))
target = int(input())
print(binary_search(array,target,0,len(array)-1)+1)