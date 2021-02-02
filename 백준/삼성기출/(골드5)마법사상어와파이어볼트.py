dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]

# 1. 파이어볼이있는곳을 찾는다.
def find_fireball():
    global fire_ball,n
    fire_ball_list=[]

    for i in range(1,n+1):
        for j in range(1,n+1):
            if len(fire_ball[(i, j)])!=0:
               fire_ball_list.append([i,j])


    return  fire_ball_list

# 2. 파이어볼을 움직인다 .
def move_fireball():
    global n

    # 1. 파이어볼이 있는곳을 찾음
    fire_ball_list=find_fireball()

    tmp_list=[]

    # 2. 파이어볼을 이동시킨다.
    while len(fire_ball_list) !=0:
          fire_x,fire_y=fire_ball_list.pop(0)
          fireball_info=fire_ball[(fire_x,fire_y)]

          while len(fireball_info)!=0:
                m, speed, direction = fireball_info.pop(0)
                next_x, next_y = fire_x, fire_y
                t = speed
                while t!=0:
                    next_x, next_y = next_x + dx[direction], next_y + dy[direction]
                    if next_x == 0:
                        next_x = n

                    if next_x == n + 1:
                        next_x = 1

                    if next_y == 0:
                        next_y = n

                    if next_y == n + 1:
                        next_y = 1

                    t -= 1

                # 이동시킬 파이어볼을 리스트에담음
                tmp_list.append([next_x,next_y,m,speed,direction])



    #  나중에 이동시킴
    while len(tmp_list)!=0:
          x,y,m,s,dir=tmp_list.pop(0)
          fire_ball[(x,y)].append((m,s,dir))



def fire_ball_merge():
    global fire_ball

    # 파이어 볼이 두개이상인것만 합친다
    # 1. 파이어볼 2개이상 찾음
    # 2. 파이어볼 2개이상인거의 리스트값을 계속 반복함
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if len(fire_ball[(i, j)]) >=2: # 파이어볼이 2개이상있고
                fire_x,fire_y=i,j
                fireball_info = fire_ball[(fire_x, fire_y)]
                merge_m = 0
                merge_speed = 0
                cnt = len(fireball_info)
                check_direction = []

                while len(fireball_info) != 0:
                    m, speed, direction = fireball_info.pop(0)
                    merge_m += m
                    merge_speed += speed
                    check_direction.append(direction)

                if (merge_m//5)==0:
                    continue

                if check_dir(check_direction):
                    merge_m = merge_m // 5
                    merge_speed = merge_speed // cnt
                    fire_ball[(fire_x, fire_y)].append([merge_m, merge_speed, 0])
                    fire_ball[(fire_x, fire_y)].append([merge_m, merge_speed, 2])
                    fire_ball[(fire_x, fire_y)].append([merge_m, merge_speed, 4])
                    fire_ball[(fire_x, fire_y)].append([merge_m, merge_speed, 6])

                else:
                    merge_m = merge_m // 5
                    merge_speed = merge_speed // cnt
                    fire_ball[(fire_x, fire_y)].append([merge_m, merge_speed, 1])
                    fire_ball[(fire_x, fire_y)].append([merge_m, merge_speed, 3])
                    fire_ball[(fire_x, fire_y)].append([merge_m, merge_speed, 5])
                    fire_ball[(fire_x, fire_y)].append([merge_m, merge_speed, 7])


    return


# 파이어볼 방향 체크

def check_dir(check_direction):
    check_direction.sort()
    even=False
    odd=False
    if check_direction[0]%2==0:
       even=True

    else:
         odd=True

    if even:
       for i in check_direction:
           if i%2==1:
               return False

       return True

    elif odd:
         for i in check_direction:
             if i%2==0:
                 return False

         return True






n,t,k=map(int,input().split())  # n *n 격자 , m = 파이어볼수 , k=명령횟수

board=[0]*(n+1)
fire_ball=dict()
for i in range(n):
    board[i]=[0]*(n+1)

for i in range(1,n+1):
    for j in range(1,n+1):
        fire_ball[(i,j)]=[]



while t!=0:
      r,c,m,s,d=map(int,input().split())
      fire_ball[(r,c)].append([m,s,d]) # 질량 속도 방향
      t-=1

answer=0
while k!=0:
      move_fireball()
      fire_ball_merge()
      k-=1


# 정답 갱신

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if len(fire_ball[(i, j)]) != 0:
            for z in fire_ball[(i, j)]:
                answer+=z[0]


print(answer)
