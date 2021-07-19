# 국제 알고리즘 대회
x = int(input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
count = 1
for i in range(opt):  # 재귀함수처럼 구현도전
    mina = min(x)
    maxb = max(b)
    a.remove(mina)  # 위치가 중요하지 않아!
    a.append(maxb)
    b.remove(maxb)
    b.append(mina)
    count+=1
    if mina==maxb: break
    opt = count
