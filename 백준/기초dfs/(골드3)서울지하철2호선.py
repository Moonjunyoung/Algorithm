from collections import deque
def dfs(cur,start,cnt):
    global graph,visit,n,Cycle_list

    for i in graph[cur]:
        if visit[i]==0:
            visit[i]=cnt+1
            dfs(i,start,cnt+1)
        elif visit[i]!=0 and cnt>2:
             if start==i: # 1. 순환선이다.
                for x in range(start,n+1): # 2. 싸이클의 시작지점으로 부터  미방문인 노드를 제외하고 순환되는노선을 찾음
                    if visit[x]==0:continue
                    if visit[x]<=visit[start]:
                        Cycle_list.add(x)
    return

n=int(input())
queue=deque()
Cycle_list=set()
answer=[0]*(n+1)
dist=[0]*(n+1)
graph=[[] for _ in range(n+1)]
visit = [0] * (n + 1)
t=n
while t!=0:
      a,b=map(int,input().split())
      graph[a].append(b)
      graph[b].append(a)
      t-=1


# 1. 순환선을 찾으러감 (순환선은 싸이클로 형성되어있음 단 움직인횟수가 3이상이어야함)
for i in range(1,(n+1)):
    visit = [0] * (n + 1)
    visit[i]=1
    dfs(i,i,1)



# 순환선의 정점들
for x in Cycle_list:
    visit[x]=-1
    queue.append(x)



# 2.순환선부터 순환선이 아닌곳까지 bfs로 얼마나걸리는 지확인
while queue:
      cur=queue.popleft()
      for i in graph[cur]:
          if visit[i]==-1:continue ## 순환선이면 continue
          if dist[i]==0 or dist[i]>dist[cur]+1:
             dist[i]=dist[cur]+1
             queue.append(i)

for x in range(1,len(dist)):
    print(dist[x],end=' ')