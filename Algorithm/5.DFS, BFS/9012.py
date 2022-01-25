# stack아이디어 떠올리는 문제

# 처음엔 replace(')(','),(')해서 나눌 생각했는데 주어진 예시에 (()())있었음

def is_vps(s):
    stack = []
    for i in s:
        if i == '(': stack.append(i)
        else : 
            if stack != [] : stack.pop()
            else : return 'NO'
    if stack == [] : return 'YES'
    else : return 'NO'

t = int(input())
ps = ['']*t

for i in range(t):
    ps[i] = input()
    
for i in range(t):
    print(is_vps(ps[i]))