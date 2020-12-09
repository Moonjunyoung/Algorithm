from collections import deque
import sys
sys.setrecursionlimit(111111)

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def check_right():
    global n,m,cold_mountain
    sum=0
    for i in range(n):
        for j in range(m):
            sum+=cold_mountain[i][j]

    if sum==0:
        return True
    else:
        return False

def init():
    global visit,n,m
    for i in range(n):
        for j in range(m):
            visit[i][j]=False

def bfs(x,y):
    global n,m,cold_mountain,visit,dist
    queue=deque()
    queue.append((x,y))
    visit[x][y]=True
    while queue:
         cur_x,cur_y=queue.popleft()
         for i in range(4):
             da=dx[i]+cur_x
             db=dy[i]+cur_y
             if da<0 or db<0 or da>=n or db>=m:continue
             if cold_mountain[da][db]==0 and visit[da][db]==False:
                visit[da][db]=True
                dist[da][db]=dist[cur_x][cur_y]+1
             elif cold_mountain[da][db]!=0 and visit[da][db]==False:
                  visit[da][db]=True
                  queue.append((da,db))
    return



def find_answer(x,y):
    global cold_mountain,visit
    visit[x][y]=True
    for i in range(4):
        da = dx[i] + x
        db = dy[i] + y
        if da < 0 or db < 0 or da >= n or db >= m: continue
        if cold_mountain[da][db] != 0 and visit[da][db] == False:
           find_answer(da,db)


def remove_mountain():
    global cold_mountain,dist,n,m
    for i in range(n):
        for j in range(m):
            if cold_mountain[i][j]!=0:
                for z in range(4):
                    da = dx[z] + i
                    db = dy[z] + j
                    if da < 0 or db < 0 or da >= n or db >= m: continue
                    if cold_mountain[da][db]==0:
                       cold_mountain[i][j]-=dist[da][db]
                       if cold_mountain[i][j]<0:
                          cold_mountain[i][j]=0



n,m=map(int,input().split())
cold_mountain=[]
visit=[False]*n
dist=[0]*n

for i in range(n):
    cold_mountain.append(list(map(int,input().split())))
    visit[i]=[False]*m
    dist[i]=[0]*m

answer=0

while True:
    init()
    sum = 0
    for i in range(n):
        for j in range(m):
            if visit[i][j]==False and cold_mountain[i][j]!=0:
                bfs(i,j)
                ## 1. bfs를 돌려서 주변좌표를 통해 다음번에 빙산이 얼마나 녹는지 확인


    remove_mountain()  # 2.해당 위치의 빙산이 녹는것을 계산함
    cnt=0
    init()
    for i in range(n): # 3.연결된 빙산을 확인함 
        for j in range(m):
            if visit[i][j]==False and cold_mountain[i][j]!=0:
                find_answer(i,j)
                cnt+=1

    answer+=1 

    if cnt>=2: # 4.1 연결된 빙산이 두개이상인경우 정답
       break

    if check_right()==True: ## 4.2  빙산이 모두 다녹았을경우 정지시킴
       answer=0
       break



print(answer)