from collections import deque
import copy
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def air_move():
    global board,r,c,air_clear

    tmp_board = [0] * r
    check=[False]*r
    for i in range(r):
        tmp_board[i]=[0]*c
        check[i]=[False]*c

    upper_x,upper_y=air_clear[0] #위에
    lower_x,lower_y=air_clear[1] # 아래


    # 1. 위에 공기 청정기 오른쪽 바람이동시킴
    for i in range(c):
        if i>0 and i<c-1:
            tmp_board[upper_x][i+1]=board[upper_x][i]
            check[upper_x][i]=True
            check[upper_x][i+1]=True


    # 1. 위에 공기청정기 위로
    for i in range(upper_x-1,-1,-1):
        tmp_board[i][c-1]=board[i+1][c-1]
        check[i][c-1]=True
        check[i+1][c-1]=True


    # 1. 위에 공기청정기 왼쪽으로
    for i in range(c-1,-1,-1):
        if i >0:
            tmp_board[0][i-1] = board[0][i]
            check[0][i-1]=True
            check[0][i]=True


    #위 공기청정기 아래로
    for i in range(upper_x-1):
        tmp_board[i+1][0]=board[i][0]
        check[i+1][0]=True
        check[i][0]=True


    # 2. 아래 공기 청정기 바람을 오른쪽 으로 이동시킴
    for i in range(c):
        if board[lower_x][i]!=-1 or board[lower_x][i]==0:
            if i>0 and i<c-1:
                tmp_board[lower_x][i+1]=board[lower_x][i]
                check[lower_x][i+1]=True
                check[lower_x][i]=True

    #아래로이동시킴
    for i in range(lower_x,r-1):
        tmp_board[i+1][c-1]=board[i][c-1]
        check[i+1][c-1]=True
        check[i][c-1]=True


    # 2. 아래공기청정기 바람 왼쪽으로
    for i in range(c-1,-1,-1):
        if i >0:
            tmp_board[r-1][i-1] = board[r-1][i]
            check[r-1][i-1]=True
            check[r-1][i]=True

    # 2. 아래공기청정기 바람 위로
    for i in range(r-1,lower_x+1,-1):
        tmp_board[i-1][0]=board[i][0]
        check[i-1][0]=True
        check[i][0]=True


    for i in range(r):
        for j in range(c):
            if check[i][j]:
                board[i][j]=tmp_board[i][j]





def diffusion():
    global board,r,c,queue

    tmp_board=copy.deepcopy(board)

    while queue:
          cur_x,cur_y=queue.popleft()
          change_map=[]
          cnt=0
          cost=tmp_board[cur_x][cur_y]//5
          for i in range(4):
              nx=dx[i]+cur_x
              ny=dy[i]+cur_y
              if nx < 0 or ny < 0 or nx >= r or ny >= c: continue
              if board[nx][ny] != -1:  # 미세먼지면
                 change_map.append([nx, ny])
                 cnt += 1

          while change_map:
                c_x, c_y = change_map.pop(0)
                board[c_x][c_y] += cost  # 증가시킴

          board[cur_x][cur_y] = board[cur_x][cur_y] - (cost * cnt)



r,c,t=map(int,input().split())
board=[0]*r
for i in range(r):board[i]=list(map(int,input().split()))

air_clear=[]


while t!=0:
    queue = deque()
    for i in range(r):
        for j in range(c):
            if board[i][j] == -1:  # 공기청정기면
                air_clear.append([i, j])

            elif board[i][j] != -1 and board[i][j] != 0:
                queue.append([i, j])
    diffusion()
    air_move()
    t-=1

answer=0

for i in range(r):
    for j in range(c):
        if board[i][j]>=1:
            answer+=board[i][j]

print(answer)