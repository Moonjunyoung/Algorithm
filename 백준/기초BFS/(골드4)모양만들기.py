from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(cur_x,cur_y):
    global board,visited,group,row,col
    cnt=1
    queue=deque()
    queue.append([cur_x,cur_y])
    visited[cur_x][cur_y]=group

    while queue:
        c_x,c_y=queue.popleft()
        for i in range(4):
            nx=dx[i]+c_x
            ny=dy[i]+c_y
            if 0<=nx<row and 0<=ny<col and board[nx][ny]==1:
               if visited[nx][ny]==0:
                   visited[nx][ny]=group
                   queue.append([nx,ny])
                   cnt+=1

    return cnt




row,col=map(int,input().split())
board=[0]*row
visited=[0]*row
answer=0
group_list=[0]
group=1
for i in range(row):
    board[i]=list(map(int,input().split()))
    visited[i]=[0]*col



# 1. bfs를 돌려서 1끼리 그룹핑을 한다.
for i in range(row):
    for j in range(col):
        if board[i][j]==1 and visited[i][j]==0:
           group_list.append(bfs(i,j))
           group+=1

# 2. 0의 위치에서 group 된 정보들을 통해 모양을 찾는다.
for i in range(row):
    for j in range(col):
        if board[i][j]==0:
            near=set()
            for z in range(4):
                nx=dx[z]+i
                ny=dy[z]+j
                if 0 <= nx < row and 0 <= ny < col and board[nx][ny] ==1:
                    near.add(visited[nx][ny]) # group핑된 좌표를 넣는다.

            s=1 # 0포함이니 1
            for x in near:
                s+=group_list[x]

            answer=max(s,answer)

print(answer)

