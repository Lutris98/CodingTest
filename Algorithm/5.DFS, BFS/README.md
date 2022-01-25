# 그래프
그래프는 Node와 Edge로 구성되며 인접리스트/행렬로 표현가능(행렬은 속도를 위해 모든 관계저장하는 것)</br>
파이썬의 경우 C와 달리 연결리스트를 위한 라이브러리 import가 필요없이 그냥 list기능으로</br>
탐색함수 짤때 입력값 3가지 graph, start(시작노드), visited(방문리스트)</br>
간단하게 짜려면 연결관계만 고려해서 짜도 됨</br>

인접리스트 예시
graph = [[] for _ in range(3)] #행 3개인 3차원 배열</br>
graph[0].append((1,7))  # 노드별 연결노드와 해당거리</br>
graph[0].append((2,5))</br>
graph[1].append((0,7))</br>
graph[2].append((0,5))</br>

인접행렬은 간단하게</br>
[[0,7,5],[7,0,inf],[5,inf,0]]</br>

## DFS (DepthFirst)
왜 : 아래 노드가 우선</br>
원론적 구현 : Stack</br>
시작노드 append후</br>
인접노드중 '하나' append반복하다 없어지면 직전노드 pop</br>
실제 구현은 재귀함수로 함-보통 하향식 분석, 상향식 분석도 있음</br>


def dfs(graph,v,visited): # graph를 거리없이 작은 노드 기준으로 연결</br>
    visited[v] = True</br>
    for i in graph[v]:</br>
        if not visited[i] :</br>
            dfs(graph,i,visited)  # 계속 자식노드중 작은쪽 찾아들어가는 게 반복적임</br>

## BFS (BreadthFirst)
왜 : 층단위가 우선</br>
원론적 구현 : Queue</br>
시작노드 append</br>
맨밑노드 popleft후 인접노드 '모두' append 반복</br>
실제 구현은 from collections import deque해서 queue=deque([start])</br>

def bfs(graph,start,visited):</br>
    queue = deque([start])  # 큐를 사용하니 연결순대로 방문할필요 없음</br>
    visited[start] = True</br>
    while queue:</br>
        v = queue.popleft()</br>
        for i in graph[v]:</br>
            if not visited[i]:</br>
                queue.append(i)  # 매번 방문안한 자식노드들은 큐에 들어감</br>
                visited[i]=True</br>


DFS BFS :  [2583, 11403, 1389, 14502, 2636, 17070, 2644, 2606, 11724, 1967, 11725, 7569, 16236, 16953, 2667, 2178, 17471, 1976, 2589, 11559, 1012, 16234, 1260, 14226, 7576, 1167, 2468, 2146, 13913, 17472, 1937, 13023, 18352, 1520, 2250, 1068, 13460, 13549, 12851, 2573, 17142, 1726, 1939, 1707, 2206, 1325, 19238, 3197, 1600]