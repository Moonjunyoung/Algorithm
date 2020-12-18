from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]
answer_number="123456780"
puzzle=[0]*3
current_number=""
#1. 입력 받기
for i in range(3):puzzle[i]=list(map(str,input().split()))
for i in range(3):
    for j in range(3):
        current_number+=puzzle[i][j]

visited=dict() ## 방문여부를 체크하는 변수
queue=deque()
visited[current_number]=0 #방문 여부 체크
queue.append(current_number)

while queue:
       cur_num=queue.popleft()
       cur_num=str(cur_num)
       tmp=cur_num.find('0') # 0을 기준으로 상하좌우를 바꿀수있음 0의 위치를 찾는다.
       cur_x=tmp//3
       cur_y=tmp%3
       # 1차원 좌표를 2차원으로 변동

       for i in range(4): #2차원 좌표로 상하좌우를 찾는다.
           da=cur_x+dx[i]
           db=cur_y+dy[i]

           if da<0 or db<0 or da>=3 or db>=3:continue
           # 스왑 시키기위함
           tmp_number=list(cur_num)
           tmp_number[3*da+db],tmp_number[cur_x*3+cur_y]=cur_num[cur_x*3+cur_y],tmp_number[3*da+db]
           swap_number="".join(tmp_number)
           if swap_number not in visited:#미방문이면
               visited[swap_number]=0 #방문
               visited[swap_number]=visited[cur_num]+1 #가중치갱신
               queue.append(swap_number)


if answer_number not in visited:#방문한적이없으면
    print(-1)
else:
    print(visited[answer_number])