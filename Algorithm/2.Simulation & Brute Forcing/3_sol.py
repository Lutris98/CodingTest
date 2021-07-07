data = input()
row = int(data[1])
col = int(ord(data[0])) - int(ord('a'))+1  # 아스키코드는 알파벳순이라는 걸 알고 있자

steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]  #두가지 형태모두 자주 사용
result = 0
for step in steps :
    nrow = row + step[0]
    ncol = col + step[1]
    if nrow>=1 and nrow<=8 and ncol>=1 and ncol<=8 : result+=1  #다른 방식으로 짜보기
print(result)