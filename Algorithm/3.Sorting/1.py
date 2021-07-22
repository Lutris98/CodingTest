# Selection sort
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(array)):  # 루프를 두번 돌리므로 시간복잡도가 O(N2)
     min_index = i  # 정말 초기값은 아무거나 해도 상관없다
     for j in range(i+1,len(array)):  # 이전 값이랑 비교하면 안됨
          if array[j] < array[min_index]:
               min_index = j  # min으로 찾는 대신 직접 비교해서
     array[i], array[min_index] = array[min_index], array[i]  # 파이썬에서만 가능한 스왑
print(array)

# Insertion sort
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(1,len(array)):  # range시작지점 좀 잘 활용하기
     for j in range(i,0,-1):  # 거꾸로 count하면 간단하게 구현가능(움직이는 방향의 일관성)  #range주의(끝숫자에서 하나제거)
          if array[j]<array[j-1]:
               array[j-1], array[j] = array[j], array[j-1]  # 전에는 모두 정렬되어있다는 가정이 기본
print(array)

# Quick sort
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
def quick_sort(array):
     if len(array)<=1: return array
     pivot = array[0]
     rest = array[1:]

     left_side = [x for x in rest if x <= pivot]
     right_side = [x for x in rest if x > pivot]

     return quick_sort(left_side)+[pivot]+quick_sort(right_side)  # 재귀적으로 정의
print(quick_sort(array))

# Count Sort
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count = [0]*(max(array)+1)  # 후에 인덱스로 불러오려면 []로 안됨
for i in range(len(array)):
     count[array[i]] += 1  # 비어있는 공간있어도 어쩔수 없지
for i in range(len(count)):
     for j in range(count[i]):
          print(i, end='')