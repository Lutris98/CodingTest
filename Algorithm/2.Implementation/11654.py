x = input()
if type(x) is str:  # 파이썬에서 type으로 변수의 자료형 검사, ord로 문자의 아스키코드값
    print(ord(x))
else : print(chr(x))