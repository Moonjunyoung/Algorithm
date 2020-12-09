from collections import deque
import sys
sys.setrecursionlimit(111111)


def init():
    global dist,check,n
    for i in range(n):
        for j in range(n):
            dist[i][j]=0
            check[i][j]=False


def find_number(number):
    global board,n
    for i in range(n):
        for j in range(n):
            if board[i][j]==number:
                return (i,j)




dx=[0,0,1,-1]
dy=[1,-1,0,0]

n=int(input())
board=[0]*n
dist=[0]*n
check=[False]*n
for i in range(n):
    board[i]=list(map(int,input().split()))
    dist[i]=[0]*n
    check[i]=[False]*n


start_x=0
start_y=0


number=1
cost=0
while True:
    if number>pow(n,2):break
    queue = deque()
    queue.append((start_x, start_y))  ##시작점
    init()
    while queue:  ##모든 지점에 대한 최단거리를구함
        cur_x,cur_y=queue.popleft()
        check[cur_x][cur_y]=True
        for i in range(4):
            da=(cur_x+dx[i])%n
            db=(cur_y+dy[i])%n

            if check[da][db]==False:
               check[da][db]=True
               dist[da][db]=dist[cur_x][cur_y]+1
               queue.append([da,db])


    tmp_x,tmp_y=find_number(number)
    cost+=dist[tmp_x][tmp_y]+1 ##해당거리까지의 비용갱신
    start_x=tmp_x ##다음시작점
    start_y=tmp_y ## 다음시작점
    number+=1



print(cost)