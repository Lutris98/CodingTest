n, m = map(int,input().split())

occupied = [[0]*m for i in n]
for i in range(n):
    occupied[i] = list(map(int,input().split()))
    
# n, m 주어지자마자 직사각형의 graph작성가능(만약 2,2라면)
adjacent=[[(2,1),(3,1),(4,0)],
          [(3,0),(4,1)],
          [(4,1)]]  # 하지만 일반화모르겠음
# 그이후는 adjacent의 true여부 검색하면 되는데 DFS, BFS 차이도 모르겠음
