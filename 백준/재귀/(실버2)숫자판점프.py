from collections import deque
import sys
sys.setrecursionlimit(111111)
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(x,y,tmp):
    global number_list,answer_list

    if len(tmp)==6:
        answer_list.add(tmp)
        return

    for i in range(4):
        da=dx[i]+x
        db=dy[i]+y
        if da<0 or db<0 or da>=5 or db>=5:continue
        #이전에 방문했던것도 방문이 가능하므로 체크배열 사용 x
        dfs(da,db,tmp+str(number_list[da][db]))





answer_list=set()
number_list=[0]*5
visit=[False]*5
answer=0
for i in range(5):
    number_list[i]=list(map(int,input().split()))
    visit[i]=[False]*5


dfs(0,0,"")

for i in range(5):
    for j in range(5):
        dfs(i,j,"") ##모든위치에서 dfs돌려서 만들수있는숫자를 구함

print(len(answer_list))
