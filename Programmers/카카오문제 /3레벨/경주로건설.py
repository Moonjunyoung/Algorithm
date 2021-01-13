from collections import deque

def bfs(board,row,col,dir):
    queue=deque()
    # 우=0 좌=1 하=2 상=3
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    dist=[-1]*row

    for i in range(row):dist[i]=[-1]*col
    queue.append([0,0,dir,0])
    dist[0][0]=0
    while queue:
          cur_x,cur_y,cur_dir,cost=queue.popleft()
          if cur_x==row-1 and cur_y==col-1:
              continue # 3. 컨티뉴를 안해주면 최소비용이 안나온다 break를 해줘도 안됨 무조건 큐가끝나야 다돈거

          for i in range(4):
              nx=cur_x+dx[i]
              ny=cur_y+dy[i]
              if nx<0 or ny<0 or nx>=row or ny>=col:continue
              if board[nx][ny]==1:continue
              next_cost=0
              if i==cur_dir: # 1. 방향이같으면 비용+100추가 다르면 600
                  next_cost=cost+100
              else:
                  next_cost=cost+600

              # 2. 방문을 안하거나 , 방문을했는데 현재 cost보다 작은경우 다시 갱신시켜줌 <-이부분이핵심
              if dist[nx][ny]==-1 or dist[nx][ny]>next_cost:
                  dist[nx][ny]=next_cost
                  queue.append([nx,ny,i,next_cost])


    return dist[row-1][col-1]


def solution(board):
    answer = 0
    a=bfs(board,len(board),len(board[0]),0) # 0,0인지점에서 방향이 오른쪽으로보고있을떄
    b=bfs(board,len(board),len(board[0]),2) # 0,0인지점에서 방향이 아래로 보고잇을떄

    answer=min(a,b)
    return answer
