import copy
import itertools

def game_over(game_board):
    global board,n,m
    for i in range(n):
        for j in range(m):
            if game_board[i][j]==1:
                return True
    return False

def find_enemy(cur_x,cur_y,game_board):
    enemy_list=[]
    global n,m,d

    for i in range(n):
        for j in range(m):
            if game_board[i][j]==1:
                dist=abs(cur_x-i)+abs(cur_y-j) #적과의거리
                if dist<=d: # 사정거리안이면
                    enemy_list.append([i,j,dist])

    tmp=sorted(enemy_list,key=lambda x:(x[2],x[1])) # 1. 거리가 작고 2. 가장왼쪽에있는것 순으로 정렬
    if len(tmp)==0:
        return False
    else:
        return tmp[0]

def move_enemy(game_board):
    global n,m

    for i in range(m):
        if game_board[n-1][i]==1:
            game_board[n-1][i]=0

    for i in range(n-2,-1,-1):
        for j in range(m):
            if game_board[i][j]==1:
               game_board[i][j] = 0
               game_board[i+1][j]=1


def cattle_defense(game_board,archer_list):
    global n,m,answer_kill
    kill = 0
    while game_over(game_board): # 맵에 적이 없을떄까지 게임을 진행한다.
          enemy_list=[]

          # 1. 가장 가까운 적을 찾는다.
          for i in archer_list:
              flag=find_enemy(i[0],i[1],game_board)
              if flag==False:continue # 적이없는경우
              enemy_list.append(flag)

          # 2. 적을 제거한다.
          for i in enemy_list:
              e_x=i[0]
              e_y=i[1]
              if game_board[e_x][e_y]==1:
                 game_board[e_x][e_y]=0
                 kill+=1

          #3. 적을 이동시킨다.
          move_enemy(game_board)


    # 4. 정답갱신
    answer_kill=max(kill,answer_kill)
    return


n,m,d=map(int,input().split())
board=[0]*n
archer_pos_list=[]
answer_kill=0

# 1. 입력받기
for i in range(n):board[i]=list(map(int,input().split()))
for i in range(m):archer_pos_list.append([n,i])


# 2. 궁수 배치
archer_pos_list=list(itertools.combinations(archer_pos_list,3))
for i in archer_pos_list:
    cur_archer_list=[]
    game_board=copy.deepcopy(board)
    for j in i:cur_archer_list.append(j)
    # 3. 캐슬 디펜스 시작
    cattle_defense(game_board,cur_archer_list)



print(answer_kill)