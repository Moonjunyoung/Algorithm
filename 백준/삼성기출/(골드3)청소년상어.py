import copy
t=0
fish_board=[0]*4
fish_direction=[0]*4
# 방향
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]

def fish_find(cnt): # 1. 물고기를 찾는다.
    global fish_board,fish_direction
    for i in range(4):
        for j in range(4):
            if cnt==fish_board[i][j]:
                return [i,j]

    return [-1,-1]


def fish_move(c_x,c_y): #  2.물고기를 이동시킨다
    global fish_board,fish_direction
    cur_x,cur_y=c_x,c_y
    fish_cur=fish_direction[cur_x][cur_y]


    for _ in range(8):
        next_x = cur_x + dx[fish_cur]
        next_y = cur_y + dy[fish_cur]

        if next_x>=0 and next_y>=0 and next_x<4 and next_y<4 and fish_board[next_x][next_y]>=-1:
            fish_name = fish_board[next_x][next_y]  # 해당 물고기의 다음좌표확인
            fish_dir = fish_direction[next_x][next_y]

            if fish_name==-1: #빈칸인경우
                fish_board[next_x][next_y]=fish_board[cur_x][cur_y]
                fish_direction[next_x][next_y]=fish_direction[cur_x][cur_y]
                fish_board[cur_x][cur_y]=-1
                fish_direction[cur_x][cur_y]=-1

            else:
                fish_board[next_x][next_y]=fish_board[cur_x][cur_y]
                fish_direction[next_x][next_y]=fish_direction[cur_x][cur_y]
                fish_board[cur_x][cur_y]=fish_name
                fish_direction[cur_x][cur_y]=fish_dir

            break

        else: # 이동이 불가능한경우
             fish_cur=(fish_cur+1)
             if fish_cur==8:fish_cur=0

             fish_direction[cur_x][cur_y]=fish_cur #현재 물고기의 방향을 바꿔줌


def fish_move_main(): # 3 물고기
    for i in range(1,17):
        f_x,f_y=fish_find(i)
        if f_x==-1 and f_y==-1:continue # 물고기가 존재 x
        fish_move(f_x,f_y)


def Game():
    # 1. 상어는 0,0에있는 물고기를 먹는다 .
    shark_dir = fish_direction[0][0]
    tmp=fish_board[0][0]
    fish_board[0][0] = -9999
    fish_direction[0][0]=-1
    Shark_dfs(0,0,shark_dir,tmp)


def Shark_dfs(cur_x,cur_y,dir,sum):
    global fish_board,fish_direction,answer


    fish_move_main()  # 1. 물고기 이동진행

    tmp_board = copy.deepcopy(fish_board)
    tmp_board2 = copy.deepcopy(fish_direction)


    flag=find_fish(cur_x,cur_y,dir) # 2. 현재 상어가 먹을수있는 물고기를 찾는다.
    if len(flag)==0:
        answer=max(sum,answer)
        return

    else:
        for i in flag: # 3.상어가 먹을수있는 물고기 리스트들가지고 백트래킹 돌림
            fish_x,fish_y,fish_dir=i
            fish_board[cur_x][cur_y]=-1 #상어의 현재 위치 빈칸
            fish_direction[cur_x][cur_y]=-1 #상어의 현재방향 빈칸 으로
            tmp=fish_board[fish_x][fish_y]
            fish_board[fish_x][fish_y]=-9999 #상어가 해당 물고기 먹으러 이동

            Shark_dfs(fish_x,fish_y,fish_dir,sum+tmp) # 해당 물고기를 먹으러간다.
            fish_board=copy.deepcopy(tmp_board)
            fish_direction=copy.deepcopy(tmp_board2)

    return

# 현재 위치의 상어로부터 먹을수있는 물고기들을 찾는다 .
def find_fish(cur_x,cur_y,dir):
    global fish_board,fish_direction
    fish_list=[]
    while True:
          next_x=dx[dir]+cur_x
          next_y=dy[dir]+cur_y
          if next_x<0 or next_y<0 or next_x>=4 or next_y>=4:break

          else:
               if fish_board[next_x][next_y]>0:
                  fish_list.append([next_x,next_y,fish_direction[next_x][next_y]])

          cur_x = next_x
          cur_y = next_y

    return fish_list

while t!=4:
      tmp=list(map(int,input().split()))
      a=[]
      b=[]
      for i in range(len(tmp)):
          if i%2==0:
              a.append(tmp[i])
          else:
              b.append(tmp[i]-1)

      fish_board[t]=a
      fish_direction[t]=b

      t+=1

answer=0
Game()
print(answer)