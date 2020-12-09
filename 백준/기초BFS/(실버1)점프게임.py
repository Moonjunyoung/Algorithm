from collections import deque
n,k=map(int,input().split())
left_board=list(map(int,input()))
right_board=list(map(int,input()))

queue=deque()
queue.append([0,0,'L']) #현재위치 time ,맵위치
left_board_check=[False]*n
right_board_check=[False]*n
left_board_check[0]=True


while queue:
      cur_x,cur_time,cur_map=queue.popleft()
      if cur_x+1==n or cur_x+k>=n or cur_x-1==n: ## 칸을 넘을수 있으면 정답
          print(1)
          exit(0)

      if cur_map=='L': ##현재맵 위치가 L
            if cur_x+1<n and left_board_check[cur_x+1]==False and left_board[cur_x+1]==1:
                queue.append([cur_x+1,cur_time+1,'L'])
                left_board_check[cur_x+1]=True
            if cur_x-1>=0 and left_board_check[cur_x-1]==False and left_board[cur_x-1]==1:
               queue.append([cur_x-1,cur_time+1,'L'])
               left_board_check[cur_x-1]=True
            if cur_x+k<n and right_board_check[cur_x+k]==False and right_board[cur_x+k]==1:
                queue.append([cur_x+k,cur_time+1,'R'])
                right_board_check[cur_x+k]=True

      elif cur_map=='R': ##현재 맵 위치가 R
          if cur_x + 1 < n and right_board_check[cur_x + 1] == False and right_board[cur_x + 1] == 1:
              queue.append([cur_x + 1, cur_time + 1, 'R'])
              right_board_check[cur_x + 1] = True

          if cur_x - 1 >= 0 and right_board_check[cur_x - 1] == False and right_board[cur_x - 1] == 1:
              queue.append([cur_x - 1, cur_time + 1, 'R'])
              right_board_check[cur_x - 1] = True
          if cur_x + k < n and left_board_check[cur_x + k] == False and left_board[cur_x + k] == 1:
              queue.append([cur_x + k, cur_time + 1, 'L'])
              left_board_check[cur_x+k]=True


      # 1초시간 뒤 해당칸은 방문을 못하게됨
      left_board[cur_time]=0
      right_board[cur_time]=0


print(0)


