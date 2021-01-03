# 시간 초과 발생하는 코드 c++로 하면 통과하는 로직
from collections import deque
dx=[0,1,1]
dy=[1,0,1]
def bfs():
    global n,answer
    queue=deque()
    queue.append([0,1,0])
    #처음에 0,1 위치의 동쪽방향

    while queue:
          cur_x,cur_y,dir=queue.popleft()
          if cur_x==n-1 and cur_y==n-1:
              answer+=1
              continue

          if dir==0:##동쪽 방향일떄
              da=cur_x+dx[0]
              db=cur_y+dy[0]
              if da >= 0 and db >= 0 and da < n and db < n and board[da][db]!=1:
                 queue.append([da,db,0])

              # 파이프가 회전 하는 경우 (동쪽일떄는 대각선으로 회전가능)
              da=cur_x+dx[2]
              db=cur_y+dy[2]
              if da < 0 or db < 0 or da >= n or db >= n :continue
              if board[da][db]!=1 and board[cur_x][cur_y+1]!=1 and board[cur_x+1][cur_y]!=1:
                 queue.append([da,db,2])

          elif dir==1: #남쪽 방향일떄
               da=cur_x+dx[1]
               db=cur_y+dy[1]
               if da >=0 and db >=0 and da < n and db < n and board[da][db] != 1:
                   queue.append([da, db, 1])

               #남쪽 방향일떄 파이프가 대각선 방향으로 회전
               da = cur_x + dx[2]
               db = cur_y + dy[2]
               if da < 0 or db < 0 or da >= n or db >= n: continue
               if board[da][db] != 1 and board[cur_x][cur_y + 1] != 1 and board[cur_x + 1][cur_y] != 1:
                   queue.append([da, db, 2])

          elif dir==2: #대각선 방향일떄
               da=cur_x+dx[2]
               db=cur_y+dy[2]
               if da >= 0 and db > 0 and da < n and db < n:
                  if board[da][db] != 1 and board[cur_x][cur_y + 1] != 1 and board[cur_x + 1][cur_y] != 1:
                     queue.append([da, db, 2])

               #대각선 방향일떄 동쪽과 남쪽으로 회전가능
               for i in range(2):
                   da=cur_x+dx[i]
                   db=cur_y+dy[i]
                   if da<0 or db<0 or da>=n or db>=n:continue
                   if board[da][db]!=1:
                       queue.append([da,db,i])




n=int(input())
board=[0]*n
answer=0
for i in range(n):
    board[i]=list(map(int,input().split()))

bfs()
print(answer)

