from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def game_over():
    global board,n,m
    for i in range(n):
        for j in range(m):
            if board[i][j]==1:
                return True
    return False

def dispear_check(cur_x,cur_y):
    cnt=0
    global board,n,m
    for i in range(4):
        nx=cur_x+dx[i]
        ny=cur_y+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m:continue
        if visited[nx][ny]==True:
           cnt+=1

    if cnt>=2:
       return True
    else:
        return False

def bfs():
    global visited,n,m,board
    queue=deque()
    queue.append([0,0])
    visited[0][0]=True

    while queue:
          c_x,c_y=queue.popleft()
          for i in range(4):
              nx=c_x+dx[i]
              ny=c_y+dy[i]
              if nx<0 or ny<0 or nx>=n or ny>=m:continue
              if board[nx][ny]==0 and visited[nx][ny]==False:
                 visited[nx][ny]=True
                 queue.append([nx,ny])

    return


n,m=map(int,input().split())
board=[0]*n
answer=0
for i in range(n):
    board[i]=list(map(int,input().split()))

while game_over():
      visited = [False] * n
      for i in range(n):
        visited[i] = [False] * m

      bfs()
      for i in range(n):
          for j in range(m):
              if board[i][j] == 1:
                  if dispear_check(i, j):
                     board[i][j]=0

      answer+=1


print(answer)