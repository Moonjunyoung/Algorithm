dx=[-1,0,1,0]
dy=[0,1,0,-1]
#0 = 북 , 1= 동쪽 ,2=남쪽 3=서쪽

def dfs(cur_x,cur_y,robot_dir): # 현재위치 ,방향
    global board,row,col
    if board[cur_x][cur_y]==0: #빈칸인경우
        board[cur_x][cur_y]=2 ##청소완료

    tmp=robot_dir
    #0 = 북 , 1= 동쪽 ,2=남쪽 3=서쪽
    # 북쪽->서쪽->남쪽->동쪽
    for _ in range(4):
        if robot_dir==0: #북쪽이면 서쪽으로
            robot_dir=3
        elif robot_dir==1: #동쪽이면
             robot_dir=0 #북쪽
        elif robot_dir==2: #남쪽이면
             robot_dir=1 #동쪽
        elif robot_dir==3: #서쪽이면
             robot_dir=2 #남쪽

        d_x=dx[robot_dir]+cur_x
        d_y=dy[robot_dir]+cur_y
        if d_x<0 or d_y<0 or d_x>=row or d_y>=col:continue #범위를 넘어가면
        if board[d_x][d_y]==0: ##해당 방향이 청소하지않은경우  청소하러감
            dfs(d_x,d_y,robot_dir)


    #0 = 북 , 1= 동쪽 ,2=남쪽 3=서쪽
    #네방향 모두 청소가 이미 되어있으면 현재 좌표에서 후진한다. (이점에서 실수한듯)
    if tmp==0: # 북쪽방향이면 뒤로
        cur_x+=1
    elif tmp==1: # 동쪽
         cur_y-=1
    elif tmp==2:
         cur_x-=1
    elif tmp==3:
         cur_y+=1


    #후진한 방향이 범위를 넘어서거나 벽인경우 현재 좌표 방향에서 후진
    if cur_x < 0 or cur_y < 0 or cur_x >= row or cur_y >= col or board[cur_x][cur_y]==1:
        answer=0
        for i in range(row):
            for j in range(col):
                if board[i][j]==2:
                    answer+=1

        print(answer)
        exit(0)
    else:
        dfs(cur_x,cur_y,tmp)




row,col=map(int,input().split())
board=[0]*row
cur_x,cur_y,dir=map(int,input().split())
for i in range(row):board[i]=list(map(int,input().split()))
dfs(cur_x,cur_y,dir)
