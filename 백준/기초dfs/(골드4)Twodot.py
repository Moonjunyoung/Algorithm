dx=[0,0,1,-1]
dy=[1,-1,0,0]
def dfs(cur_x,cur_y,start_alpha,start_x,start_y,cnt):
    global board,visited,n,m


    for i in range(4):
        nx=dx[i]+cur_x
        ny=dy[i]+cur_y
        if nx<0 or ny<0 or nx>=n or ny>=m:continue
        if board[nx][ny]!=start_alpha:continue

        if visited[nx][ny]==False:
            visited[nx][ny]=True
            dfs(nx,ny,start_alpha,start_x,start_y,cnt+1)
            visited[nx][ny]=False

        else: # 방문을 했지만 시작점과 같고 4번이상 이동한 경우 
            if nx == start_x and ny == start_y and cnt >= 4:
                print('Yes')
                exit(0)


    return

n,m=map(int,input().split())
board=[0]*n
visited=[0]*n
for i in range(n):
    a=input()
    board[i]=list(a)
    visited[i]=[False]*m


for i in range(n):
    for j in range(m):
        visited[i][j]=True
        dfs(i,j,board[i][j],i,j,1)
        visited[i][j]=False


print('No')