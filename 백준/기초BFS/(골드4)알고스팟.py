from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]

m,n=map(int,input().split())

board=[0]*n
visited=[False]*n
for i in range(n):
    board[i]=list(map(int,input()))
    visited[i]=[False]*m

queue=deque()
queue.append([0,0,0]) # 1. 현재 좌표 와 벽을 부순횟수를 넣음
visited[0][0]=True

while queue:
      cur_x,cur_y,Break_wall=queue.popleft()

      if cur_x ==n-1 and cur_y==m-1:
          print(Break_wall)
          break

      for i in range(4):
          nx=dx[i]+cur_x
          ny=dy[i]+cur_y

          if nx<0 or ny<0 or nx>=n or ny>=m:continue
          # 2. 벽을 안부셔도되는경우
          if board[nx][ny]==0 and visited[nx][ny]==False:
             visited[nx][ny]=1
             queue.appendleft([nx,ny,Break_wall])

          # 3. 벽을 부셔야하는경우 (벽을 부셧으니 벽부순횟수를 갱신)
          elif board[nx][ny]==1 and visited[nx][ny]==False:
               visited[nx][ny]=True
               queue.append([nx,ny,Break_wall+1])
