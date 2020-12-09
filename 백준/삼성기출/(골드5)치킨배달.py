import itertools

n, m = map(int, input().split())
board=[0]*n
for i in range(n):board[i]=list(map(int,input().split()))

house=[]
chiken=[]
answer=99999999

for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            house.append([i,j])
        elif board[i][j]==2:
            chiken.append([i,j])


# 1. 치킨집들 중에 중복이 안되게 m개의 치킨집을 뽑는 경우를 찾는다 .
combination_list=list(itertools.combinations(chiken,m))


answer=999999999
for i in combination_list:
    total=0
    for z in house: ##2.경우의수에 따라 모든 집의 좌표에서 치킨거리를 구함
        house_x=z[0]
        house_y=z[1]
        dis = 999999999
        for j in i: #3. 현재 집좌표에서 고를수있는 치킨집들중 치킨거리를 구함
            chiken_x = j[0]
            chiken_y = j[1]
            dis=min(dis,abs(house_x-chiken_x)+abs(house_y-chiken_y))

        total+=dis

    answer=min(total,answer)


print(answer)



