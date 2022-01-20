# 2019 국가교육기관 코딩테스트
condition = input().split()  # 여러개 입력은 split으로 리스트만듦 #input안에 인수필요없음

N = condition[0]
M = condition[1]
K = condition[2]

given = input().split()

import time
start_time = time.time()  # 다 입력하고 

condition = list(map(int,condition))  # map함수는 인수가 안에 있으며 return값 활용

given = list(map(int,given))
given.sort()  # sort함수는 인수가 밖에 inplace True(특이한 쪽) # 오름차순이 기본

a = given[-1]
b = given[-2]
c = a * (M-int(M/(K+1))) + b * int(M/(K+1))  # 분수는 괄호로 범위주의
print(c)

end_time = time.time()
print('time : ',end_time-start_time)