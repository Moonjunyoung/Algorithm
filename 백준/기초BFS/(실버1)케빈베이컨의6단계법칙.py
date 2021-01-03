from collections import deque
n,m=map(int,input().split())
friend=[0]*(n+1)
for i in range(1,n+1):friend[i]=list()


for i in range(m):
    a,b=map(int,input().split())
    friend[a].append(b)
    friend[b].append(a)



answer_list=[0]*(n+1)
answer_list[0]=9999999
for i in range(1,n+1):
    queue=deque()
    queue.append(i)
    visited=[False]*(n+1)
    dist=[0]*(n+1)
    visited[i]=True
    while queue:
        cur=queue.popleft()
        for j in friend[cur]:
            if visited[j]==False:
                visited[j]=True
                dist[j]=dist[cur]+1
                queue.append(j)

    answer_list[i]=sum(dist)


print(answer_list.index(min(answer_list)))