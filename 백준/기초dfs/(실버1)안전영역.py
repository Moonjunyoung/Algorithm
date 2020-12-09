import sys
sys.setrecursionlimit(111111)


dx=[0,0,1,-1]
dy=[1,-1,0,0]

def init():
    global n,visit
    for i in range(n):
        for j in range(n):
            visit[i][j]=False

def dfs(x,y,number):
    global n,visit,cnt,map_list
    visit[x][y]=True
    for i in range(4):
        da=dx[i]+x
        db=dy[i]+y
        if da<0 or db<0 or da>=n or db>=n:continue
        if visit[da][db]==False and map_list[da][db]>number:
            dfs(da,db,number)



    return

n=int(input())
map_list=[]
visit=[0]*n
number=set()
for i in range(n):
    map_list.append(list(map(int,input().split())))
    visit[i]=[False]*n


for i in range(n):
    for j in range(n):
        number.add(map_list[i][j]) ## 물이 잠길수있는 높이를 다넣음


answer=0
for i in number: # 물이 잠길수있는 높이 하나하나 확인하면서 가장 많은 안전영역을 구하면됨
    cnt=0
    init()
    for j in range(n):
        for z in range(n):
            if map_list[j][z]>i and visit[j][z]==False: 
                dfs(j,z,i)
                cnt+=1

    answer=max(answer,cnt)


if answer==0: ## 물이 안잠긴곳이 발생할시 
    answer=1

print(answer)