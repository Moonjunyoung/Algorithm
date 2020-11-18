dx=[1,0,-1,0]
dy=[0,1,0,-1]
#아래,오른쪽 옆, 위,왼쪽 옆


## 개씹 노가다 구현 원리모름

n,m,r=map(int,input().split())
array=[[0]]*n

for i in range(n):array[i]=list(map(int,input().split()))


array_location=[[0]]*n
for i in range(n):array_location[i]=[0]*m
tmp_array=[[0]]*n
for i in range(n):tmp_array[i]=[0]*m
## 임시 배열을 만듬

for i in range(n):
    for j in range(m):
        tmp_array[i][j]=array[i][j]


start_x=0
start_y=0

cur=0
flag=False
cnt=0
while True:
    if flag:
        break

    while True: 
        a=dx[cur]+start_x
        b=dy[cur]+start_y

        # 1. 해당 범위에 있고 값이 채워져있지않으면 이동가능
        if a<n and b<m and a>=0 and b>=0 and array_location[a][b]==0:
                array_location[a][b]=(start_x,start_y)
                cnt+=1
                start_x=start_x+dx[cur]
                start_y=start_y+dy[cur]

        # 2. 해당범위에 있지않고 값이 채워져있는 경우 
        else:
            if cnt==m*n: ## 2-1. 값이 모두다 채워진경우 1_ rotation 성공
                for i in range(n):
                    for j in range(m):
                        a,b=array_location[i][j]  
                        array[i][j]=tmp_array[a][b] 
                        array_location[i][j]=0

                for i in range(n):
                    for j in range(m):
                        tmp_array[i][j]=array[i][j]

                start_x=0
                start_y=0
                cur=0

                if r==1: ##2-2 회전을 다한 경우 종료를 시킴
                   flag = True
                   break
                else: #2-1-1 회전 다 안한경우엔 1 감소
                    r-=1
                    cnt=0
                    break

            if cur==3: # 4번 다돌았으면 다음 좌표로 이동
                start_x+=1
                start_y+=1
                cur=0

            else:
                cur+=1
            break


for i in range(n):
    for j in range(m):
        print(array[i][j],end=' ')
    print()





