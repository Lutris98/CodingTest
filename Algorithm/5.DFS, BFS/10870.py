# 재귀함수에 대한 내용

import sys
n = int(sys.stdin.readline())

def pibonacci(nth):
    numbers = []
    if nth == 0 : return 0 
    elif nth == 1 : return 1 
    else : return pibonacci(nth-1) + pibonacci(nth-2)

print(pibonacci(n))