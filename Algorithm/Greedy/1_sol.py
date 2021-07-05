n = int(input("손님이 낸 돈은 : "))
count = 0  # 변수이름 센스

coin_types = [500,100,50,10]

for coin in coin_types :  #for문으로 반복을 극도로 줄임(리스트활용 익숙해지자)
    count += n // coin
    n %= coin

print(count)

# 그리디로 풀 수 있는 이유는 동전조합의 큰 단위가 작은 단위의 배수이기 때문(작은 쪽으로 표현된 조합은 대체가능)