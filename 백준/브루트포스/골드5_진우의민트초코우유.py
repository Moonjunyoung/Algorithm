import itertools

def distance(jinwo_x,jinwo_y,milk_x,milk_y):
    return abs(milk_x-jinwo_x)+abs(milk_y-jinwo_y)


n,m,h=map(int,input().split()) # 마을크기 , 진우초기체력 , 증가하는 양
board=[0]*n
for i in range(n):board[i]=list(map(int,input().split()))
milk_list=[]

jinwo_x,jinwo_y=0,0
for i in range(n):
    for j in range(n):
        if board[i][j]==2:
            milk_list.append([i,j])

        elif board[i][j]==1:
             jinwo_x,jinwo_y=i,j


permute=list(itertools.permutations(milk_list))
answer=0
for i in permute:
    jinwo_hp=m
    j_x,j_y=jinwo_x,jinwo_y
    cnt=0
    for j in i:
        cost=distance(j_x,j_y,j[0],j[1]) # 진우위치에서 해당 우유까지 거리
        c = distance(j[0], j[1], jinwo_x, jinwo_y)  # 해당 우유 에서 집까지 거리
        if jinwo_hp>=cost: # 해당우유를 먹을수있으면
           cnt+=1
           jinwo_hp -= cost
           jinwo_hp += h  #hp상승
           if jinwo_hp>=c: #집에 갈수있으면 갱신
               answer = max(cnt, answer)

           j_x, j_y = j[0], j[1]

        else:
             break



print(answer)
