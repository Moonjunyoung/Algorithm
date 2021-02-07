import itertools
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def check_cost(selcted_flower):
    global n,board
    check = [0] * n
    for i in range(n): check[i] = [False]*n
    cnt=0

    for i in selcted_flower:
        f_x,f_y=i
        check[f_x][f_y]=True
        cnt+=board[f_x][f_y]
        for j in range(4):
            nx=f_x+dx[j]
            ny=f_y+dy[j]
            if nx<0 or ny<0 or nx>=n or ny>=n or check[nx][ny]==True:
                return 10000000000

            check[nx][ny]=True
            cnt+=board[nx][ny]

    return cnt

n=int(input())
board=[0]*n
for i in range(n):board[i]=list(map(int,input().split()))

flowers=[]
for i in range(1,n-1):
    for j in range(1,n-1):
        flowers.append([i,j])


flowers_combi=list(itertools.combinations(flowers,3))
answer=10000000000

for i in flowers_combi:
    answer=min(answer,check_cost(i))



print(answer)