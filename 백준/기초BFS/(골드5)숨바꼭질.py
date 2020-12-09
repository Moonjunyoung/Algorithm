import collections

n,k=map(int,input().split())

dist=[0]*200001
check=[False]*200001
queue=collections.deque()
queue.append(n) ##현재위치를 넣고 최단거리를 구함

check[n]=True
while queue:
    cur=queue.popleft()
    #점이 100000 까지 들어오므로 최대범위는 200000임 
    
    if cur+1<200001 and check[cur+1]==False:
       check[cur+1]=True
       queue.append(cur+1)
       dist[cur+1]=dist[cur]+1

    if cur-1>=0 and check[cur-1]==False:
       check[cur-1]=True
       queue.append(cur-1)
       dist[cur-1]=dist[cur]+1

    if 2*cur<200001 and check[2*cur]==False:
       check[2*cur]=True
       queue.append(2*cur)
       dist[2*cur]=dist[cur]+1



print(dist[k])

