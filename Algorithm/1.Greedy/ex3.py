# 2019 국가교육기관 코딩테스트
data = []
candidate = []
n,m = map(int,input().split())
for i in range(n) :
    data.append(list(map(int, input(x).split())))  # data[0]처럼하면 빈 리스트에 했다고 오류남
    candidate.append(min(data[i]))
print(max(candidate))