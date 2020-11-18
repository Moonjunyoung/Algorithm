def restore_board(board,chase_board):
    global n,m
    for i in range(n):
        for j in range(m):
            board[i][j]=chase_board[i][j]

    return board

def white_black_check_chaseboard(board,x,y,white_black_board):
    cnt=0
    for i in range(x,x+8):
        for j in range(y,y+8): ## white_black board 사이즈는 8*8인데 board값은 더크므로 인덱스가 넘칠경우 나눠줌으로 해결
            if white_black_board[i%8][j%8]!=board[i][j]:
               cnt+=1

    return cnt


def black_white_check_chaseboard(board,x,y,black_white_board):
    cnt=0
    for i in range(x,x+8):
        for j in range(y,y+8):
            if black_white_board[i%8][j%8]!=board[i][j]:
               cnt+=1

    return cnt



white_black=[[0]]*8
black_white=[[0]]*8
for i in range(8):
    white_black[i]=[0]*8
    black_white[i]=[0]*8

white_black=[['W','B','W','B','W','B','W','B'],
              ['B','W','B','W','B','W','B','W'],
              ['W','B','W','B','W','B','W','B'],
              ['B','W','B','W','B','W','B','W'],
             ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
             ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
             ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
             ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
             ]
black_white=[['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
             ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
             ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
             ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
             ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
             ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
             ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
             ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
             ]

# 이문제에서 해매가지고 헛질한점 => 8x8영역당 최소로 바꿔야하는 블록을 구하는건데 전체를 다바꿧을경우로 잘못함

 
#1. black_white 와 white_black으로 이루어진 체스판을 만듬 이것을 가지고 들어오는 값과 비교

n,m=map(int,input().split())
chase_board=[[0]]*n
tmp_chaseboard=[[0]]*n
for i in range(n):tmp_chaseboard[i]=[[0]]*m

for i in range(n):chase_board[i]=list(map(str,input()))
tmp_chaseboard=restore_board(tmp_chaseboard,chase_board) ## 2. 원본 체스판을 임시로 저장
answer=999999999

# white black 판 과 비교
for i in range(n):
    for j in range(m):
        cnt = 0
        if i+8<=n and j+8<=m: ## 3.i,j 위치부터 i+8 j+8위치의 바꿔야할 블록을 계산함 해당 위치당 하나하나 계산하면서 비교
            cnt+=white_black_check_chaseboard(tmp_chaseboard,i,j,white_black) 
            answer=min(cnt,answer)


#black white와 비교
tmp_chaseboard=restore_board(tmp_chaseboard,chase_board) #예전 체스판으로 원상복귀

for i in range(n):
    for j in range(m):
        cnt = 0
        if i+8<=n and j+8<=m:
            cnt+=black_white_check_chaseboard(tmp_chaseboard,i,j,black_white)
            answer=min(cnt,answer)

print(answer)


