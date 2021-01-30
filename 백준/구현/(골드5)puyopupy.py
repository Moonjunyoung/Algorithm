from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def change_map(tmp_board,column):
    global board
    tmp_board.reverse()
    for i in range(12):
        board[i][column]=tmp_board.pop(0)


def bomb():
    global board,r,c


    for i in range(c):
        tmp_list=[]
        for j in range(r):
            tmp_list.append(board[j][i])

        tmp_list.reverse()
        idx=0
        cnt=0
        while idx<12 and cnt<12:
              if tmp_list[idx]=='.':
                 tmp_list.append(tmp_list.pop(idx))
                 idx-=1
                 cnt+=1

              idx+=1


        change_map(tmp_list,i)



def bfs(x,y,color):
    global board,r,c
    visited=[False]*r
    for i in range(r):visited[i]=[False]*c
    queue=deque()
    queue.append([x,y,color])
    disappear_list=[[x,y]]
    visited[x][y]=True

    while queue:
          cur_x,cur_y,co=queue.popleft()
          for i in range(4):
              nx=dx[i]+cur_x
              ny=dy[i]+cur_y
              if nx<0 or ny<0 or nx>=r or ny>=c:continue
              if board[nx][ny]==co and visited[nx][ny]==False:
                  queue.append([nx,ny,co])
                  visited[nx][ny]=True
                  disappear_list.append([nx,ny])



    if len(disappear_list)>=4:
        while disappear_list:
            c_x, c_y = disappear_list.pop()
            board[c_x][c_y] = '.'
        return True

    else:
        return False



r=12
c=6
board=[0]*12
for i in range(12):board[i]=list(map(str,input()))

answer=0
while True:
      flag = False
      for i in range(r):
          for j in range(c):
              if board[i][j]!='.':
                  if bfs(i,j,board[i][j]): # 1. 터트릴수있는 그룹을 찾고 지운다.
                      flag=True


      # 2. 그룹이 제거되었으므로 밑으로 내린다 .
      if flag:
         bomb()
         answer+=1
      else:
          print(answer)
          break