from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]
answer_time=0


def find_shark():
    global n,fish_board
    for i in range(n):
        for j in range(n):
            if fish_board[i][j]==9:
                return [i,j]

def find_shack_eat(eat_pos):
    global n,shark_size,fish_board,shark_eat_fish,answer_time


    if len(eat_pos)==0: #더이상 먹을게 없으면
        print(answer_time)
        exit(0)

    eat_pos.sort(key= lambda x:(x[2],x[0],x[1])) #1. 거리우선  2.가장위값기준  3.가장왼쪽값기준
    eat_x=eat_pos[0][0]
    eat_y=eat_pos[0][1]
    answer_time+=eat_pos[0][2]
    fish_board[eat_x][eat_y]=9 ##현재 상어위치를 먹을상어위치로
    shark_eat_fish += 1 #먹은 물고기증가
    if shark_eat_fish == shark_size:  # 상어 진화
        shark_size += 1
        shark_eat_fish = 0


def bfs(shark_x,shark_y):
    global n,shark_size,fish_board
    queue=deque()
    dist=[0]*n
    visited=[False]*n
    for i in range(n):
        dist[i]=[0]*n
        visited[i]=[False]*n

    queue.append([shark_x,shark_y])
    dist[shark_x][shark_y]=0
    visited[shark_x][shark_y]=True
    fish_board[shark_x][shark_y]=0
    eat_pos=[]
    while queue:
        cur_x,cur_y=queue.popleft()
        for i in range(4):
            da=cur_x+dx[i]
            db=cur_y+dy[i]

            if da<0 or db<0 or da>=n or db>=n:continue
            if shark_size<fish_board[da][db]:continue
            if  visited[da][db]==False: #1. 자기보다 작거나 같은 놈만 지나갈수잇음
                visited[da][db]=True
                queue.append([da,db])
                dist[da][db]=dist[cur_x][cur_y]+1 #거리갱신
                distance=dist[da][db]
                if fish_board[da][db]!=0 and shark_size>fish_board[da][db]: #자기보다 작거나같은놈일경우 넣음
                    eat_pos.append([da, db, distance])

    find_shack_eat(eat_pos) #먹을수있는 먹이를 찾으러간다.






n=int(input())
fish_board=[0]*n
shark_eat_fish=0
shark_size=2
for i in range(n):
    fish_board[i]=list(map(int,input().split()))

while True:
      shark_x,shark_y=find_shark()
      bfs(shark_x,shark_y)