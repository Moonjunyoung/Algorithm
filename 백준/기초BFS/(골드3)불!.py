from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def fire_bfs():
    global board,fire_dist,fire_queue
    while fire_queue:
        cur_x, cur_y = fire_queue.popleft()
        for i in range(4):
            da = dx[i] + cur_x
            db = dy[i] + cur_y

            if da < 0 or db < 0 or da >= r or db >= c: continue
            if board[da][db] != '#' and fire_dist[da][db] == 0:
                fire_dist[da][db] = fire_dist[cur_x][cur_y] + 1
                fire_queue.append([da, db])


r,c=map(int,input().split())
board=[0]*r
fire_dist=[0]*r
jihun_dist=[0]*r
for i in range(r):
    board[i]=list(map(str,input()))
    fire_dist[i]=[0]*c
    jihun_dist[i]=[0]*c

fire_queue=deque()
queue=deque()
for i in range(r):
    for j in range(c):
        if board[i][j]=='F':
            fire_queue.append([i,j])
        elif board[i][j]=='J':
            queue.append([i,j])


if len(fire_queue)!=0:
    fire_bfs()

for i in range(r):
    for j in range(c):
        if fire_dist[i][j]==0:
            fire_dist[i][j]=99999999


while queue:
      cur_x,cur_y=queue.popleft()
      for i in range(4):
          da=dx[i]+cur_x
          db=dy[i]+cur_y

          if da>=r or db>=c or da<0 or db<0:
             if board[cur_x][cur_y]=='.' or board[cur_x][cur_y]=='J': # 1. 현재 위치에서 탈출이 가능한지 확인
                if jihun_dist[cur_x][cur_y]<fire_dist[cur_x][cur_y]:
                   print(jihun_dist[cur_x][cur_y]+1)
                   exit(0)

          if da < 0 or db < 0 or da >= r or db >= c:continue
          if jihun_dist[da][db]!=0:continue # 2. 이미 방문한위치면 넘김


          if board[da][db]=='.' and jihun_dist[cur_x][cur_y]+1<fire_dist[da][db]: # 해당 위치로 이동할떄 불이 번져있지않으면 이동
            jihun_dist[da][db]=jihun_dist[cur_x][cur_y]+1
            queue.append([da,db])


print('IMPOSSIBLE')