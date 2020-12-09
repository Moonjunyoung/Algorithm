import collections

dx=[0,0,1,-1]
dy=[1,-1,0,0]


col,row=map(int,input().split())
tomato=[]
check=[]
dist=[]
for i in range(row): ##row
    tomato.append(list(map(int,input().split()))) ##col

for i in range(row):
    check.append([False]*col)
    dist.append([0]*col)

queue=collections.deque()

## 익은 토마토를 먼저 큐에 넣음
for i in range(row):
    for j in range(col):
        if tomato[i][j]==1:
            queue.append([i,j])


# bfs를 통해 최단거리를 계산
while queue:
      cur_x, cur_y = queue.popleft()
      for z in range(4):
         da=dx[z]+cur_x
         db=dy[z]+cur_y

         if da<0 or db<0 or da>=row or db>=col:continue
         if check[da][db]==False and tomato[da][db]==0:
            check[da][db]=True
            queue.append([da,db])
            tomato[da][db]=1  # 익혔으므로 1로 만듬
            dist[da][db]=dist[cur_x][cur_y]+1





flag=False
answer=0
for i in range(row):
    for j in range(col):
        if tomato[i][j]==0: ##안익은 토마토가 존재하면 (bfs로 이동할수없어서 토마토를 못익은경우)
            flag=True
            break
        answer=max(dist[i][j],answer)


if flag:
    print(-1)
else:
    print(answer)
