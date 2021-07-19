# DFS, BFS
그래프는 Node와 Edge로 구성되며 인접리스트/인접행렬로 표현가능(리스트쪽은 메모리낭비적으나 속도가 느림)</br>
파이썬의 경우 C와 달리 연결리스트를 위한 라이브러리 import가 필요없이 그냥 list기능으로</br>
graph, start는 고정값, visited리스트도 입력받기도 함</br>

## DFS (DepthFirst)
원론적 구현 : Stack</br>
시작노드 append후</br>
인접노드중 '하나' append반복하다 없어지면 직전노드 pop</br>
실제 구현은 재귀함수로 함</br>

## BFS (BreadthFirst)
원론적 구현 : Queue</br>
시작노드 append</br>
맨밑노드 popleft후 인접노드 '모두' append 반복</br>
실제 구현은 from collections import deque해서 queue=deque([start])</br>