from collections import deque
import itertools
import copy

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def ctrl_move(c_x,c_y,board,dir):
    next_x,next_y=0,0
    if dir==0: # 1. 오른쪽
       for i in range(c_y,4):
           next_x, next_y = c_x, i
           if board[c_x][i]!=0: #카드가 존재한다
              break

    elif dir==1: # 2. 왼쪽
         for i in range(c_y,-1,-1):
             next_x, next_y = c_x, i
             if board[c_x][i] != 0:  # 카드가 존재한다
                break

    elif dir==2: # 3. 아래쪽
         for i in range(c_x,4):
             next_x, next_y = i, c_y
             if board[i][c_y]!=0:
                break

    elif dir==3:  # 4.위쪽
         for i in range(c_x,-1,-1):
             next_x, next_y = i, c_y
             if board[i][c_y]!=0:
                break

    return [next_x,next_y]


def bfs(start_x,start_y,end_x,end_y,board):
    queue=deque()
    dist=[-1]*4
    for i in range(4):dist[i]=[-1]*4
    queue.append([start_x,start_y])
    dist[start_x][start_y]=0


    while queue:
          cur_x,cur_y=queue.popleft()
          for i in range(4):
              nx=dx[i]+cur_x
              ny=dy[i]+cur_y
              if nx<0 or ny<0 or nx>=4 or ny>=4:continue

              # 1. 그냥 이동
              if dist[nx][ny]==-1 or dist[cur_x][cur_y]+1<dist[nx][ny]:
                 dist[nx][ny]=dist[cur_x][cur_y]+1
                 queue.append([nx,ny])

              # 2. 컨트롤 누르고 이동
              ctrl_x,ctrl_y=ctrl_move(nx, ny, board, i)
              if dist[ctrl_x][ctrl_y]==-1 or dist[cur_x][cur_y]+1<dist[ctrl_x][ctrl_y]:
                 dist[ctrl_x][ctrl_y]=dist[cur_x][cur_y]+1
                 queue.append([ctrl_x,ctrl_y])

    return dist[end_x][end_y]


def solution(board, r, c):
    card_list=dict()
    card_num=set()
    for i in range(1,7):
        if i not in card_list:
            card_list[i]=[]


    # 1. 카드인 경우를 뽑음 순열을 돌리기위해
    for i in range(4):
        for j in range(4):
            if board[i][j]!=0:
                card_num.add(board[i][j])
                card_list[board[i][j]].append([i,j])


    permute=list(itertools.permutations(card_num))
    answer_list=[]

    # 2. 카드를 뽑을 수있는 경우에대해 완전탐색을 돌림 (itertools로)
    for i in permute:
        s=0
        card_cursor = []
        card_cursor.append([r, c])
        tmp_board=copy.deepcopy(board)

        # 2.1 해당 순열
        for j in i:
            card_1=card_list[j][0]
            card_2=card_list[j][1]

            # 3. 현재 카드 커서의위치에서 해당카드까지 가까운것을 선정
            while card_cursor:
                  z=card_cursor.pop(0)
                  ta=bfs(z[0],z[1],card_1[0],card_1[1],tmp_board)+bfs(card_1[0],card_1[1],card_2[0],card_2[1],tmp_board)+2
                  tb=bfs(z[0], z[1], card_2[0], card_2[1], tmp_board)+bfs(card_2[0],card_2[1],card_1[0],card_1[1],tmp_board)+2


            # 4. 가까운것을 선정하는데 이떄 가까운것의 위치를 넣음
            if ta < tb:
                s += ta
                card_cursor.append([card_2[0], card_2[1]])
            else:
                s += tb
                card_cursor.append([card_1[0], card_1[1]])


            tmp_board[card_1[0]][card_1[1]]=0
            tmp_board[card_2[0]][card_2[1]] = 0

        answer_list.append(s)

    answer_list.sort()
    return answer_list[0]

solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1,0)