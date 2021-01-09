from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]

# 물고기를 먹음
def eat_fish(my_fish_list):
    # 1. 거리  , 2. 가장위에있는 물고기 3. 가장왼쪽에있는물고기 순으로 정렬
    my_fish_list=sorted(my_fish_list,key= lambda x:(x[2],x[0],x[1]))
    return my_fish_list[0]


# 내 상어의 위치를 찾는다
def find_my_shark():
    global board,n
    for i in range(n):
        for j in range(n):
            if board[i][j]==9:
                return [i,j]

# bfs를 통해 먹을수있는 물고기를 찾으러간다.
def bfs(cur_x,cur_y):
    global board,n,shark,eat_cnt,time

    visited=[False]*n
    for i in range(n):visited[i]=[False]*n
    queue = deque()
    queue.append([cur_x,cur_y,0])
    visited[cur_x][cur_y]=True
    flag=False
    my_fist_list=[]
    while queue:
          c_x,c_y,dist=queue.popleft()
          for i in range(4):
              nx=c_x+dx[i]
              ny=c_y+dy[i]
              # 1. 자기보다 큰 물고기가 있으면 못지나감
              if nx<0 or nx>=n or ny<0 or ny>=n or visited[nx][ny] or board[nx][ny]>shark:continue

              # 2. 빈칸이거나 자기랑 같으면 그냥 지나감
              if board[nx][ny]==0 or board[nx][ny]==shark:
                  visited[nx][ny]=True
                  queue.append([nx,ny,dist+1])

              # 3. 빈칸이 아니고 물고기를 먹을수있는물고기
              elif board[nx][ny]!=0 and board[nx][ny]<shark:
                   visited[nx][ny]=True
                   queue.append([nx, ny, dist + 1])
                   my_fist_list.append([nx,ny,dist+1])
                   flag=True


    # 먹을수있는 물고기가 존재하면
    if flag:
        fish_x,fish_y,fish_dist=eat_fish(my_fist_list)
        board[fish_x][fish_y]=9
        board[cur_x][cur_y]=0
        eat_cnt+=1
        #물고기를 먹었으니 해당 물고기의 거리를 추가시킴
        time+=fish_dist
        return True

    # 먹을수 있는 물고기가 존재하지 x
    else:
        return False





n=int(input())
board=[0]*n
for i in range(n):
    board[i]=list(map(int,input().split()))

shark=2 # 1. 아기상어의 초기상태
eat_cnt=0
time=0
while True:
     my_x, my_y = find_my_shark() # 현재 내상어의 위치를 찾는다 
     if bfs(my_x,my_y):
        if eat_cnt==shark: # 1. 상어의크기만큼 먹었으면 진화시킴
           eat_cnt=0
           shark+=1
     else:
         break


print(time)