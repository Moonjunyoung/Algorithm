from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(my_cur_x,my_cur_y):
    global board,n,l,r,visited
    queue=deque()
    queue.append([my_cur_x,my_cur_y])
    change_pos=[]
    flag=False
    total=0
    while queue:
        cur_x,cur_y=queue.popleft()
        for i in range(4):
            da=dx[i]+cur_x
            db=dy[i]+cur_y

            # 현재 맵을 넘어가는경우
            if da<0 or db<0 or da>=n or db>=n:continue
            # 1. 현재좌표에서 국경선을 열수있는곳을 찾는다 .
            isvisited=abs(board[cur_x][cur_y]-board[da][db])
            if isvisited>=l and isvisited<=r and visited[da][db]==False: #국경선을 열수있으면
               visited[da][db]=True
               queue.append([da,db])
               total+=board[da][db]
               change_pos.append([da,db])
               flag=True


    # 2 .연합이 존재한다면 해당 좌표를 갱신한다.
    if flag:
        avg=total//len(change_pos)
        for i in change_pos:
            a,b=i
            board[a][b]=avg
        return True
    else:
        return False




n,l,r=map(int,input().split())
board=[0]*n
for i in range(n):board[i]=list(map(int,input().split()))
# 1. 입력을 받는다.
answer=0

while True:
    visited = [False] * n
    for i in range(n):visited[i]=[False]*n

    flag=False
    for i in range(n):
        for j in range(n):
            if visited[i][j]==False:
                if bfs(i,j):
                   flag=True

    if flag==False:
        print(answer)
        break

    answer+=1


