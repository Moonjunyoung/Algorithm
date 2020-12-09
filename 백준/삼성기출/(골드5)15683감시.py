import copy
def copy_board(src):
    dst=copy.deepcopy(src)
    return dst

def find_answer():
    global board,n,m,answer
    cnt=0
    for i in range(n):
        for j in range(m):
            if board[i][j]==0:
                cnt+=1

    answer=min(answer,cnt)

def update(direction,cctv): ##해당 씨씨티비의 방향값을 통해 맵을 업데이트 해줌
    global board,n,m

    cctv_x=cctv[0]
    cctv_y=cctv[1]

    direction=direction%4

    if direction==0: ##동쪽방향 y값만 바뀜
        for i in range(cctv_y+1,m):
            if board[cctv_x][i]==6: # 벽이면 탐색불가
                break
            board[cctv_x][i]=-1 ##벽이아닌경우 -1로 바꿔줌 탐색가능

    elif direction==1: ##남쪽방향 x값만바뀜
        for i in range(cctv_x+1,n):
            if board[i][cctv_y] == 6:  # 벽이면 탐색불가
                break
            board[i][cctv_y] = -1  ##벽이아닌경우 -1로 바꿔줌 탐색가능

    elif direction==2: #서쪽 방향 y값만 바뀜
        for i in range(cctv_y-1,-1,-1):
            if board[cctv_x][i]==6: # 벽이면 탐색불가
                break
            board[cctv_x][i]=-1 ##벽이아닌경우 -1로 바꿔줌 탐색가능

    elif direction==3: ##북쪽방향 x값만바뀜
        for i in range(cctv_x-1,-1,-1):
            if board[i][cctv_y] == 6:  # 벽이면 탐색불가
                break
            board[i][cctv_y] = -1  ##벽이아닌경우 -1로 바꿔줌 탐색가능







def dfs(cctv_idx):
    global cctv_list,cctv_rotation,board

    if len(cctv_list)==cctv_idx: ## 경우 탐색이 완료되면
       find_answer() ## 사각지대의 크기를 구함
       return

    cctv_type=cctv_list[cctv_idx][2]-1
    cctv_type_rotation=cctv_rotation[cctv_type]
    tmp_board=copy_board(board) ## 현재 상태의 board를 저장 update후 바뀌므로 모든경우를 돌기위해서 이전값을 저장해놔야함

    for i in range(cctv_type_rotation): ## 해당 cctv idx의 cctv타입에 대한 회전수 (즉 이 회전수는 해당 cctv가 볼수있는 경우의수)
        if cctv_type==0: ## 씨씨티비가 1번 인경우
            update(i,cctv_list[cctv_idx])  # 한방향만

        if cctv_type == 1:  ##씨씨티비가 2번인경우 <-> 위아래
            update(i,cctv_list[cctv_idx])
            update(i+2, cctv_list[cctv_idx])

        if cctv_type == 2: # 씨씨티비가 3번인경우
            update(i, cctv_list[cctv_idx])
            update(i+1, cctv_list[cctv_idx])

        if cctv_type==3: ##씨씨티비가 4번인경우
            update(i, cctv_list[cctv_idx])
            update(i + 2, cctv_list[cctv_idx])
            update(i + 3, cctv_list[cctv_idx])

        if cctv_type==4: ##씨씨티비가 5번인경우
            update(i, cctv_list[cctv_idx])
            update(i + 1, cctv_list[cctv_idx])
            update(i + 2, cctv_list[cctv_idx])
            update(i + 3, cctv_list[cctv_idx])


        dfs(cctv_idx+1)
        board=copy_board(tmp_board) ##탐색이 끝난뒤 이전보드로..






n, m = map(int, input().split())
board=[0]*n
cctv_rotation=[4,2,4,4,1]
cctv_list=[]
answer=99999999
for i in range(n):board[i]=list(map(int,input().split()))

for i in range(n):
    for j in range(m):
        if board[i][j]!=0 and board[i][j]!=6: ##벽과 cctv가 아닌경우
            cctv_list.append((i,j,board[i][j])) # 0에는 cctv x좌표 , 1에는 cctv y좌표 , 2 에는 cctv 타입을 넣어줌

dfs(0)

print(answer)