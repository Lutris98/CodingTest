# 파이썬으로 구현하는 자료구조

## 1. 배열 : list로 대체
장점은 순차탐색에 좋음(연속된 메모리 공간 할당)</br>
단점은 삽입,삭제시 비효율적</br>

list랑 다른 점</br>
모든 원소가 같은 자료형</br>
크기 확장 불가</br>

array = []</br>
array.append('a')  #맨끝에 추가 </br>
array.remove('b')  #원소 찾아 삭제</br>

## 1. 스택 : 그냥 list에서 push와 pop만 사용하면 됨
장점은 삽입삭제가 맨 윗부분에서만 일어남</br>
단점은 탐색하기 어려움</br>

stack = []</br>
stack.append('a')  #push대신</br>
stack.pop()</br>

## 2. 선형큐 : from collections import deque (리스트사용구현하면 삭제가 O(N))
문제점은 배열의 마지막 index값이 계속 변함(대안이 원형큐지만 직접구현해야함)</br>
queue = deque([])</br>
queue.append('a')</br>
queue.popleft()</br>


## 3. 우선순위큐 : import heapq
장점 : 우선순위높은 것부터 처리</br>
최소힙 기반(힙 자료구조는 리스트로 이진트리 직접 구현해야함)</br>
인덱스고정된 건 최솟값인 heap[0] 밖에 없음(다음을 보려면 heappop)</br>

heap = [] #heapq모듈은 리스트를 우선순위큐처럼 사용하도록 허용해줌</br>
heapq.heapify(heap)  #기존 리스트</br>
heapq.heappush(heap, 4)  # 순서대로 큐채워짐(1,3,4,7순대로)</br>
heapq.heappop(heapq.heappop(heap)) # 작은 값부터 삭제</br>

