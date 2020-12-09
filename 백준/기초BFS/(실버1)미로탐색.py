import collections

dx=[0,0,1,-1]
dy=[1,-1,0,0]

n,m=map(int,input().split())
miro=[]
check=[]
for i in range(n): ##row
    miro.append(list(map(int,input()))) ##col

for i in range(n):check.append([False]*m)


queue=collections.deque()

queue.append([0,0])## 1,1에서 출발

check[0][0]=True

while queue:
    cur_x,cur_y=queue.popleft()
    for i in range(4):
        da=dx[i]+cur_x
        db=dy[i]+cur_y

        if da<0 or da>=n or db<0 or db>=m or miro[da][db]==0:continue

        if check[da][db]==False: ##미방문일시
            check[da][db]=True
            queue.append([da,db])
            miro[da][db]=miro[cur_x][cur_y]+1 ##위치 갱신


print(miro[n-1][m-1])




