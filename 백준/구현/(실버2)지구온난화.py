r,c=map(int,input().split())
board=[0]*r

for i in range(r):board[i]=list(map(str,input()))

change_list = []

for i in range(r):
    for j in range(c):
        cur_x,cur_y=i,j
        cnt=0
        if board[cur_x][cur_y]=='.':continue #현재 위치가 바다면 그냥넘김
        if cur_x-1<0: #맵밖을 벗어나면 (상)
            cnt+=1
        else:
            if board[cur_x-1][cur_y]=='.':
                cnt+=1

        if cur_x+1>=r: #맵밖을 벗어나면 (하)
            cnt+=1
        else:
            if board[cur_x+1][cur_y]=='.':
                cnt+=1

        if cur_y+1>=c: #맵밖을 벗어나면 (우)
            cnt+=1
        else:
            if board[cur_x][cur_y+1]=='.':
                cnt+=1

        if cur_y-1<0: #맵밖을 벗어나면 (좌)
            cnt+=1
        else:
            if board[cur_x][cur_y-1]=='.':
                cnt+=1

        if cnt>=3:
            change_list.append([cur_x,cur_y])


# 1. 바다로 바꿔 준다.
while change_list:
      c_x,c_y=change_list.pop()
      board[c_x][c_y]='.'


change_list=[]
for i in range(r):
    for j in range(c):
        if board[i][j]=='X':
            change_list.append([i,j])


# X들중에서 y열이 가장 작은것 , X들중에서 y열이 가장 큰것 ,
# X들중에서 x열이 가장큰것 X들중에서

change_list=sorted(change_list,key=lambda x:-x[0]) # end _x
start_x=change_list[len(change_list)-1][0]
end_x=change_list[0][0]

change_list=sorted(change_list,key=lambda x:(-x[1])) # end_y
start_y=change_list[len(change_list)-1][1]
end_y=change_list[0][1]


for i in range(start_x,end_x+1):
    for j in range(start_y,end_y+1):
        print(board[i][j],end='')
    print()



