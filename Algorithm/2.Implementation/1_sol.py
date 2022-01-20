n = int(input())
x,y = 1,1  #언패킹
plans = input().split()

dx = [0,0,-1,1]  #테트리스하면서 많이 본 방식(움직임을 리스트로 변환)
dy = [-1,1,0,0]
moves = ['L','R','U','D']

for plan in plans :
    for i in range(len(moves)):  #움직임별 경로검토
        if plan == moves[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        if x < 1 or y < 1 or x > n or y > n: continue  # 조건 만족하면 for문 바로 나감(앞선코드 실행안함)
        x,y = nx,ny  # nx,ny만드는 이유는 조건을 만족하지 않았을때 갱신하지 않는 방식이 제일 깔끔
print(x,y)