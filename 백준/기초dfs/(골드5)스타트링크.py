from collections import deque

f,s,g,u,d=map(int,input().split())


queue=deque()
dist=[0]*(f+1)
check=[False]*(f+1)
queue.append(s) ##광호의 위치를 넣음
check[s]=True

while queue:
    cur=queue.popleft()
    if cur==g:
        print(dist[g])
        exit(0)

    if cur+u<=f and check[cur+u]==False: ##광호가 위로 올라갈떄
       check[cur+u]=True
       queue.append(cur+u)
       dist[cur+u]=dist[cur]+1

    if cur-d>0 and check[cur-d]==False: #광호가 내려갈떄
       check[cur-d]=True
       queue.append(cur-d)
       dist[cur-d]=dist[cur]+1



# while문을 빠져나온거는 해당 좌표를 못찾은것이므로 계단으로 밖에 못감
print('use the stairs')
