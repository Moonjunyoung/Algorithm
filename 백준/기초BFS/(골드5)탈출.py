from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]
r,c=map(int,input().split())
dist=[0]*r
water_dist=[0]*r
board = [list(map(str, input())) for _ in range(r)]
for i in range(r):
    dist[i]=[0]*c
    water_dist[i]=[0]*c


queue=deque()
water=deque()
ans_x=0
anx_y=0
for i in range(r):
    for j in range(c):
        if board[i][j]=='S':
           queue.append([i,j]) ##고슴도치좌표를넣음
        elif board[i][j]=='*':
            water.append([i,j]) ##물의 좌표를 넣음
        elif board[i][j]=='D':
             ans_x=i
             anx_y=j


# 1. 물의 bfs를 돌려서 위치를 확인함
while water:
      cur_x,cur_y=water.popleft()
      for i in range(4):
          d_x=cur_x+dx[i]
          d_y=cur_y+dy[i]
          if d_x<0 or d_y<0 or d_x>=r or d_y>=c:continue
          if water_dist[d_x][d_y]!=0:continue
          if board[d_x][d_y]=='.' or board[d_x][d_y]=='S':
             water_dist[d_x][d_y]=water_dist[cur_x][cur_y]+1
             water.append([d_x,d_y])





# 2. 고슴도치의 bfs를 돌리는데 
while queue:
      cur_x,cur_y=queue.popleft()
      for i in range(4):
          d_x=cur_x+dx[i]
          d_y=cur_y+dy[i]
          if d_x<0 or d_y<0 or d_x>=r or d_y>=c:continue
          if dist[d_x][d_y]!=0:continue
          if board[d_x][d_y]=='.' or board[d_x][d_y]=='D': 
            if water_dist[cur_x][cur_y]==0: ##물이 방문 안한곳이면 그냥 좌표값 갱신함
               dist[d_x][d_y] = dist[cur_x][cur_y] + 1
               queue.append([d_x, d_y])

            elif dist[cur_x][cur_y]+1<=water_dist[cur_x][cur_y]: ##그런데 물이 방문한곳이고 고슴도치가 방문하려는곳이 물이 방문했던좌표보다 작거나 같아야 이동가능
                dist[d_x][d_y]=dist[cur_x][cur_y]+1
                queue.append([d_x,d_y])


if dist[ans_x][anx_y]==0:
    print('KAKTUS')
else:
    print(dist[ans_x][anx_y])