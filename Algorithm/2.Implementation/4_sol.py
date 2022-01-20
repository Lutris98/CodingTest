n, m = map(int, input().split())
x, y, direction = map(int, input().split())

d = [[0]*m for i in range(n)]  # 2차원 리스트엔 컴프리헨션이 최고임(기억하길) # 방문했던 곳은 따로 관리
d[x][y] = 1

mymap = []
for i in range(n) :
    mymap.append(list(map(int, input().split())))
dx = [-1,0,1,0]  #방향의 역할은 움직임의 종류결정뿐임
dy = [0,1,0,-1]

def turn_left() :  # 동작 반복되는 것은 함수로
    global direction  #전역변수는 그대로 활용해도 되지만 명시해주는 게 깔끔
    direction-=1
    if direction==-1 : direction=3

count = 1
turns=0  #네 방향모두 찾아봤을때 위한 디테일(간단)
while True:  #무한반복은 while문
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny]==0 and mymap[nx][ny]==0:  #일단 좌표옮긴뒤 가본여부랑 육지여부판단
        d[nx][ny]=1
        x = nx
        y = ny
        count +=1
        turns=0
        continue
    else: turns+=1
    if turns==4:
        nx = x - dx[direction]  #방향유지한채로 뒤로가는 것 구현
        ny = y - dy[direction]
        if mymap[nx][ny]==0:
            x = nx
            y = ny
        else: break
        turns=0
print(count)