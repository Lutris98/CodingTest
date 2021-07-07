N = int(input())
route = input().split()
location=[1,1]

for a in route:
    if a == 'R' : location[1]+=1  #route길이상 나갈 일은 없음
    elif a == 'L' : location[1]-=1
    elif a == 'D' : location[0]+=1
    else : location[0] -= 1
    if location[0]<1 : location[0]=1  # continue, break문은 for, while같은 반복문만 해당  #for과 같은 수준에 있어야함
    if location[1]<1 : location[1]=1
print('{0} {1}'.format(location[0],location[1]))

# if문안에 continue넣는게 안되다 보니까 진짜 미개하게 코드를 짜게 되었음