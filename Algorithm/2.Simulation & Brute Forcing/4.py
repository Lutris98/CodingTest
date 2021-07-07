scale = list(map(int,input().split()))
a,b,c = map(int,input().split())
mymap = list(range(scale[0]))
for i in range(scale[0]) :
    mymap[i] = list(map(int,input().split()))
loc = [a,b]


# 삼성전자 코테에서 자주 출제되는 유형이라는데 아무래도 개발자는 아닌가...
# 움직임은 방향까지 해서 너무 복잡했다...