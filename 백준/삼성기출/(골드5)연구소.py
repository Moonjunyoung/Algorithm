import sys
import copy
from collections import deque
sys.setrecursionlimit(10000)

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs():
    global view,n,m,answer
    copy_array= [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            copy_array[i][j] = view[i][j]

    queue=deque()

    for i in range(n):
        for j in range(m):
            if copy_array[i][j]==2:
                queue.append([i,j])

    while queue:
          cur_x,cur_y=queue.popleft()
          for i in range(4):
              da=cur_x+dx[i]
              db=cur_y+dy[i]
              if 0<=da and 0<=db and da<n and db<m:
                if copy_array[da][db]==0:
                    copy_array[da][db]=2
                    queue.append([da,db])


    cnt = 0
    for i in range(n):
        for j in range(m):
            if copy_array[i][j]==0:
                cnt += 1

    answer = max(cnt, answer)
    return




def dfs(cnt):
    global visited,view,n,m,answer

    if cnt==3: ## bfs를돌려서 안전영역을 확보함
        bfs()
        return


    for i in range(n):
        for j in range(m):
            if view[i][j]==0: ##빈공간인경우
                view[i][j]=1 #벽을 세우고
                dfs(cnt+1)
                view[i][j]=0


    return

n,m=map(int,input().split())
view=[0]*n
answer=0
# 1. 맵 입력 받음
for i in range(n):
    view[i]=list(map(int,input().split()))


dfs(0)
print(answer)