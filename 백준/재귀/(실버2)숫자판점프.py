board=[0]*5
answer_list=set()
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(depth,number,cur_x,cur_y):
    global board,answer_list
    if depth==6:
        answer_list.add(number)
        return



    for i in range(4):
        da=cur_x+dx[i]
        db=cur_y+dy[i]
        if da<0 or db<0 or da>=5 or db>=5:continue
        dfs(depth+1,number+str(board[da][db]),da,db)



 # 1.한번 거친곳은 다시 방문해도되므로 visit 배열 필요 x
 
for i in range(5):
    board[i]=list(map(int,input().split()))


for i in range(5):
    for j in range(5):
        dfs(0,"",i,j)


print(len(answer_list))