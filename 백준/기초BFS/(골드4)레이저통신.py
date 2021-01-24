from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def bfs(start_x,start_y,end_x,end_y):
    global w,h,board,lazor_list

    visited=[0]*h
    for i in range(h):visited[i]=[-1]*w
    queue = deque()

    # 1. 현재 시작하는 위치에서의 네방향의 cost를 0으로 두고 시작
    for i in range(4):
        queue.append([start_x,start_y,i,0])


    visited[start_x][start_y]=0

    while queue:
          cur_x,cur_y,dir,cost=queue.popleft()
          for i in range(4):
              nx=cur_x+dx[i]
              ny=cur_y+dy[i]
              if nx<0 or ny<0 or nx>=h or ny>=w:continue
              if board[nx][ny]=='*':continue

              next_cost=cost
              if dir!=i: # 방향이 다를경우 거울을 설치해야됨
                  next_cost+=1

              if visited[nx][ny]==-1: # 1. 처음방문인곳이면 그냥 현재 cost 갱신
                 visited[nx][ny]=next_cost
                 queue.append([nx,ny,i,next_cost])

              elif visited[nx][ny]!=-1: # 2. 이미 방문한 위치인데 현재까지 이동한경로에서 거울개수가 적을경우 갱신이가능
                   if visited[nx][ny]>=next_cost:
                      visited[nx][ny]=next_cost
                      queue.append([nx, ny,i,next_cost])


    return visited[end_x][end_y]


w,h=map(int,input().split())
board=[0]*h
for i in range(h):
    a=input()
    board[i]=list(a)

lazor_list=[]
for i in range(h):
    for j in range(w):
        if board[i][j]=='C':
            lazor_list.append([i,j])

print(bfs(lazor_list[0][0],lazor_list[0][1],lazor_list[1][0],lazor_list[1][1]))
