# 직접 해보면서 문제를 작은 문제들로 나눌 수 있다는 것을 깨달음

n = int(input())

def hanoi(n):
    move = 0
    print(hanoi(n))
    if n==1 : 
        print(1,' ',3)
        move+=1
        return move
    if n==2:
        print(1,' ',2)
        print(1,' ',3)
        print(2,' ',3)
        move+=2
        return move
    







print(hanoi())