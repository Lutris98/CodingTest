x = 0  # 파이썬은 변수형까지 설정해줄 필요는 없음
a = 0  # a,b,c는 각각 500,100,50원 개수(긴 수식보다 깔끔하게 변수지정)
b = 0
c = 0
N = int(input("손님이 낸 돈은 : "))  #input은 항상 str형태로

if N < 50 :
    x = N/10
elif N < 100 :
    c = int(N/50)
    N = N - 50*c
    x = c + N/10
elif N < 500 :  # 항상 반복되는 구조에는 민감해야 한다(계속 N-100*b하기보단 N갱신)
    b= int(N/100)
    N = N - 100*b
    c = int(N/50)
    x = b + c + N/10
else :
    a = int(N/500)
    N = N - 500*a
    b = int(N/100)
    N = N - 100*b
    c = int(N/50)
    N = N - 50*c
    x = a +b + c + N/10

print(f"동전 {int(x)}개 드리겠습니다")  # fstring으로 통일하자