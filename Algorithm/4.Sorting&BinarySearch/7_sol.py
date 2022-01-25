# 난 이진탐색으로 풀 생각도 못했음
# parametric search 유형의 문제(최적화문제를 yesno문제로 치환하는 기법) 주로 이진탐색으로 해결
# 해보고 오차계속 줄여나가는 방식(머신러닝 방식)

n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0  # start와 end는 이진탐색을 적용한 작위적 설정(mid만 의미있음)
end = max(array)
result = 0
while (start<=end):
    total = 0
    mid = (start+end)//2
    for x in array:  # total구하기
        if x>mid: total += x-mid
    if total<m: end = mid-1
    else: 
        result = mid
        start = mid+1
print(result)
