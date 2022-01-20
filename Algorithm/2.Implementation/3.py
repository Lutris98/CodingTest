loc = input()
mydict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
x, y = int(loc[1]), mydict[loc[0]] #딕셔너리 애용하자(판다스가 아닌 기본 replace는 제한적임)
dx = [-2,-2,-1,-1,1,1,2,2]
dy = [-1,1,-2,2,-2,2,-1,1]
nx,ny = list(range(8)),list(range(8))  #리스트는 입력받더라도 빈리스트만들어야한다 # 배열과 리스트는 차이있음!(map도 마찬가지)
count=0
for i in range(8):
    nx[i] = x + dx[i]
    ny[i] = y + dy[i]
    if nx[i]<1 or ny[i]<1 or nx[i]>8 or ny[i]>8 : continue
    count+=1
print(count)

# 역시 경험이 최고야