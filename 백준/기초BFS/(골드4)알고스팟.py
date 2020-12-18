from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]

col,row=map(int,input().split())
map_view=[0]*row
dist=[-1]*row

for i in range(row):
    map_view[i]=list(map(int,input()))
    dist[i]=[-1]*col

queue=deque()
queue.append([0,0])
dist[0][0]=0
while queue:
    cur_x,cur_y=queue.popleft()

    # 1. 벽일경우에 맨뒤에 넣고 벽이 아닐경우에는 맨앞에 넣음 
    # 2. 벽일경우 dist갱신 벽이아닐경우는 갱신 x
    # 즉 벽이아닌경우의 값이 나오면 먼저처리하고 벽인 값이 나오면 나중에 처리하여 최소 몇개의 벽을 부수는지확인이가능하다.
    for i in range(4):
        da=dx[i]+cur_x
        db=dy[i]+cur_y
        if da<0 or db<0 or da>=row or db>=col:continue
        if dist[da][db]==-1 and map_view[da][db]==1: #벽일경우 맨뒤에넣음 값갱신해야됨
            queue.append([da,db])
            dist[da][db]=dist[cur_x][cur_y]+1 #값갱신

        elif dist[da][db]==-1 and map_view[da][db]==0: #벽이아닐경우 맨앞에넣음
             queue.appendleft([da,db])
             dist[da][db]=dist[cur_x][cur_y]


print(dist[row-1][col-1])