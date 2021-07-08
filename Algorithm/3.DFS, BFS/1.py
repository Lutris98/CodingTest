visited = [False] * 9
def dfs(graph, v, visited):  # 실제 구현은 재귀함수로 하나 원론적 구현은 스택에 인접노드하나 push해서 만듦하고 인접노드 떨어지면 pop한느 방식으로
    visited[v] = True  # 현재 노드 방문처리
    print(v, end='')
    for i in graph[v]:
        if not visited[i] : dfs(graph,i,visited)  # 모든 노드에 대해 재귀적으로 방문  #노드 작은 순서도 필수가 아니니 충분
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
dfs(graph,1,visited)

