import collections

dx=[0,0,1,-1]
dy=[1,-1,0,0]

n,m=map(int,input().split())
picture=[]
check=[]
for i in range(n): ##row
    picture.append(list(map(int,input().split()))) ##col

for i in range(n):check.append([False]*m)


queue=collections.deque() ## 파이썬에서는 queue 사용시 deque 추천 (속도가 빠름)


cnt=0
answer_cnt=0
for i in range(n):
    for j in range(m):
        if picture[i][j]==1 and check[i][j]==False: # 이동할수있으면 이동 
            check[i][j]=True
            cnt2=1
            cnt+=1
            queue.append([i,j])
            while queue:
                  cur_x,cur_y=queue.popleft() 
                  for z in range(4): ## 현재위치에서 상하좌우  확인
                      da=dx[z]+cur_x  
                      db=dy[z]+cur_y

                      if da<0 or da>=n or db<0 or db>=m:continue #이동할수없는 좌표면
                      if picture[da][db]==1 and check[da][db]==False: ##이동할수있으면 
                          check[da][db]=True #이동
                          queue.append([da,db])
                          cnt2+=1

            answer_cnt=max(answer_cnt,cnt2)


print(cnt)
print(answer_cnt)

