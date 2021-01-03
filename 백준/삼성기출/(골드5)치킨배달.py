import itertools
n,m=map(int,input().split())
board=[0]*n
house_pos=[]
chiken_pos=[]
answer=999999999
# 1. 맵 입력
for i in range(n):board[i]=list(map(int,input().split()))

for i in range(n):
    for j in range(n):
        if board[i][j]==1: # 1. 집
            house_pos.append([i,j])
        elif board[i][j]==2: # 1-2. 치킨 집
             chiken_pos.append([i,j])



chiken_pos_list=list(itertools.combinations(chiken_pos,m)) ## 1. 치킨집들중에 m개의 치킨 집을 뽑는 경우


answer=999999999

for i in chiken_pos_list:
    total = 0
    for j in house_pos:
        house_x,house_y=j #현재집
        chiken_distance=99999999
        for z in i:
            chiken_x,chiken_y=z ## 1. 현재집에서 뽑은 조합들중에 최소 치킨거리를 구한다.
            chiken_distance=min(chiken_distance,abs(house_x-chiken_x)+abs(house_y-chiken_y))

        total+=chiken_distance # 2.현재집의 최소 치킨거리를 누적 

    answer=min(total,answer)


print(answer)





