import sys
sys.setrecursionlimit(111111)

dx=[0,0,1,-1]
dy=[1,-1,0,0]
def dfs(x,y,color):
    global check,n,colors
    check[x][y]=True

    for i in range(4):
        da=dx[i]+x
        db=dy[i]+y
        if da<0 or db<0 or da>=n or db>=n: continue
        if check[da][db]==False and colors[da][db]==color:
            dfs(da,db,color)


n=int(input())
colors=[0]*n
check=[False]*n
find_color=['R','G','B']
for i in range(n):
    colors[i]=list(map(str,input()))
    check[i]=[False]*n


answer_list={'R':0,'G':0,'B':0}
answer_list2={'R':0}


# 1. 정상인 사람의 볼수 있는 R,G,B를구함
for c in find_color:
    for i in range(n):
        for j in range(n):
            if check[i][j]==False and colors[i][j]==c:
                dfs(i,j,c)
                answer_list[c]+=1


check=[False]*n
for i in range(n):check[i]=[False]*n


# 2. 적록색약이 있는 사람의 R,G,B를 구함 적록색약은 R==G이므로 R이나 G둘중하나를 R로바꾸고 dfs탐색
for i in range(n):
    for j in range(n):
        if colors[i][j]=='G':
            colors[i][j]='R'


for i in range(n):
    for j in range(n):
        if check[i][j]==False and colors[i][j]=='R':
            dfs(i,j,'R')
            answer_list2['R']+=1



print(answer_list['R']+answer_list['G']+answer_list['B'],answer_list2['R']+answer_list['B'])
