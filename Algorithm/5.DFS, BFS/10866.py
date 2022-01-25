# queue 만드는 문제

class deque():
    def __init__(self):
        self.queue = []

    def push_front(self,x):
        self.queue.insert(0,x) #insert없었으면 곤란했을뻔
        return self.queue

    def push_back(self,x):
        self.queue.append(x)
        return self.queue

    def pop_front(self):
        if len(self.queue)==0 : return -1
        else : return self.queue.pop(0)  #기본 deque는 pop(0)과 같음, 첫번째를 빼고 인덱스 밀어주기  # pop숫자출력하고 queue도 바뀌고

    def pop_back(self):
        if len(self.queue)==0 : return -1
        else : return self.queue.pop()

    def size(self):
        return len(self.queue)

    def empty(self):
        if len(self.queue)==0 :
            return 1
        else : return 0

    def front(self):
        if len(self.queue)==0 : return -1
        else :
            return self.queue[0]

    def back(self):
        if len(self.queue)==0 : return -1
        else : 
            return self.queue[-1]

import sys
n = sys.stdin.readline()

method = ['']*n
q = deque()

for i in range(n):
    method[i] = input()
for i in range(n):
    if ' ' in method[i]:
        x = int(method[i].split(' ')[1])
        method[i] = method[i].split(' ')[0]
    if method[i] == 'push_front' : q.push_front(x)
    elif method[i] == 'push_back' : q.push_back(x)
    elif method[i] == 'pop_front' : print(q.pop_front())
    elif method[i] == 'pop_back' : print(q.pop_back())
    elif method[i] == 'size' : print(q.size())
    elif method[i] == 'empty' : print(q.empty())
    elif method[i] == 'front' : print(q.front())
    elif method[i] == 'back' : print(q.back())