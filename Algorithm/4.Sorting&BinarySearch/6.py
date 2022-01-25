n = int(input())  # n범위가 백만
store = list(map(int,input().split()))
store.sort()  # 정렬이 필수인 것 잊지 말기
m = int(input())
client = list(map(int,input().split()))
client.sort()
def binary_search(array,target,start,end):  # 즉석에서 적기 쉽구만
    mid = (start+end)//2
    if array[mid]==target: return mid+1
    elif array[mid]>target: return binary_search(array,target,start,mid-1)
    else: return binary_search(array,target,mid+1,end)  # 빠져나갈 가능성?
for i in client:
    if binary_search(store,i,0,n-1)==False:  # 한번이라도 걸리면 아웃 구현하려면 no가 먼저
        print('no')
    else: print('yes')

# 없을 때 구현을 어떻게 하는 건지 잘 모르겠음