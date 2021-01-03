dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(cur_x,cur_y,cur_x2,cur_y2,button):
    global coin_pos,n,m,board,answer

    if button>=10:
        return

    for i in range(4):
        da=dx[i]+cur_x
        db=dy[i]+cur_y
        da_2=dx[i]+cur_x2
        db_2=dy[i]+cur_y2
        cnt=0
        if da<0 or da>=n or db<0 or db>=m: #범위를 나가면
            cnt+=1
        if da_2 < 0 or da_2 >= n or db_2 < 0 or db_2 >= m:  # 범위를 나가면
            cnt += 1

        if cnt == 1: # 1. 둘중 하나만 나간경우 정답 갱신
           answer = min(button + 1, answer)
           return


        if cnt==2:continue # 2. 두 동전 둘다 나가면 이동 x

        # 이동하려는곳이 벽이면 해당 동전은 이동 x 현재위치 그대로
        if board[da][db]=='#':
            da,db=cur_x,cur_y

        if board[da_2][db_2]=='#':
            da_2,db_2=cur_x2,cur_y2

        dfs(da,db,da_2,db_2,button+1)

    return

n,m=map(int,input().split())
board=[0]*n
for i in range(n):
    board[i]=list(map(str,input()))

answer=999999999
coin_pos=[]
for i in range(n):
    for j in range(m):
        if board[i][j]=='o':
            coin_pos.append([i,j])


dfs(coin_pos[0][0],coin_pos[0][1],coin_pos[1][0],coin_pos[1][1],0)
if answer==999999999:
    print(-1)
else:
    print(answer)