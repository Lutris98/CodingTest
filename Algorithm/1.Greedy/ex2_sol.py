n,m,k = map(int,input().split())  #내 코드 다섯줄 # map객체를 이런식으로 언패킹하기도 하는군, input은 안에 들어가 있기만 하면 알아서 입력받음
data = list(map(int,input().split()))  # 제약을 딱히 코드로 걸지는 않네

data.sort()
first = data[-1]
second = data[-2]

count = int(m / (k+1)) * k  # 몫개수 만큼 k번 반복후 나머지 더해주기(번거로워보이지만 코드가 깔끔)
count += m % (k+1)

result = 0
result += count * first
result += (m-count) * second
print(result)

#문제에 있는 조건 구현할 필요없네?!

