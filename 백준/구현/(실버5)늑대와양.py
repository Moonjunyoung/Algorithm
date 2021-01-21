from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def set_ultari(cur_x,cur_y):
    global queue,r,c,board

    for i in range(4):
        nx=dx[i]+cur_x
        ny=dy[i]+cur_y

        if nx<0 or ny<0 or nx>=r or ny>=c:continue
        if board[nx][ny]=='W':
            return True
        elif board[nx][ny]=='.':
            board[nx][ny]='D'




r,c=map(int,input().split())
board=[0]*r
for i in range(r):
    board[i]=list(map(str,input()))

for i in range(r):
    for j in range(c):
        if board[i][j]=='S':
            if set_ultari(i,j):
                print(0)
                exit(0)

print(1)
for i in range(r):
    for j in range(c):
        print(board[i][j],end='')
    print()


from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def set_ultari(cur_x,cur_y):
    global queue,r,c,board

    for i in range(4):
        nx=dx[i]+cur_x
        ny=dy[i]+cur_y

        if nx<0 or ny<0 or nx>=r or ny>=c:continue
        # 1. 주변에 늑대가있으면 울타리를 설치 못함
        if board[nx][ny]=='W':
            return True

        elif board[nx][ny]=='.':
            board[nx][ny]='D'




r,c=map(int,input().split())
board=[0]*r
for i in range(r):
    board[i]=list(map(str,input()))

for i in range(r):
    for j in range(c):
        if board[i][j]=='S':
            if set_ultari(i,j):
                print(0)
                exit(0)

print(1)
for i in range(r):
    for j in range(c):
        print(board[i][j],end='')
    print()


